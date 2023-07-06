from django.shortcuts import render,HttpResponse
from firstapp.models import Contact
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'start.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def contact(request):
    if request.method == "POST":
        firstName = request.POST.get('FirstName')
        lastName = request.POST.get('LastName')
        username = request.POST.get('username')
        email = request.POST.get('Email')
        reason = request.POST.get('Reason')
        contact = Contact(FirstName=firstName,LastName=lastName,Username=username,Email=email,reason=reason)
        contact.save()
        messages.success(request, "Your Message has been sent successfully.")
    return render(request, 'contact.html')