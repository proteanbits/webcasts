from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

from main.models import UserProfile


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2')
        error_messages = {
            'username': {
                'unique': "A user with this email already exists",
            }
        }

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
            UserProfile.objects.create(user=user)
        return user


class UserForm(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = ('username', )


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('dob', )


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)

    
