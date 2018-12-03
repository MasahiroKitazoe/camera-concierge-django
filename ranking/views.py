from django.shortcuts import render
from django.views import generic

from .models import Rank
from camera.services import CameraSearcher

class IndexView(generic.ListView):
  template_name = "ranking/index.html"
  context_object_name = "ranks"

  def get_queryset(self):
    return Rank.objects.all()


class DetailView(generic.DetailView):
  model = Rank
  template_name = "ranking/detail.html"

  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['og_image'] = "https://lh3.googleusercontent.com/W6HJ3Tl_wD1D3kc4p2HzrfkBLra4zREWvhrg6K-r6XD7aNm_0inDpoDKidoBaQkmwmbnmB3rTtJq4jUzVBa_86tTlCv7IXuSUWjxAt4aQdc7dqTgv9yA4pI-cdISK6quj16S1QIeoh-QwrBF_u4jyJC36AlZ4LEX3wOslawh4Fy_2BN5v0FaSobKWZR2Xe94W5q8s1sLCFCzThXozWTE7ZMO8cS8k2BcZVj3PVaB4r6jojog8f_s9mMC-LqJaQzgJy2DIbhDP7jFZ4_g45SvPc9PJ7O9OOEfamtgNgBRXPhTqE0fhCwLAoGyLUHU3FsxQMRtmPye1onm-sAqt6DrYOuX02q8hyB8jjr0lnFyNKEOoV00rrGB3F1QDJfh8-Jztj6E2KYth8ulJNjOgzc2hd4V-Fo1UDV50FKgzjIlyz2r5jkEpAsLy4up9Tqn5cg3dE2izvj2ISdhrFAfAaxqzkxkX6WRVVurNE6gkuvczX7K7m6Cn3kVi4PIQOM4LCG7OR9PNhHYz1R4eu-9HeXNqCC6CaytpHbZQsuYDtJ-NV_GG5VZe0vFNeL58E-UQT_1hZt6XYubK-Y3rsann_BhnLRpYBj7xIGgNiN9-HQB_xZlwY1BygTkPNv4mwf5D6LBBtHOCY_iko7NIJIG1V6r8EQrzg=w1043-h697-no"
        context['cameras'] = \
                  CameraSearcher().filter_cameras_by_ranking(context['rank'].id)
        return context
