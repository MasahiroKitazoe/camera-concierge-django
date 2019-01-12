from .models import Camera
from ranking.models import Rank


class CameraSearcher:
    def __init__(self, rank_id=None, sort_type="review"):
        self.rank_id = rank_id
        self.sort_type = sort_type

    def filter_cameras_by_ranking(self):
        """
        引数rank_idで与えられたidのrankが指定する条件に合った
        cameraを抜き出して辞書型のデータをを要素とする配列にして返す
        """
        rank_criteria = Rank.objects.get(pk=self.rank_id).map_rank()
        return self.filter(rank_criteria)

    def sort_filter_results(self, results):
        sort_type = self.sort_type + "_count"
        return sorted(results, key=lambda camera: camera[sort_type], reverse=True)

    def filter(self, criteria_dict):
        """
        引数criteria_dictに格納されたcameraの検索条件を元に、
        該当のcameraを抜き出して配列で返す。
        """
        cameras = Camera.map_cameras()

        results = []

        for cam_id, camera_specs in cameras.items():
            match_flag = True  # 検索結果を表すフラグ

            for spec_name, spec_val in camera_specs.items():
                # nameは部分一致でフィルタする
                if (spec_name == "name") and (criteria_dict.get("name", None) is not None):
                    if criteria_dict["name"] not in spec_val:
                        match_flag = False
                        break
                    continue  # 一致していたら、次の検索条件へ

                # フィールド名にmin, maxが入っているfocus(焦点距離)については先に処理する
                if "focus" in spec_name and criteria_dict.get(spec_name, None) is not None:
                    if spec_name == "min_focus" and criteria_dict[spec_name] > spec_val:
                        match_flag = False
                        break
                    if spec_name == "max_focus" and criteria_dict[spec_name] < spec_val:
                        match_flag = False
                        break
                    continue  # 一致していたら、次の検索条件へ

                # min, maxで絞る条件でない場合（cameraのbooleanの属性値を想定）
                criteria_val = criteria_dict.get(spec_name, None)
                if criteria_val is not None and len(str(criteria_val)) != 0:
                    if spec_val != criteria_val:
                        match_flag = False
                        break

                min_key = "min_" + spec_name
                max_key = "max_" + spec_name

                min_value = criteria_dict.get(min_key, None)
                max_value = criteria_dict.get(max_key, None)

                # 最小値でフィルタ
                if min_value:
                    if spec_val < min_value:
                        match_flag = False
                        break

                # 最大値でフィルタ
                if max_value:
                    if spec_val > max_value:
                        match_flag = False
                        break

            if match_flag is False:
                continue

            results.append(camera_specs)

        # レビュー数降順でカメラをソート
        return self.sort_filter_results(results)
