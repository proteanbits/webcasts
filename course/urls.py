from django.urls import path

from .views import index, course_detail, class_detail

app_name = 'course'

urlpatterns = [
    path('', index, name='course_list'),
    path('<slug:slug>', course_detail, name='course_detail'),
    path('class/<slug:slug>', class_detail, name='class_detail'),
]
