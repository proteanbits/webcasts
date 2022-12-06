import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View

from course.models import Course, CourseSubscription, CourseClass
from main.forms import ContactForm, NewUserForm

from .decorators import published_course


# Create your views here.
def home(request):
    context = {
        'title': 'Welcome to the best Django Tutorials'
    }
    return render(request, 'pages/home.html', context)


# Create your views here.
def about_us(request):
    context = {
        'title': 'About Us'
    }
    return render(request, 'pages/about_us.html', context)


def contact_us(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = ContactForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            sender = form.cleaned_data['sender']
            cc_myself = form.cleaned_data['cc_myself']

            print(subject, message, sender, cc_myself)

            return HttpResponseRedirect(reverse('main:thank_you_contact_us'))

    # if a GET (or any other method) we'll create a blank form
    else:
        form = ContactForm()

    return render(request, 'pages/contact_us.html', {'form': form})


def thank_you_contact_us(request):
    return render(request, 'pages/thank_you_contact_us.html')


class Register(View):
    """Create new User

    Creates a new user. Sends an welcome email to user and new user
    registered email to admin

    """

    # user = get_user_model()

    def get(self, request):
        """Show the initial UserCreationForm

        Args:
            request: HttpRequest

        Returns:
            object: HttpResponse
        """
        context = {
            'form': NewUserForm
        }
        return render(request, 'auth/register.html', context)

    def post(self, request):
        """Handles the POST UserCreationForm.

        Args:
            request: HttpRequest

        Returns:
            object: HttpResponse
        """
        # TODO send emails by handling user_created signal?
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

        context = {
            'form': form
        }
        return render(request, 'auth/register.html', context)


def courses(request):
    """Display a list of published courses

    :param request:
    :return:
    """
    context = {
        'courses': Course.published.all()
    }

    return render(request, 'pages/courses.html', context)


@published_course
def show_course(request, slug):
    """Display individual course

    :param request:
    :param slug:
    :return:
    """
    course = Course.objects.filter(slug=slug).get()
    context = {
        'course': course,
        'is_subscribed': course.has_subscription(request.user),
        'is_author': course.is_author(request.user)
    }

    return render(request, 'pages/course.html', context)


@login_required
def course_class(request, slug):
    """Display individual classes

    :param request:
    :param slug:
    :return:
    """

    course_cls = CourseClass.objects.filter(slug=slug).get()

    context = {
        'class': course_cls,
        'is_subscribed': course_cls.course.has_subscription(request.user),
        'is_author': course_cls.course.is_author(request.user)
    }
    return render(request, 'pages/class.html', context)


@login_required
def subscribe(request, slug):
    course = Course.objects.filter(slug=slug).get()

    course_subscription = CourseSubscription.objects.create(
        user=request.user, course=course, date_subscribed=datetime.datetime.now())
    course_subscription.save()

    return redirect(reverse('main:course',
                            kwargs={'slug': course.slug}))


@login_required
def profile(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'pages/profile.html', context)
