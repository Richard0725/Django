from django.contrib import admin
from myApp2 import models
# Register your models here.
class MyAdmin(admin.ModelAdmin):
    list_display = ["title","detail","imgs"]
admin.site.register(models.bookdetails)