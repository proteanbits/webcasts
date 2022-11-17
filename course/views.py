from django.shortcuts import render

from .models import Course, CourseClass


# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {
        'title': 'List of Courses',
        'courses': courses
    }

    return render(request, 'pages/course/list.html', context)


def course_detail(request, slug):
    course = Course.objects.get(slug__exact=slug)

    context = {
        'course': course
    }

    return render(request, 'pages/course/detail.html', context)


def class_detail(request, slug):
    course_class = CourseClass.objects.get(slug__exact=slug)

    context = {
        'class': course_class
    }

    return render(request, 'pages/class/detail.html', context)