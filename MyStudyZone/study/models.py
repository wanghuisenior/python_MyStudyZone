import uuid

from django.db import models


# ForeignKey：一对多，将字段定义在多的一端中
# ManyToManyField：多对多，将字段定义在两端中
# OneToOneField：一对一，将字段定义在任意一端中
# ##########################选项
# null：如果为True，表示允许为空，默认值是False
# blank：如果为True，则该字段允许为空白，默认值是False
# 对比：null是数据库范畴的概念，blank是表单验证证范畴的
# db_column：字段的名称，如果未指定，则使用属性的名称
# db_index：若值为True, 则在表中会为此字段创建索引，默认值是False
# default：默认值
# primary_key：若为True，则该字段会成为模型的主键字段，默认值是False，一般作为AutoField的选项使用
# unique：如果为True, 这个字段在表中必须有唯一值，默认值是False
# Create your models here.
class User(models.Model):
	# 使用uuid作为主键，auto_created无需在创建对象时指定主键的值
	# MySQL数据库中UUIDField类型一定是32位的char类型，在数据库Model中，
	# 开发者不需要设置max_length = xxx，因为这个max_length的数值默认的一定是32
	user_id = models.UUIDField(primary_key=True, auto_created=True, default=uuid.uuid4, editable=False)
	user_name = models.CharField(max_length=255)
	user_tel = models.CharField(max_length=255)
	user_email = models.EmailField(max_length=255)
	user_info = models.TextField(blank=True, null=True)
	create_time = models.DateTimeField(auto_now_add=True)  # auto_now无论是你添加还是修改对象，时间为你添加或者修改的时间
	update_time = models.DateTimeField(auto_now=True)  # auto_now_add为添加时的时间，更新对象时不会有变动。
	# 如果已经在setting配置了MEDIA_ROOT = os.path.join(BASE_DIR, "static/media")，那么将创建photos文件夹
	image = models.ImageField(upload_to='photos', default='photos/default_user.jpg')

	class Meta:
		ordering = ['-update_time']

	# authors = models.ManyToManyField(Author)  # 多对多，会生成中间表book_authors
	# publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)  # 一对多，将字段定义在多的端中
	def encode2json(self):
		return {'user_id': self.user_id, 'user_name': self.user_name, 'user_tel': self.user_tel,
				'user_email': self.user_email,
				'user_info': self.user_info, 'create_time': self.create_time, 'update_time': self.update_time}

# 基本查询
# exact：表示判等
#
# 例：查询编号为1的图书
# list=BookInfo.books.filter(id__exact=1)
# 可简写为：
# list=BookInfo.books.filter(id=1)
# 不等于使用等于的运算符，使用exclude()过滤器
# 例：查询编号不等于3的图书
# list = BookInfo.books.exclude(id=3)
# contains：是否包含
# 说明：如果要包含%无需转义，直接写即可
# 例：查询书名包含‘传’的图书
# list=BookInfo.books.filter(btitle__contains='传'
# startswith、endswith：以指定值开头或结尾
# 例：查询书名以‘部’结尾的图书
# list=BookInfo.books.filter(btitle__endswith='部')
# isnull：是否为null
# 例：查询书名不为空的图书
# list = BookInfo.books.filter(btitle__isnull=False)
# in：是否包含在范围内
# 例：查询编号为1或3或5的图书
# list = BookInfo.books.filter(pk__in=[1, 3, 5])
# gt、gte、lt、lte：大于、大于等于、小于、小于等于不等于
# 查询编号大于3的图书
# list = BookInfo.books.filter(id__gt=3)
# year、month、day、week_day、hour、minute、second：对日期时间类型的属性进行运算
# 例：查询1980年发表的图书
# list=BookInfo.books.filter(bpub_date__year=1980)
# F对象(属性比较)
# 语法如下  F(属性名)
# 例：查询阅读量大于等于评论量的图书
# from django.db.models import F
# ...
# list = BookInfo.books.filter(bread__gte=F('bcommet'))
# 可以在F()对象上使用算数运算
# 例：查询阅读量大于2倍评论量的图书
# list = BookInfo.books.filter(bread__gt=F('bcommet') * 2)
# Q对象(多个过滤器逐个调用表示逻辑与关系，同sql语句中where部分的and关键字)
#
#
# 例：查询阅读量大于20，并且编号小于3的图书
# list=BookInfo.books.filter(bread__gt=20,id__lt=3)
# 或
# list=BookInfo.books.filter(bread__gt=20).filter(id__lt=3)
# 如果需要实现逻辑或or的查询，需要使用Q()对象结合|运算符
#
# Q对象被义在django.db.models中
# 语法：Q(属性名__运算符=值)
#
# 例：查询阅读量大于20的图书，改写为Q对象如下
# from django.db.models import Q
# ...
# list = BookInfo.books.filter(Q(bread__gt=20))
# Q对象可以使用&、|连接，&表示逻辑与，|表示逻辑或
# 例：查询阅读量大于20，或编号小于3的图书，只能使用Q对象实现
# list = BookInfo.books.filter(Q(bread__gt=20) | Q(pk__lt=3))
# Q对象前可以使用~操作符，表示非not
#
# 例：查询编号不等于3的图书
# list = BookInfo.books.filter(~Q(pk=3))
# 关联查询(类似join查询)
# 关联模型类名小写__属性名__运算符=值
# 如果没有没有“__运算符”部分，表示等于，结果和sql中的inner join相同
# 例：查询图书，要求图书中英雄的描述包含‘八’
# list = BookInfo.books.filter(heroinfo__hcontent__contains='八')
#
# 例：查询书名为“天龙八部”的所有英雄
# list = HeroInfo.objects.filter(hbook__btitle='天龙八部')
# 聚合查询
#
# 使用aggregate()过滤器调用聚合函数
# 聚合函数包括：Avg，Count，Max，Min，Sum，被定义在django.db.models中
# 例：查询图书的总阅读量
# from django.db.models import Sum
# ...
# list = BookInfo.books.aggregate(Sum('bread'))
#
# 使用count时一般不使用aggregate()过滤器
# 例：查询图书总数
# list = BookInfo.books.count()
# 关联对象
#
# 在定义模型类时，可以指定三种关联关系，最常用的是一对多关系，如本例中的“图书-英雄”就为一对多关系，接下来进入shell练习关系的查询
# python manage.py shell
# 查询编号为1的图书
# book=BookInfo.books.get(pk=1)
# 获得book图书的所有英雄
# book.heroinfo_set.all()
# 获得编号为1的英雄
# hero=HeroInfo.objects.get(pk=1)
# 获得hero英雄出自的图书
# hero.hbook
