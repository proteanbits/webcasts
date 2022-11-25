from re import template

from django.shortcuts import render
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import CreateView

from .models import Course, CourseClass


# Create your views here.

def index(request):
    courses = Course.objects.all()
    context = {
        'title': 'List of Courses',
        'courses': courses
    }

    return render(request, 'pages/course/list.html', context)


class CreateCourse(CreateView):
    model = Course
    template_name = 'pages/course/create.html'
    fields = ['title', 'price', 'short_desc', 'desc', 'status']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super(CreateCourse, self).form_valid(form)
        form.instance.authors.add(self.request.user)
        return response

    def get_success_url(self):
        return reverse('course:course_list')


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