from django.shortcuts import render,redirect
from user_accounts.forms import Register_form,user_change_form
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.http import HttpResponse
# Create your views here.
# email send setup starts here -------------------------
from django.core.mail import EmailMessage,EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.contrib.sites.shortcuts import get_current_site
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.models import User

def send_transaction_email(user, amount, subject, template):
        message = render_to_string(template, {
            'user' : user,
            'amount' : amount,
        })
        send_email = EmailMultiAlternatives(subject, '', to=[user.email])
        send_email.attach_alternative(message, "text/html")
        send_email.send()

# email send setup ends here ---------------------------------
        
# activating user related funcion starts here -------------------------------
def activate(request, uid64, token):
    try:
        uid = urlsafe_base64_decode(uid64).decode()
        user = User._default_manager.get(pk=uid)
    except(user.DoesNotExist):
        user = None 
    
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        return render(request, 'confirmation_page.html', {'message': 'You have successfully confirmed your email. Log in now.'})
        return redirect('loginpage')
    else:
        return redirect('signup')
    

# activating user related funcion ends  here -------------------------------

# singup related stars here 
def signup(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = Register_form(request.POST)
            if form.is_valid():
                messages.success(request,"Welcome to our website")
                new_user=form.save()
                new_user.is_active=False
                new_user.save
                
                token = default_token_generator.make_token(new_user)
                print("token ", token)
                uid = urlsafe_base64_encode(force_bytes(new_user.pk))
                print("uid ", uid)
                current_site = get_current_site(request)
                confirm_link = f'http://{current_site.domain}/user/activate/{uid}/{token}'
                email_subject = "Confirm Your Email"
                email_body = render_to_string('confirm_email.html', {'confirm_link' : confirm_link})
                email = EmailMultiAlternatives(email_subject , '', to=[new_user.email])
                email.attach_alternative(email_body, "text/html")
                email.send()
                
                return redirect("loginpage")
        else : 
            form = Register_form(request.POST)
        return render(request,"./signup.html",{'form':form})
    else : 
       
        return redirect("signup")


# signup related form ends here 

# login related form 
def User_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request,data=request.POST)
            if form.is_valid():
                name = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=name,password=password) #checking user in the database or not
                if user is not None:
                    login(request,user)
                    return redirect("profilepage")
        else :
            form = AuthenticationForm()
        return render(request,"./login.html",{'form':form})
    else:
        return redirect("signup")
        
def profile(request):
    if request.user.is_authenticated:
        return render(request,"./profile.html",{'user':request.user}) 
    else :
        return redirect("loginpage")
    


    
def update_profile(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = user_change_form(request.POST,instance=request.user)
            if form.is_valid():
                messages.success(request,"Account Updated Suceessfully")
                form.save()
                return redirect("profilepage")
        else: 
            form = user_change_form(instance=request.user)
        return render(request,"./update_profile.html",{'form':form})
    else : 
        return redirect("singup")
    
# user logout area 

def user_logout(request):
    logout(request)
    return redirect("loginpage")

def change_pass(request):
    if request.method == "POST":
        form = PasswordChangeForm(user =request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            # form.cleaned_data['user']
            return redirect("singup")
    else : 
        form = PasswordChangeForm(user = request.user)
        return render(request,"./passchangeform.html",{'form':form})
    
# change password without old password

    
def change_pass2(request):
    if request.method == "POST":
        form = SetPasswordForm(user =request.user,data=request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            # form.cleaned_data['user']
            return redirect("profilepage")
    else : 
        form = SetPasswordForm(user = request.user)
    return render(request,"./passchangeform.html",{'form':form})








    




    




