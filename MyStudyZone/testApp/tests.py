from django.test import TestCase


# Create your tests here.
class Cat(object):
	def __init__(self, **kwargs):
		print('带参数', kwargs)


for i in dir('abc'):
	print(i)
print('abc'.capitalize())