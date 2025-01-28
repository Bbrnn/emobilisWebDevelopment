from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm, UserRegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.conf import settings


# Create your views here.
#User registration and login views
def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            # Get form data
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']

            # Additional validation
            if password != confirm_password:
                messages.error(request, "Passwords don't match")
                return render(request, 'registration/register.html', {'form': form})

            # Check if username or email already exists
            if User.objects.filter(username=username).exists():
                messages.error(request, "Username already exists")
                return render(request, 'registration/register.html', {'form': form})
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already exists")
                return render(request, 'registration/register.html', {'form': form})

            # Create new user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()

            # Log the user in after registration
           # login(request, user)

            messages.success(request, "Registration successful. You can now log in!")
            return redirect('login')  # Redirect to login after successful registration
        else:
            # If the form is not valid, show error messages
            messages.error(request, "There were errors in your form.")
            return render(request, 'registration/register.html', {'form': form})

    else:
        form = UserRegistrationForm()

    return render(request, 'registration/register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "You have logged in successfully!")
            return redirect('product_list')  # Redirect to the product list page after successful login
        else:
            messages.error(request, "Invalid username or password. Please try again.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def product_list(request):
    return render(request, 'product_list.html')


def contact_success(request):
    return render(request, 'contact_success.html')

"""
#view to handle ContactForm submissions
def contact_view(request):
    if request.method == "POST":
        # Bind the POST data to the form
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Send an email notification
            subject = form.cleaned_data['subject']
            message = f"Message from {form.cleaned_data['name']} ({form.cleaned_data['email']}):\n\n{form.cleaned_data['message']}"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],  # Send to admin email
                fail_silently=False,
            )

            # Success message
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')  # Redirect to the contact page after successful submission

        else:
            # Form validation error
            messages.error(request, "There was an error in your form. Please correct it and try again.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

"""

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

            # Send an email notification to the admin
            subject = form.cleaned_data['subject']
            message = f"Message from {form.cleaned_data['name']} ({form.cleaned_data['email']}):\n\n{form.cleaned_data['message']}"
            send_mail(
                subject,
                message,
                settings.EMAIL_HOST_USER,
                [settings.EMAIL_HOST_USER],  # You can add other recipient emails here if needed
                fail_silently=False,
            )

            # Show success message
            messages.success(request, "Your message has been sent successfully!")

            # Redirect to the same page or another page after successful submission
            return redirect('contact')  # Make sure this is your correct URL name
        else:
            # Form validation errors
            messages.error(request, "There was an error in your form. Please correct it and try again.")
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})