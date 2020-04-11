from student import views
from django.conf.urls import include, url
from django.urls import path

urlpatterns = [
    path('create_stud', views.create_stud),
    path('', views.show_stud),
    path('show_stud', views.show_stud),
    path('update_stud/<int:id>', views.update_stud),
    path('delete_stud/<int:id>', views.delete_stud),
]
