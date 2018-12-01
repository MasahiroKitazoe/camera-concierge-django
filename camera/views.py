from django.shortcuts import render

def top_page(request):
  return render(request, 'camera/top_page.html', {})

def search(request):
  return render(request, 'camera/search.html', {})
