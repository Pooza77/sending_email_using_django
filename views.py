from django.shortcuts import render
from django.core.mail import EmailMessage, get_connection
from django.conf import settings
# Sample code to send an email
from django.core.mail import send_mail

def home(request):
    send_mail(
    "hello",
    "Dummy.",
    "poozasunuwar777@gmail.com",
    ["pujasunuwar777@gmail.com"],
    fail_silently=False,
)
    return render(request, 'home.html')