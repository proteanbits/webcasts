from django import forms

from course.models import CourseClass, Course


class CourseClassForm(forms.ModelForm):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    to_field_name='slug',
                                    widget=forms.Select(attrs={
                                        'class': "form-control"}))

    class Meta:
        model = CourseClass
        fields = ['title', 'is_free', 'short_desc', 'desc', 'course']

    def __init__(self, user, *args, **kwargs):
        super(CourseClassForm, self).__init__(*args, **kwargs)
        self.fields['course'].queryset = user.courses.all()
