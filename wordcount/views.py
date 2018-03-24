from django.http import HttpResponse
from django.shortcuts import render

def home(request):
  return render(request, 'home.html', {'Hithere':'This is a dict'})