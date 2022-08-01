#  *Python* 与*Mysql*  学习

## 1.安装mysql

### 1.1 docker快速部署

~~~dockerfile
docker run --name mysql01 -d -p 3306:3306 -v G:/dockerdata/mysql/conf:/etc/mysql/conf.d -v G:/dockerdata/mysql/data:/var/lib/mysql -v G:/dockerdata/mysql/logs:/etc/mysql/logs -e MYSQL_ROOT_PASSWORD=123456 -d mysql:5.7 
~~~

### 1.2 忘记密码操作

+ 暂停mysql服务
+  进入容器  vim /etc/mysql/conf.d/docker.cnf 修改相关配置文件 添加$\color{red}{skip-grant-tables}$ 无密码登录模式，这样不需要密码可以直接以root身份登录，然后重设密码
+  重置密码 容器内<mysql : use mysql; update mysql.user set authentication_string=password('root') where User='root';
+ 刷新权限flush privileges;
+ 再删除第二步加的$\color{red}{skip-grant-tables}$  使用密码登录模式
+ 重启MySQL5、重启MySQL

## 2.mysq语法（回顾）

### 2.1数据库

+ 查看数据库

  ```sql
  show databases;
  ```

+ 创建数据库

  ```
  create databases 数据库名字 default charset utf-8 cllate utf-8_general_ci;
  ```

+ 删除数据库

  ```sql
  drop database 数据库名字;
  ```

+ 进入数据库

  ```
  use database 数据库名字;
  ```

### 2.2 数据表

+ 查看表

  ```sql
  show databases
  ```


+ 创建表

  ```sql
  create table 表名(
         id int,  #列名称 类型,
         name varchar(16)  #列名称 类型,
         age int  #列名称 类型,
  )default charset=utf-8
  
  
  create table 表名(
  	   id int auto_increment primary key, #设置主键 （主键不允许为空）auto 为自加关键字
         name varchar(16)  not null #列名称 类型  不允许为空
         age int default 3  #插入数据时age列默认值为3  
  
  )default charset=utf-8  
  ```

+ 删除表

  ```sql
  drop table 表名
  ```



### 2.3 常用数据类型

+ tinyint

  ```sql
  #有符号  取值范围 -128~127
  #无符号 取值范围 0~255 unsinght
  
  create table tb(
      	id int auto_increment primary key,
          age tinyint unsigned, 
  
  )default charset=utf-8
  
  ```

+ int

  ```sql
  #带符号范围- 2147483648~2147483647
  #无符号范围是 0~4294967295。
  ```

  

+ bigint

  ```sql
  #有符号范围是 -9223372036854775808~9223372036854775807
  #无符号范围是  0 ~ 18446744073709551615
  ```

+  float

+ double

+ decimal

  ```sql
  create table tb(
      	id int auto_increment primary key,
          salary decimal(m,d), 
  
  )default charset=utf-8
  # m代表数字总数（不包含负号），d 代表小数点后个数 m最大值为65，d最大值为30
  ```

+ char(m) 查询速度快

  ```sql
  #定长字符串 m最大容纳数255字符
  char(11) #固定存储11个字符 哪怕不足11个，也会存11个
  ```

+ varchar 更节省内存

  ```sql
  #变长字符串 最大容纳数65535字节 /3 = m最大字符
  varchar(11)  #真实有多长就存储多长 最长存储长度11
  ```

+ text

  ```sql
  #一般用来存储可变的大字符串 65535（2**16-1）字符
  长文本一般使用text 新闻 文章
  ```

+ mediumtext

  ```sql
  #可以存储2**24-1(16777215)字符
  ```

+ longtext

  ```sql
  #可存储2**32-1 字符 or 4GB
  ```

+ datetime

  ```sql
  YYYY-MM-DD HH:MM:SS
  ```

+ date

  ```sql
  YYYY-MM-DD
  ```

  



