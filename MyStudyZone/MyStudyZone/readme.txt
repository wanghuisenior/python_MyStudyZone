创建app  (添加到installed apps)
python manage.py startapp testApp

依赖文件生成
pip freeze > requirements.txt
依赖文件安装
pip install -r requirements.txt

添加静态资源，在settings.py中最后一行添加
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)  # 开发时创建的静态目录

创建表
python manage.py makemigrations
python manage.py migrate

对queryset进行序列化
from django.core import serializers
serializers.serialize('json', queryset)
开启项目远程访问
1 开启mysql数据库远程访问：
新建查询
mysql> use mysql;
Database changed
mysql> grant all privileges  on *.* to root@'%' identified by "root";
2 让别人通过IP访问我的电脑（服务器必须开启）：
在settings.py中加入 ALLOWED_HOSTS = ['*'] # 我的电脑的ip地址
                    数据库改为宿主数据库地址 'HOST': '192.168.16.198',
3 找到项目中manage.py的位置，打开命令行运行以下命令
python manage.py runserver 0.0.0.0:8000


wps/excel  layui数据表格导出文件，打开提示已经检测到"XXX.xsl"是SYLK文件,但是不能将其加载的问题
当您打开一个文本文件、 CSV 文件和文件的前两个字符是大写字母"I"，"D"时，会发生此问题。
如果将ID中的任意字母换成小写都不会出现此问题，估计是固定的识别“ID”或“ID_XXXX”
解决：将ID列重命名

layui表格如何隐藏某个列：
    直接再表格中不定义该列即可，  后面仍然可以获取到
    或者再done函数中加入 $("[data-field='id']").css('display', 'none'); //隐藏列
