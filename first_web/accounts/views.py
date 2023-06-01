from django.shortcuts import render,redirect,reverse
from.forms import UserRegisterForm,UserLoginForm
from django.contrib.auth.models import User
from .forms import*
from .models import Profile
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from random import randint
from django.contrib.auth.forms import PasswordChangeForm      
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from django.views import View
from django.utils.encoding import force_str,force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode 
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.contrib.sites.shortcuts import get_current_site
from six import text_type
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
# Create your views here.
class EmailToken(PasswordResetTokenGenerator):
    def _make_hash_value(self,user,timestamp):
        return (text_type(user.is_active) + text_type(user.id) + text_type(timestamp))

email_generator = EmailToken()

def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(username = data['user_name'],
                                            email= data['email'],
                                            first_name = data['first_name'],
                                            last_name = data['last_name'],
                                            password = data['password_2'])
            user.is_acive = False 
            user.save()
            domain = get_current_site(request).domain
            uidb64 = urlsafe_base64_encode(force_bytes(user.id))
            url = reverse('accounts:active',kwargs = {'uidb64':uidb64,'token':email_generator.make_token(user)})
            link = 'http://' + domain + url 
            email = EmailMessage (
                'active user', link ,'test', [data['email']]
                )
            email.send(fail_silently = False )
            messages.error(request,'for verify click the link in your email')
            return redirect('home:home')
    else:
        form = UserRegisterForm()
    context = {'form':form}
    return render(request,'accounts/register.html',context)



class RegisterEmail(View):
    def get(self,request,uidb64,token):
        id = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(id = id) 
        if user and email_generator.check_token(user, token):
            user.is_active = True 
            user.save()
            return redirect ('account:login')



def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            data= form.cleaned_data
            try :
                user = authenticate (request,username = User.objects.get(email = data['user']), password= data['password'])
            except:
                user = authenticate (request,username = data['user'], password= data['password'])
                # User is authenticated
            if user is not None:
                login(request,user)
                messages.success(request,"welcome",'primary')
                return redirect('home:home')
            else:
                messages.error(request,"user or password is wrong",'danger')
    else:
        form = UserLoginForm()
        return render (request,'accounts/Login.html',{'form': form})
    return render(request,'accounts/Login.html',{'form':form})

def user_logout(request):
    logout(request)
    messages.success(request,'you have logged out','success')
    return redirect('home:home')
    
    
@login_required(login_url ='accounts:login')
def user_profile(request):
    profile = Profile.objects.get(user_id = request.user.id)
    return render(request,'accounts/profile.html',{'profile':profile})

@login_required(login_url ='accounts:login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST,instance = request.user)
        profile_form = ProfileUpdateForm(request.POST,instance = request.user.profile)
        if user_form and profile_form .is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request,'updated successfulli','success')
            return redirect('accounts:profile')
    else:
        user_form = UserUpdateForm(instance = request.user)
        profile_form = ProfileUpdateForm(instance = request.user.profile)
        context = {'user_form':user_form,'profile_form':profile_form}
    
    return render(request,'accounts/update.html',context)
def phone(request):
    if request.method == 'POST':
        form = PhoneForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            phone = f"0{data['phone']}"
            global random_code,Phone
            random_code = randint(100,1000)
            sms = ghasedak.Ghasedak("94d252ddebface4dd9b19cf885817595a2e415f447341f0d3703f17f1af8b533")
            sms.send({ 
                        'message': random_code,  
                        'receptor' : phone, 
                        'linenumber': "10008566"
            })
    else:
        form = PhoneForm()
    return render(request,'accounts/phone.html',{'form':form})

def verify(request):
    if request.method == 'POST':
        form = CodeForm(request.POST)
        if form.is_valid():
            if random_code == form.cleaned_data['code']:
                Profile = Profile.objects.get(phone = phone)
                user = User.objects.get(profile__id = profile_id)
                login(request,user)
                messages.success(request,'hi user','success')
                return redirect('home:home')
            else:
                messages.error(request,'wrong code')

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user,request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            messages.success(request,'password changed','success')
            return redirect(request,'accounts:profile')
        else:
            messages.error(request,'wrong','danger')
            return redirect(request,'accounts:change')
    else:
        form = PasswordChangeForm(request.user)       
    return render(request,'accounts/change.html',{'form':form})     


class ResetPassword(auth_views.PasswordResetView):
    template_name = 'accounts/reset.html'
    success_url = reverse_lazy('accounts:reset_done')
    email_template_name = 'accounts/link.html'
    
class DonePassword(auth_views.PasswordResetDoneView):
    template_name='accounts/done.html'
class ConfirmPassword(auth_views.PasswordResetConfirmView):
    template_name = 'accounts/confirm.html'
    success_url = reverse_lazy('accounts:complete')
class Complete(auth_views.PasswordResetCompleteView):
    template_name = 'accounts/complete.html'
    