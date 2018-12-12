from .models import Camera
from ranking.models import Rank

# rank.verbose_name -> 絞り込み対象のCameraのフィールド名


class CameraSearcher:
    def filter_cameras_by_ranking(self, rank_id):
        rank = Rank.objects.get(pk=rank_id)
        rank_dict = rank.__dict__

        # 絞り込み条件のないフィールドを弾く
        criteria_dict = {}
        for key, val in criteria_dict.items():
          if val == 0 or val is None:
            continue
          criteria_dict[key] = val

        for key, val in criteria_dict.items():
        pass

    def filter_cameras_by_users(self):
        pass
