from django.shortcuts import render

def top_page(request):
  return render(request, 'search/top_page.html', {})

def search(request):
  return render(request, 'search/search.html', {})
