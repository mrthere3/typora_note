import time

from django.shortcuts import render,HttpResponse,redirect
from app01.models import Department
from django.contrib import messages
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    return render(request,'index.html',{'data_list':['发票', '海关缴款书', '代扣代缴', '农产品加计扣除发票信息', '农产品加计扣除海关文书', '异常发票']})
#
def depart_index(request):
    index =1
    page_size = 10
    if request.method == "GET":
        index = int(request.GET.get("index",1))
        page_size = int(request.GET.get("pagesize",3))
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
        print(request.POST)
        odepart = request.POST.get("old_depart_name")
        ndepart = request.POST.get("depart_name")
        Department.objects.filter(title=odepart).update(title=ndepart)

    return redirect("/depart/list/")

