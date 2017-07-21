from django.test import TestCase
from alarmsg import models

# Create your tests here.
bool_data=models.TbDataaqubool.objects.get(locid__exact=35)
# print(3/5)