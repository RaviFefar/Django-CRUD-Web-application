from django.contrib import admin
from student.models import Stud
from django.utils.html import format_html

class listAllStudent(admin.ModelAdmin):
    list_display = ('name','email','number','hobbies','gender','image_html','age')

    def image_html(self,obj):
        return format_html('<img src="/media/%s" width="100px">' % (obj.image))
    image_html.allow_tags = True

admin.site.register(Stud, listAllStudent)

# Register your models here.
