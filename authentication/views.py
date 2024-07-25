from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
from django.utils.html import strip_tags
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .custom_email_backend import CustomEmailBackend

from project_tracker import settings
from .tokens import generate_token
# Create your views here.
def home(request):
    return render(request, "authentication/index.html")

def signup(request):
    if request.method == "POST":
    # Retrieve form data
        email = request.POST["email"]
        fname = request.POST["fname"]
        lname = request.POST["lname"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # Validate email
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered!")
            return redirect('signup')

        # Validate password match
        if pass1 != pass2:
            messages.error(request, "Passwords do not match!")
            return redirect('signup')

        # Create user object
        myuser = User.objects.create_user(username = email, email = email, password = pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False # Disable account until email confirmation
        myuser.save()

        # Welcome Email
        welcome_subject = "Welcome to ProjectTracker - Login!!"
        welcome_message = "Hello " + myuser.first_name + "!! \n" + "Welcome to ProjectTracker. \nThank you for visiting our website. \n"+"We have also sent you a confirmation email, please confirm your email address. \n\n"+"Thanking You\n"+"Daniil"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(
            subject = welcome_subject, 
            message = welcome_message, 
            from_email = from_email, 
            recipient_list = to_list, 
            fail_silently=True,
            connection = CustomEmailBackend(),
        )
        
        # Email Address Confirmation Email with HTML template
        current_site = get_current_site(request)
        confirmation_subject = "Confirm your Email @ ProjectTracker - Django Login!!"
        uid = urlsafe_base64_encode(force_bytes(myuser.pk))
        token = generate_token.make_token(myuser) 
        confirmation_url = f"http://{current_site.domain}{reverse('activate', kwargs={'uidb64': uid, 'token': token})}"
        confirmation_message = render_to_string('email_confirmation.html',{     
            'name': myuser.first_name,
            'confirmation_url': confirmation_url
        })
        plain_message = strip_tags(confirmation_message)
        send_mail(
            subject = confirmation_subject,
            message = plain_message,
            html_message = confirmation_message,
            from_email = from_email,
            recipient_list = to_list,
            fail_silently = True,
            connection = CustomEmailBackend(),
        )
        return redirect('signin')
    
    return render(request, "authentication/signup.html")

def activate(request,uidb64,token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        myuser = User.objects.get(pk=uid)
    except (TypeError,ValueError,OverflowError,User.DoesNotExist):
        myuser = None

    if myuser is not None and generate_token.check_token(myuser,token):
        myuser.is_active = True
        # user.profile.signup_confirmation = True
        myuser.save()
        login(request,myuser)
        messages.success(request, "Your Account has been activated!!")
        return redirect('signin')
    else:
        return render(request,'activation_failed.html')
    
def signin(request):
    if request.method == "POST":
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        user = authenticate(email=email, password=pass1)
        if user is not None:
            login(request, user)
            email = user.email
            return render(request,"authentication/index.html", {'email' : email})

        else:
            messages.error(request, "Bad Credentials!")
            return redirect("signin")
    return render(request, "authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged out successfully!")
    return redirect("home")
