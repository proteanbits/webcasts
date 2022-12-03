from django.urls import path

from .views import (CreateCourse, CourseDetail, DeleteCourse, ListCourses,
                    UpdateCourse)
from .views import (CreateClass, ClassDetail, DeleteClass, UpdateClass)

app_name = 'course'

urlpatterns = [
    # Course
    path('courses/', ListCourses.as_view(), name='course_list'),
    path('course/create/', CreateCourse.as_view(), name='create_course'),
    path('course/<slug:slug>/update/', UpdateCourse.as_view(),
         name='update_course'),
    path('course/<slug:slug>/delete/', DeleteCourse.as_view(),
         name='delete_course'),
    path('course/<slug:slug>/', CourseDetail.as_view(),
         name='course_detail'),

    # Class
    path('course/<slug:course_slug>/class/create/',
         CreateClass.as_view(),
         name='create_class'),
    path('class/<slug:slug>/update/', UpdateClass.as_view(),
         name='update_class'),
    path('class/<slug:slug>/delete/', DeleteClass.as_view(),
         name='delete_class'),
    path('class/<slug:slug>/', ClassDetail.as_view(),
         name='class_detail'),
]
