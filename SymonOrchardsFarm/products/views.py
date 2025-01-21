from django.shortcuts import render,redirect
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

# Create your views here.
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


#view to handle ContactForm submissions
def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            form.save()

           # send an email notification
            subject = form.cleaned_data['subject']
            message = f"Message from {form.cleaned_data['name']} ({form.cleaned_data['email']}):\n\n ({form.cleaned_data['message']})"
            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                [settings.CONTACT_EMAIL],
            )
            return redirect('contact_success')
        else:
            form = ContactForm()
            return render(request, 'contact.html', {'form': form})







