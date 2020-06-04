from django.shortcuts import render
from django.http import HttpResponse
import random

alphabets_lower = 'abcdefghijklmnopqrstuvwxyz'
numbers = '1234567890'
special_Characters = '!@#$%^&*(){[]:?></\|"".,;:`~`'

# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    
    thepassword=generate_Password(request)
    
    return render(request, 'generator/password.html', {'password': thepassword})

def generate_Password(request):
    thepassword=''
    
    length=int(request.GET.get('length'))

    characters = list(alphabets_lower)

    if request.GET.get('Uppercase'):
        characters = characters + list(alphabets_lower.upper())
        thepassword+=random.choice(list(alphabets_lower.upper()))
        length-=1

    if request.GET.get('Numbers'):
        characters = characters + list(numbers)
        thepassword+=random.choice(list(numbers))
        length-=1
    
    if  request.GET.get('Special Characters'):
        characters = characters + list(special_Characters)
        thepassword+=random.choice(list(special_Characters))
        length-=1
    
    for _ in range(length):
        thepassword+=random.choice(characters)
    
    return thepassword

def check(lst,thepassword):
    for _ in lst:
        if _ in thepassword:
            return True


