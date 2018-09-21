创建app  (添加到installed apps)
python manage.py startapp my_app

依赖文件生成
pip freeze > requirements.txt
依赖文件安装
pip install -r requirements.txt

添加静态资源，在settings.py中最后一行添加
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)  # 开发时创建的静态目录

创建表
python manage.py makemigrations
python manage.py migrate

路由分发：需要将自己创建的views文件夹添加到