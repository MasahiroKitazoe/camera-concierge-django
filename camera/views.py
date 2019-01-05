from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods

from camera.models import Camera
from camera.forms import SearchForm
from camera.services import CameraSearcher


@require_http_methods(["GET"])
def top_page(request):
    return render(request, 'camera/top_page.html', {})


@require_http_methods(["GET"])
def search(request):
    if not request.GET:
        form = SearchForm()
        return render(request, 'camera/search.html', {"form": form})

    page = request.GET.get("page")
    # ページ指定の場合、formのパラメータは保存済みセッション変数から受け取る
    if page:
        form = SearchForm(request.session.get("form_data"))
    else:
        form = SearchForm(request.GET)
    form.is_valid()  # エラーは起きない想定
    request.session["form_data"] = form.cleaned_data

    search_results = CameraSearcher.filter(form.cleaned_data)
    paginator = Paginator(search_results, 10)
    cameras = paginator.get_page(page)
    return render(request, 'camera/search.html', {"form": form, "cameras": cameras})


@require_http_methods(["GET"])
def detail(request, camera_id):
    camera = get_object_or_404(Camera.objects.select_related("camera_type", "finder", "frame"), pk=camera_id)
    reviews = camera.review_set.all().order_by("id")

    paginator = Paginator(reviews, 10)
    page = request.GET.get("page")
    reviews = paginator.get_page(page)
    return render(request, "camera/detail.html", {"camera": camera, "reviews": reviews})
