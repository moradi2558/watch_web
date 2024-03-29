from django import forms
from .models import *
from django.contrib.auth.models import*
from image_uploader_widget.widgets import ImageUploaderWidget


class UserRegisterForm(forms.Form):
    user_name = forms.CharField(max_length= 50,widget = forms.TextInput(attrs={'placeholder':'user name'}))
    email = forms.EmailField(max_length= 50,widget = forms.EmailInput(attrs={'placeholder':'email'}))
    first_name = forms.CharField(max_length=50,widget = forms.TextInput(attrs={'placeholder':'first name'}))
    last_name = forms.CharField(max_length=50,widget = forms.TextInput(attrs={'placeholder':'last name'}))
    password_1 = forms.CharField(max_length=50,widget = forms.PasswordInput(attrs={'placeholder':'password'}))
    password_2 = forms.CharField(max_length=50,widget = forms.PasswordInput(attrs={'placeholder':'repeat password'}))



    def clean_user_name(self):
        user = self.cleaned_data['user_name']
        if User.objects.filter(username = user).exists():
            raise forms.ValidationError("این اسم قبلا وارد شده است")
        return user 
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email = email).exists():
            raise forms.ValidationError('این ایمیل قبلا وارد شده است')
        return email
    def clean_password_2(self):
        password1 = self.cleaned_data['password_1']
        password2 = self.cleaned_data['password_2']
        if password1 != password2 :
            raise forms.ValidationError('پسووردها مشابه هم نیستند')
        elif (len(password2) < 8 ):
            raise forms.ValidationError('پسوورد کوتاه است حداقل باید شامل 8 کاراکتر باشد')
        elif not any(x.isupper()for x in password2):
            raise forms.ValidationError('حتما باید شامل یک حرف بزرگ باشد')
        return password2
class UserLoginForm(forms.Form):
    user = forms.CharField()
    password = forms.CharField()


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name']

class ProfileUpdateForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
   
        self.fields['profile_image'].widget.attrs['id'] = 'profile_image'
        # self.fields['profile_image'].widget = 'forms.FileInput'    
    profile_image = forms.ImageField(widget=forms.FileInput)        
    class Meta:
        model = Profile
        fields = ['phone','address','profile_image']
        
        
class PhoneForm(forms.Form):
    phone = forms.IntegerField()