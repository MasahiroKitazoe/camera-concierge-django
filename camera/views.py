from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator

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

    search_results = CameraSearcher.filter(form.cleaned_data)
    paginator = Paginator(search_results, 10)
    page = request.GET.get("page")
    cameras = paginator.get_page(page)
    return render(request, 'camera/search.html', {"form": form, "cameras": cameras})


def detail(request, camera_id):
    camera = get_object_or_404(Camera.objects.select_related("camera_type", "finder", "frame"), pk=camera_id)
    reviews = camera.review_set.all()
    print(len(reviews))
    return render(request, "camera/detail.html", {"camera": camera, "reviews": reviews})
