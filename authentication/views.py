from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.core.mail import EmailMessage, send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes, force_str
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
        myuser = User.objects.create_user(email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.is_active = False # Disable account until email confirmation
        myuser.save()

        # Welcome Email
        subject = "Welcome to ProjectTracker - Login!!"
        message = "Hello " + myuser.first_name + "!! \n" + "Welcome to ProjectTracker!! \nThank you for visiting our website\n. We have also sent you a confirmation email, please confirm your email address. \n\nThanking You\n Daniil"        
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, message, from_email, to_list, fail_silently=True)
        
        # Email Address Confirmation Email
        current_site = get_current_site(request)
        email_subject = "Confirm your Email @ ProjectTracker - Django Login!!"
        uid = urlsafe_base64_encode(force_bytes(myuser.pk))
        token = generate_token.make_token(myuser) 
        confirmation_url = f"http://{current_site.domain}{reverse('activate', kwargs={'uidb64': uid, 'token': token})}"
        message2 = render_to_string('email_confirmation.html',{     
            'name': myuser.first_name,
            'confirmation_url': confirmation_url
        })
        email = EmailMessage(
        email_subject,
        message2,
        settings.EMAIL_HOST_USER,
        [myuser.email],
        )
        email.connection = CustomEmailBackend()
        email.send(fail_silently=False)
        
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
