from django.contrib import admin
# from djangoapp.models import Student
# Register your models here.
from djangoapp.models import Data

class myapp(admin.ModelAdmin):
    list_display = ('name','email','msg')
admin.site.register(Data,myapp)

# admin.site.register(Student)

