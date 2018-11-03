from django.http import HttpResponse
from django.shortcuts import render

def top_page(request):
  return render(request, 'search/top_page.html', {})

def index(request):
  return render(request, 'search/index.html', {})
