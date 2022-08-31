from django.shortcuts import render
import random
import string

def home(request):
    return render(request, 'generator/home.html')

def password(request):
    thepassword = ''
    length = int(request.GET.get("length", 12))
    chars = list(string.ascii_lowercase)
    if request.GET.get("uppercase"):
        chars.extend(list(string.ascii_uppercase))
    if request.GET.get("special"):
        chars.extend(list(string.punctuation))
    if request.GET.get("numbers"):
        chars.extend(list(string.digits))
    for i in range(length):
        thepassword += random.choice(chars)
    return render(request, 'generator/password.html', {'password':thepassword})

def about(request):
    return render(request, 'generator/about.html')

# Create your views here.
