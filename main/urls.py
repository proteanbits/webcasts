from django.urls import path

from .views import home, about_us, contact_us, thank_you_contact_us, courses, show_course, course_class, subscribe, \
    profile

app_name = 'main'

urlpatterns = [
    path('', home, name='home'),
    path('about-us', about_us, name='about_us'),
    path('contact-us', contact_us, name='contact_us'),
    path('thank-you-contact-us', thank_you_contact_us, name='thank_you_contact_us'),
    path('courses/', courses, name='courses'),
    path('course/<slug:slug>', show_course,
         name='course'),
    path('class/<slug:slug>', course_class,
         name='class'),
    # Subscribe
    path('course/<slug:slug>/subscribe/',
         subscribe,
         name='subscribe'),

    # Profile
    path('profile/', profile, name='profile'),
]
