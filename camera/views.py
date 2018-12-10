from django.shortcuts import render

from .forms import SearchForm
from .services import CameraSearcher

def top_page(request):
  return render(request, 'camera/top_page.html', {})

def search(request):
  if len(request.GET) == 0:
    form = SearchForm()
    return render(request, 'camera/search.html', {"form": form})

  form = SearchForm(request.GET)
  form.is_valid()  # エラーは起きない想定

  cameras = CameraSearcher.filter(form.cleaned_data)
  return render(request, 'camera/search.html', {"form": form, "cameras": cameras})
