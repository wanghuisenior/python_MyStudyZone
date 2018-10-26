from django.test import TestCase

# Create your tests here.

import keyword

from faker import Faker

print(keyword.iskeyword('if'))

# bar()被装饰了

dic_data = {'a': 1, 'b': 2}
print('a' in dic_data)
print('2' in dic_data)
print('b' in dic_data.keys())
print('1' in dic_data.keys())
fake = Faker('zh_CN')
print(fake.address())
print(fake.name())
print(fake.city())
print('  aa a  '.strip())