from django.db import models
from django.utils.encoding import python_2_unicode_compatible

import datetime
from django.utils import timezone

# class Customer(models.Model):
#     field1 = models.CharField(max_length=200)
#     field2 = models.CharField(max_length=200)
#     field3 = models.CharField(max_length=200)
#     field4 = models.CharField(max_length=200)
#     field5 = models.CharField(max_length=200)
#     def __str__(self):
#         return self.field1

class Spec(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=200,verbose_name="規格說明")
    field3 = models.CharField(max_length=200,null=True)
    # field4 = models.CharField(max_length=200)
    # field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field2
class Cust(models.Model):
    field1 = models.IntegerField()
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200,null=True)
    # field4 = models.CharField(max_length=200)
    # field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field2


class Item000(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200)
    field4 = models.CharField(max_length=200)
    field5 = models.CharField(max_length=200)
    field6 = models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.field1

class Item001(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200)
    field4 = models.CharField(max_length=200)
    field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field1
# 客戶	品名	欠料量	欠備庫量	客訴量	模具壽命?%	客戶	品名	欠料量	欠備庫量	客訴量	模具壽命?%																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																				

class Item002(models.Model):
    field1 = models.CharField(max_length=200,verbose_name="編號")
    field2 = models.CharField(max_length=200,verbose_name="客戶")
    field3 = models.CharField(max_length=200,verbose_name="品名")
    field4 = models.CharField(max_length=200,verbose_name="欠料量")
    field5 = models.CharField(max_length=200,verbose_name="欠備庫量")
    field6 = models.CharField(max_length=200,null=True,verbose_name="客訴量")
    field7 = models.CharField(max_length=200,null=True,verbose_name="模具壽命")
    def __str__(self):
        return self.field1
class Item003(models.Model):
    field1 = models.CharField(max_length=200)
    field2 = models.CharField(max_length=200)
    field3 = models.CharField(max_length=200)
    field4 = models.CharField(max_length=200)
    field5 = models.CharField(max_length=200)
    def __str__(self):
        return self.field1
class Item004(models.Model):
    field1 = models.CharField(max_length=200,verbose_name="編號")
    field2 = models.CharField(max_length=200,verbose_name="客戶")
    field3 = models.CharField(max_length=200,verbose_name="品名")
    field4 = models.CharField(max_length=200,verbose_name="欠料量")
    field5 = models.CharField(max_length=200,verbose_name="欠備庫量")
    field6 = models.CharField(max_length=200,null=True,verbose_name="客訴量")
    field7 = models.CharField(max_length=200,null=True,verbose_name="模具壽命")
    def __str__(self):
        return self.field1
