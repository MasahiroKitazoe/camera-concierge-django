from django.shortcuts import render, get_object_or_404

from camera.models import Camera
from camera.forms import SearchForm
from camera.services import CameraSearcher


def top_page(request):
    return render(request, 'camera/top_page.html', {})


def search(request):
    if not request.GET:
        form = SearchForm()
        return render(request, 'camera/search.html', {"form": form})

    form = SearchForm(request.GET)
    form.is_valid()  # エラーは起きない想定

    cameras = CameraSearcher.filter(form.cleaned_data)
    return render(request, 'camera/search.html', {"form": form, "cameras": cameras})


def detail(request, camera_id):
    camera = get_object_or_404(Camera, pk=camera_id)
    return render(request, "camera/detail.html", {"camera": camera})
