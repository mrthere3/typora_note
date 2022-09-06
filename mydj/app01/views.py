import time

from django.http import JsonResponse
from django.shortcuts import render,HttpResponse,redirect
from app01.models import Department,UserInfo,Adminuser
from django.contrib import messages
from django.core.paginator import Paginator
from django.forms import ModelForm
from django.core import serializers
from django.core.validators import RegexValidator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
class userform(ModelForm):
    class Meta:
        model = UserInfo
        fields ="__all__"
        exclude = ["password"] #

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.widget.attrs = {"class":"form-control"}

class loginrform(ModelForm):
    class Meta:
        model = Adminuser
        fields ="__all__"
        exclude = ["create_time"] #


def depart_index(request):
    index =1
    page_size = 10
    if request.method == "GET":
        index = int(request.GET.get("index",1))
        page_size = int(request.GET.get("pagesize",10))
    query_set = Department.objects.all()
    paginator = Paginator(query_set, page_size)
    try:
        pages = paginator.page(index) # 可能请求的页数大于 实际分页数目
    except:
        index = paginator.num_pages #针对超出直接返回到最后一页数据
        last = paginator.num_pages
        pages = paginator.page(last)
    # print(query_set)
    startindex = page_size*(index-1)
    return render(request,"depart_list.html",{'depart_list':pages,"start_index":startindex})


def depart_add(request):
    if request.method == "POST":
        depaer_ment=request.POST.get("depart_name")
        depart_query = Department.objects.filter(title=depaer_ment)
        if not depart_query:
            Department.objects.create(title=depaer_ment)
    # time.sleep(2)
    return redirect("/depart/list/")


def depart_delete(request):
    print(request.path)
    nid = request.GET.get("nid")
    Department.objects.filter(id=nid).delete()
    return redirect("/depart/list/")


def depart_edit(request):
    if request.method =="POST":
        # print(request.POST)
        odepart = request.POST.get("old_depart_name")
        ndepart = request.POST.get("depart_name")
        Department.objects.filter(title=odepart).update(title=ndepart)

    return redirect("/depart/list/")


def user_list(request):
    index = 1
    page_size = 10
    if request.method == "GET":
        index = int(request.GET.get("index", 1))
        page_size = int(request.GET.get("pagesize", 10))
    query_set = UserInfo.objects.all()
    paginator = Paginator(query_set, page_size)
    try:
        pages = paginator.page(index)  # 可能请求的页数大于 实际分页数目
    except:
        index = paginator.num_pages  # 针对超出直接返回到最后一页数据
        last = paginator.num_pages
        pages = paginator.page(last)
    # print(query_set)
    startindex = page_size * (index - 1)
    # mydjform = userform(instance=UserInfo.objects.filter(name="王工").first())
    mydjform = userform()
    return render(request, "userinfo_list.html", {'user_list': pages, "start_index": startindex,"form":mydjform})

# def user_list(request):
#     user_list = UserInfo.objects.all()
#     mydjform = userform()
#     return render(request,"userinfo_list.html",{"form":mydjform,"user_list":user_list,"start_index":0})

def user_add(request):
    if request.method == "POST":
        myform = userform(data=request.POST)
        if myform.is_valid():
            myform.save()
            return JsonResponse({"msg":"处理完成"})
        else:
            print(myform.errors)
            return JsonResponse({"msg":"处理失败 ","error_message":myform.errors})

def user_delete(request):
    # print(request.path)
    nid = request.GET.get("nid")
    UserInfo.objects.filter(id=nid).delete()
    return redirect("/user/list/")

@csrf_exempt
def user_edit(request):
    # print(request.path)
    try:
        if request.method == "POST":
            print(request.POST)
            myform = userform(data=request.POST)
            if myform.is_valid():
                user_info = UserInfo.objects.filter(name=request.POST.get("name"))
                myform = userform(data=request.POST, instance=user_info.first())
                myform.save(commit=True)
                return JsonResponse({"msg":"处理完成"})
            else:
                print(myform.errors)
                return JsonResponse({"msg":"处理失败","error_message":myform.errors})
        else:
            # print(request.GET)
            user_info = UserInfo.objects.filter(id=request.GET.get("id"))
            user_json = serializers.serialize("json", user_info)
            return JsonResponse({"msg":"处理完成","user_info":user_json,"data_method":"get"})
    except Exception as e:
        return JsonResponse({"msg": "处理失败","error_message":e})

def user_login(request):
    if request.method == "GET":
        return render(request,"admin-login.html")
    else:
        login_info = loginrform(request.post)
        if login_info.is_valid():
            admin_object = Adminuser.objects.filter(**login_info.cleaned_data).exists()
            if admin_object:
                request.user = admin_object.name
                return redirect(request,"userinfo_list.html")
            else:
                return render(request,"admin-login.html",{'form':login_info})



