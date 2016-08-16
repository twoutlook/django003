from django.contrib import admin

# Register your models here.
# from .models import Customer
from .models import Item000
from .models import Item001
from .models import Item002
from .models import Item003
from .models import Item004
from .models import Spec

from django.contrib import admin
# admin.site.register(Customer)

class Item000Admin(admin.ModelAdmin):
    list_display=['field1','field2','field3','field4','field5','field6']
admin.site.register(Item000,Item000Admin)


class SpecAdmin(admin.ModelAdmin):
    list_display=['field1','field2']
admin.site.register(Spec,SpecAdmin)


# admin.site.register(Item000)


admin.site.register(Item001)
admin.site.register(Item002)
admin.site.register(Item003)
admin.site.register(Item004)
# admin.site.register(Spec)
