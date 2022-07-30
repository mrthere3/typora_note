<h1 align = "center">javscript基础学习</h1> 

## 学习概要

- JavaScript语法基础
- DOM 和BOM
- jQuery

## 1.JavaScript介绍

### 1.1  *JavaScript* 导入形式

+ 写入在**html**内部或者写入在**内部**低端，不影响html的正常加载.

  ```html
  <script type = "text/javascript"> </script>
  ```

  

+ 写入到单独的JS文件进行导入

  ```html
  <script src = "src/js"> </script>
  ```

### 1.2  *JavaScript* 在html中的注释形式



```
// 注释内容
/* 注释内容 */
```

## 2.*JavaScript* 语法

### 2.1 *JavaScript* 基本常用的数据类型

#### 2.1.1 字符串类型

```javascript
var name ="小亮";
var name = String("小亮");
```

```javascript
var name ="中国联通";
var v1 = name.length;
var v3 =name.trim() //去除收尾空白字符//
var v4 = name.substring(0,2) //左闭右开 此行代码中国//

```

#### 2.1.2 数组类型

```javascript
v1 = [1,2,3,4]; //定义一个初始数组
v1 = Array[1,2,3,4]; //使用数组关键字Array进行定义
```

```javascript
//基本数组操作
v1 = [1,2,3,4];
v1[1] = 3 //设置值
v1.push("5") //尾插入元素
v1.unshift("5") //首部插入元素
v1.splice(0,"1") //参数含义 索引 + 元素  将元素1插入到0索引处
v1.pop()  //尾部删除，返回被删除元素
v1.shift() //首部删除，返回被删除元素
v1.splice(0,1) //指定位置删除 1为默认值 表示将0索引的元素删除 ，返回被删除元素
```

```javascript
//数组遍历 常见的遍历方式
v1 = [1,2,3,4];
1.
for(var item in v1){
    console.log(v1[item])
}
2.
for(var i =0 ,i<v1.length,i++){
   console.log(v1[i) 
}
```

#### 2.1.3 对象(字典)

```javascript
info = {
"name":"小亮";
  name:小亮 //双引号可加可不加
} 
//定义字典对象
//获取对应的值
info.name  //定义时候不加双引号
info["name"] //不加双引号

```

```javascript
//字典遍历
for(var key in info){
    console.log(info["key"])
//遍历出来的key是键
}
```

### 2.2 条件语句

```javascript
if (条件){

}else{

}

```

```javascript
if (条件){

}else if (条件){

}else{
    
}
```

## 3.浏览器*DOM*对象(document)

### 3.1 内容获取

```javascript
//根据id获取标签
var tag = document.getElementById("xx");
//获取文本内容
tag.innerText
//修改标签内容
tag.innerText=“哈哈

```

```javascript
//创建标签<div></div>
var tag= document.createElement("div")
//内容修噶爱
tag.innerText = "123"
li = document.creaateElement("li")
tag.ppendChild(li) //将div标签下添加li标签
```

### 3.2 事件添加

```html
//绑定事件
案例
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
    <input type="text" placeholder="请输入内容" id="txUser">
    <input type="button" value="请添加" onclick=addCityinfo()>
    <ul id="city">

    </ul>
    <script type="text/javascript">
        function addCityinfo(){
            var txtTag=document.getElementById("txUser")
            var newstring = txtTag.value
            if (newstring) {
                var newtag = document.createElement("li")
                newtag.innerText = newstring
                var partent = document.getElementById("city")
                partent.appendChild(newtag)
                txtTag.value = ""
            }else {
                alert("请输入内容")
            }

        }
    </script>

</body>
</html>
```



$\color{red}Dom还有很多语法，这只是了解，后续开发基本都是用组件或者jquery来进行开发.$

## 4.编码相关

+ ascII编码 256中对应关系
+ gbk2321,gbk  中文 占两个字节
+ unicode,ucs2/ucs4 包括现在发现的所有文明
+ utf-8编码  一个中文占3个字节

## 5.*JQuery* 学习

### 5.1 *JQuery*简介

+ JQuery是javascript的一个类库
+ 基于jquery来进行开发

### 5.2快速上手

+ ```javascript
  npm install jquery
  ```

