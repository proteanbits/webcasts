from django.db.models import Q
from django.http import Http404

from course.models import CourseClass, Course


def published_course(function):
    def wrap(request, *args, **kwargs):
        try:
            Course.objects.get(Q(slug=kwargs['slug']) & Q(status="PUB"))
            return function(request, *args, **kwargs)
        except Course.DoesNotExist:
            raise Http404

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
