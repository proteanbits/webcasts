from re import template

from django.db import IntegrityError
from django.urls import reverse
from django.utils.text import slugify
from django.views.generic import CreateView, DeleteView, UpdateView, ListView, DetailView

from .forms import CourseClassForm
from .models import Course, CourseClass


class CreateCourse(CreateView):
    model = Course
    template_name = 'pages/course/create.html'  # default is course_create_form.html
    fields = ['title', 'price', 'short_desc', 'desc', 'status']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super(CreateCourse, self).form_valid(form)
        form.instance.authors.add(self.request.user)
        return response

    def get_success_url(self):
        return reverse('course:course_list')


class UpdateCourse(UpdateView):
    model = Course
    template_name = 'pages/course/update.html'  # default is course_update_form.html
    fields = ['title', 'price', 'short_desc', 'desc', 'status']

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        response = super(UpdateCourse, self).form_valid(form)
        return response

    def get_success_url(self):
        return reverse('course:course_list')


class ListCourses(ListView):
    template_name = 'pages/course/list.html'
    model = Course

    def get_queryset(self):
        return self.request.user.courses.all()


class CourseDetail(DetailView):
    template_name = 'pages/course/detail.html'
    model = Course


# TODO, Implement this
class DeleteCourse(DeleteView):
    model = Course
    template_name = 'pages/course/delete.html'

    def get_success_url(self):
        return reverse('course:course_list')


class CreateClass(CreateView):
    model = CourseClass
    template_name = 'pages/class/create.html'  # default is class_create_form.html
    fields = ['title', 'is_free', 'short_desc', 'desc']

    def get_context_data(self, **kwargs):
        context = super(CreateClass, self).get_context_data(**kwargs)
        context['course'] = self.request.user.courses.filter(
            slug=self.kwargs.get('course_slug')).get()

        return context

    def form_valid(self, form):
        form.instance.course = self.request.user.courses.filter(
            slug=self.kwargs.get('course_slug')).get()
        form.instance.slug = slugify(" ".join([form.instance.course.title,
                                               form.instance.title]))
        try:
            response = super(CreateClass, self).form_valid(form)
        except IntegrityError as e:
            if 'UNIQUE' in str(e):
                form.add_error('title', "Title must be Unique for a Course")
                return self.form_invalid(form)
            raise e
        return response

    def get_success_url(self):
        return reverse('course:course_detail',
                       kwargs={'slug': self.object.course.slug})


class UpdateClass(UpdateView):
    model = CourseClass
    template_name = 'pages/class/update.html'  # default is class_update_form.html
    form_class = CourseClassForm

    def get_form_kwargs(self):
        kwargs = super(UpdateClass, self).get_form_kwargs()
        kwargs.update(user=self.request.user)
        return kwargs

    def get_initial(self):
        initial = super(UpdateClass, self).get_initial()
        initial['course'] = self.object.course
        return initial

    def form_valid(self, form):
        form.instance.slug = slugify(" ".join([form.instance.course.title,
                                               form.instance.title]))
        response = super(UpdateClass, self).form_valid(form)
        return response

    def get_success_url(self):
        return reverse('course:course_detail',
                       kwargs={'slug': self.object.course.slug})


class ClassDetail(DetailView):
    template_name = 'pages/class/detail.html'
    model = CourseClass


# TODO, Implement this
class DeleteClass(DeleteView):
    pass
