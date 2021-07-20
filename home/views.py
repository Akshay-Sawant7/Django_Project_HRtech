from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Contact
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')
    # return HttpResponse("this is homepage")

def about(request):
    return render(request, 'about.html') 

def services(request):
    return render(request, 'services.html')
 

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')





def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account created sucessfully')
            fm.save()

    else:
        fm = SignUpForm()
    return render(request,'signup.html', {'form': fm})