# *Python* 与*Mysql*  学习

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

## 2.mysq了语法（回顾）

### 2.1数据库

+ 查看数据库

  ```
  show databases;
  ```

+ 创建数据库

  ```
  create databases 数据库名字 default charset utf-8 cllate utf-8_general_ci;
  ```

+ 删除数据库

  ```
  drop database 数据库名字;
  ```

+ 进入数据库

  ```
  use database 数据库名字;
  ```

### 2.2 数据表

