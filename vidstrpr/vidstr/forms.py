from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Posts, Profile, Comment, Message

class RegisterUser(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.TextInput(attrs={"class":"form-control", "placeholder":"Email Address"}))
    first_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "First Name"}))
    last_name = forms.CharField(label="",max_length=100, widget=forms.TextInput(attrs={"class":"form-control", "placeholder": "Last Name"}))

    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterUser, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'User Name'
        self.fields['username'].label = ''
        self.fields['username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password1'].label = ''
        self.fields['password1'].help_text = '<ul class="form-text text-muted small"><li>Your password can\'t be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can\'t be a commonly used password.</li><li>Your password can\'t be entirely numeric.</li></ul>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields['password2'].label = ''
        self.fields['password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class PostForm(forms.ModelForm):
    body = forms.TextInput()
    images = forms.ImageField(required=False)

    class Meta:
        model = Posts
        fields = ("body", "images")
        exclude = ("user",)
    
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)

        self.fields['body'].widget.attrs['class'] = 'form-control'
        self.fields['body'].widget.attrs['placeholder'] = 'Enter the Main Post'
        self.fields['body'].label = ''

        self.fields['images'].widget.attrs['class'] = 'form-control'
        self.fields['images'].label = ''


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ("user", "follows")

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        self.fields['profile_image'].widget.attrs['class'] = 'form-control'
        self.fields['profile_image'].label = ''


class CommentForm(forms.ModelForm):
    body = forms.TextInput()

    class Meta:
        model = Comment
        fields = ("body",)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)

        self.fields['body'].widget.attrs['class'] = 'form-control'
        self.fields['body'].widget.attrs['style'] = 'height: 2rem;'
        self.fields['body'].label = ''

class MessageForm(forms.ModelForm):
    message = forms.TextInput()

    class Meta:
        model = Message
        fields = ("message",)

    def __init__(self, *args, **kwargs):
        super(MessageForm, self).__init__(*args, **kwargs)

        self.fields['message'].widget.attrs['class'] = 'form-control'
        self.fields['message'].widget.attrs['style'] = 'height: 2rem;'
        self.fields['message'].widget.attrs['placeholder'] = 'Type Message'
        self.fields['message'].label = ''