+ ```html
  <!DOCTYPE html>
  <html lang="en">
  <head>
      <meta charset="UTF-8">
      <title>Title</title>
      <script src="node_modules/jquery/dist/jquery.js"></script>
  </head>
  <body>
      <h1 id="info"> 中国联通</h1>
     <script type="text/javascript">
         //document.getElementById("info").innerText = "西安"
          $("#info").text("西安");
      </script>
  
  
  </body>
  </html>
  ```
  
  ![](https://raw.githubusercontent.com/mrthere3/typora_note/master/img/js/20220729190618.png)
  
  
  
  <div align="center"> 
      <font style="color:red" size = "5">使用jquery将原本的中国联通修改为西安</font> 
  </div>

### 5.3 *JQeuy* 寻找标签

#### 基本选择器样式

+ ID选择器

  ```html
  $("#id")
  ```

+ 样式选择器

  ```htm
  $(".class")
  ```


+ 标签选择器

  ```javascript
  $("h1")
  ```

+ 层级选择器

  ```javascript
  $(".c1 .c2 a")
  ```

  + 1. 后代元素选择器 

       ```javascript
       $('div span') //选取\<div>里的所有的\<span>元素。

    2. 子元素选择器       

       ```javascript
       $('div>span')//选取\<div>元素下元素名是\<span>的子元素。
       ```

    3. 相邻元素选择器    

       ```javascript
       $('.one+div')//选取class为one的下一个\<div>兄弟元素。
       ```

       

    4. 兄弟元素选择器   

       ```javascript
       $('#two~div')//选取Id为two的元素后面的所有\<div>兄弟元素。
       ```

       

  + 多选择器

    ```javascript
    $(".c1 ,c2, a") //用逗号分割开
    ```

+ 属性选择器

  ```javascript
  $("input[name ='n1']")
  ```

+ 群组选择器    

       ```javascript
       $("p a.test")//选取在p元素内 拥有class为test的a元素。
       ```

  

+ 间接寻找

  ```html
  <div>
      <div>北京</div>
      <div id='c1'>上海</div>
      <div>深圳</div>
  </div>
  ```

  ```javascript
  $('#id').prev()
  $('#id').next()
  $('#id').siblings() //定位所有的兄弟标签
  $('#id').parent() //定位标签的父标签
  $('#id').children() //定位标签的所有孩子标签
  $('#id').children(“.p10) //定位标签的所有孩子标签寻找class=p10的标签
  $('#id').find(“.p10) //定位标签的所有子孙标签寻找class=p10的标签
  $("div :first-child")  //选取每个\<div>下第一个子元素
  $("div :last-child") //选取每个\<div>下最后一个子元素
  $("div :only-child") //选择只有一个子元素的\<div>元素
  ```

#### 过滤选择器

```javascript
:first //选取第1个元素 
$('div:first') //选取所有\<div>元素中第1个\<div>元素。

:last  //选取最后一个元素
$('div:last') //选取所有\<div>元素中最后1个\<div>元素。

:not(selector) //去除所有与给定选择器 匹配的元素 
$('input:not(.myClass)') //选取class不是myClass的\<input>元素。

:even // 选取索引(从0开始)是偶数 的所有元素
$('input:even')//选取索引是偶数的\<input>元素。

:odd //选取索引(从0开始)是奇数 的所有元素
$('input:odd') //选取索引是奇数的<input>元素。

:eq(index) //选取索引(从0开始)等于 index的元素
$('input:eq(1)') //选取索引等于1的<input>元素。

:gt(index) //选取索引(从0开始)大于 index的元素
$('input:gt(1)') //选取索引大于1的\<input>元素。

:lt(index) //选取索引(从0开始)小于 index的元素
$('input:gt(1)') //选取索引小于1的\<input>元素。

:header //选取所有的标题元素，即 \<h1>到\<h6> 
$(':header') //选取网页中所有的\<h1>,\<h2>,\<h3>...

:animated  //选取当前正在执行动画的所有元素
$('div: animated') //选取正在执行动画的\<div>元素。

```

#### 内容过滤器

```javascript
:contains(text)  
$("div:contains('test')") //选取含有文本内容为test的\<div>元素

:empty  // 选取不包含子元素或文本的空元素
$("div:empty") //选取不包含子元素或文本的空\<div>元素

:has(selector)  //选取含有给定选择器 匹配的元素的元素
$("div:has(.myClass)") //选取含有class为 myClass的元素的\<div>元素

:parent //选取含有子元素或文本的元素
$("div:parent") //选取含有子元素或文本的\<div>元素

:hidden //选取所有不可见的元素
$("div:hidden") //选取所有不可见的\<div>元素

:visible  //选取所有不可见的元素
$("div:visible") //选取所有可见的\<div>元素
```

#### 属性选择器

```javascript
[attribute]  //选取拥有此属性的元素 
$("div[id]") //选取拥有属性id的元素

[attribute=value] 
$("div[title=test]") //选取属性 title 为test的\<div>元素

[attribute!=value] 
$("div[title=test]") //选取属性 title 不为test的\<div>元素

[attribute^=value] //选取属性的值以value开始的元素
$("div[title^=test]") //选取属性 title 以 test 开始的\<div>元素

[attribute$=value]    //选取属性的值以value结束的元素
$("div[title$=test]") //选取属性 title 以 test 结束的\<div>元素

[attribute*=value]   //选取属性的值含有value的元素
$("div[title*=test]") //选取属性 title 含 有 test 的\<div>元素

[selector1][selector2]...[selectorN]  //选取匹配以上所有属性 选择器的元素
$("div[id][title*=test]") //选取拥有属性id， 且属性 title 含有 test 的\<div>元素
```

#### 表单选择器

```javascript
$(':input') //选取所有<input>,<textarea>,<select>和<button>元素。

 $(':text') //选取所有的单行文本框。
```

### 5.4 *JQuery* 值处理

#### 5.4.1 修改标签值

```html
<div id = 'c1'> 内容</div>
```

```javascript
$("#id").text() //获取文本内容
$("#id").text("haha") //修改文本内容
```

```html
<input type='text',id='c2'/>
```

```javascript
$("#c2").val() //获取用户输入的值
$("#c2").val('haha') //修改用户输入的值
```

#### 5.4.2增加标签值

```javascript
$("<li>")  //创建li标签
$("#view").append($("<li>")) //将li标签添加到id=view 下
$("#view").removeCss("color") //移除css属性color
$("#view").addCss("color") //增加css属性color
$("#view").hasCss("color") //判断是否存在css属性color 返回ture和false
```

#### 5.4.2删除标签值

```javascript
$("#c2").remove()
```

### 5.5 *JQuery* 绑定事件



```html
<ul>
    <li>上海</li>
    <li>北京</li>
    <li>深圳</li>
</ul>
```

1. onclick()<!--==点击事件==-->

```javascript
$(function{$("#id").onclik(funtion(){
        var text = $(this).text()  //当前点击的标签
		console.log(text)
                });
});
//$(function) 当页面框架加载完成开始执行函数
```

2.  dblclick() <!--==双击事件==-->

   ```javascript
   $("p").click(function(){
     $(this).hide();
   });
   ```

3.  mouseenter() <!--当鼠标指针穿过元素时，会发生 mouseenter 事件。-->

   ```javascript
   $("#p1").mouseenter(function(){
       alert('您的鼠标移到了 id="p1" 的元素上!');
   });
   ```

4. mouseleave() <!--当鼠标指针离开元素时，会发生 mouseleave 事件。-->

   ```javascript
   $("#p1").mouseleave(function(){
       alert("再见，您的鼠标离开了该段落。");
   });
   ```

5. mousedown()  <!--当鼠标指针移动到元素上方，并按下鼠标按键时，会发生 mousedown 事件-->

   ```javascript
   $("#p1").mousedown(function(){
       alert("鼠标在该段落上按下！");
   });
   ```

6.  mouseup()  <!--当在元素上松开鼠标按钮时，会发生 mouseup 事件-->

   ```javascript
   $("#p1").mouseup(function(){
       alert("鼠标在段落上松开。");
   });
   ```

7. hover() <!--用于模拟光标悬停事件。-->

   ```javascript
   $("#p1").hover(
       function(){
           alert("你进入了 p1!");
       },
       function(){
           alert("拜拜! 现在你离开了 p1!");
       }
   );
   //当鼠标移动到元素上时，会触发指定的第一个函数(mouseenter);当鼠标移出这个元素时，会触发指定的第二个函数(mouseleave)。
   ```

8. focus()  <!--当元素获得焦点时，发生 focus 事件。当通过鼠标点击选中元素或通过 tab 键定位到元素时，该元素就会获得焦点。-->

   ```javascript
   $("input").focus(function(){
     $(this).css("background-color","#cccccc");
   });
   ```

9.  blur()  <!--当元素失去焦点时，发生 blur 事件。-->

   ```javascript
   $("input").blur(function(){
     $(this).css("background-color","#ffffff");
   });
   ```

   
