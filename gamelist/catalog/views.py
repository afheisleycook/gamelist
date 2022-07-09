from django.shortcuts import render
from django.http import HttpResponse
def home():
    return render('home.html')
# Create your views here.
