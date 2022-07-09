from django.shortcuts import render
from django.http import HttpResponse
def home(reques):
    return render(template_name='home.html')
# Create your views here.
