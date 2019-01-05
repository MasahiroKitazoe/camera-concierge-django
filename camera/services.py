from .models import Camera
from ranking.models import Rank


class CameraSearcher:
    def __init__(self, rank_id=None):
        self.rank_id = rank_id

    def filter_cameras_by_ranking(self):
        """
        引数rank_idで与えられたidのrankが指定する条件に合った
        cameraを抜き出して辞書型のデータをを要素とする配列にして返す
        """
        cameras = Camera.map_cameras()
        ranks = Rank.map_ranks()

        rank = ranks[self.rank_id]

        results = []

        for cam_id, camera_specs in cameras.items():
            match_flag = True  # 検索結果を表すフラグ

            # スペック条件を一つずつフィルタしていく
            for spec, val in camera_specs.items():
                # スペック以外の情報の時はスキップ
                if spec in ["name", "target_keyword"]:
                    continue

                if match_flag is False:
                    break

                # min, maxがないタイプの要素（four_kとか）
                if not isinstance(val, dict):
                    if not val == rank[spec]:
                        match_flag = False
                        continue

                # minだけ、maxだけがあるタイプ(min_isoとか)
                if "min" in spec and rank[spec] >= val:
                    match_flag = False
                    continue
                if "max" in spec and rank[spec] <= val:
                    match_flag = False
                    continue

                # min&maxがあるタイプの要素(priceとか)
                if not rank[spec]["min"] <= val <= rank[spec]["max"]:
                    match_flag = False

            # マッチしない条件があったら、次の機種のcamera_specsに回る
            if match_flag is False:
                continue

            # match_flagがTrueのままだったら、resultsに加える
            results.append(camera_specs)

        return results

    @classmethod
    def filter(cls, criteria_dict):
        """
        引数criteria_dictに格納されたcameraの検索条件を元に、
        該当のcameraを抜き出して配列で返す。
        """
        cameras = Camera.map_cameras()

        results = []

        for cam_id, camera_specs in cameras.items():
            match_flag = True  # 検索結果を表すフラグ

            for spec, val in camera_specs.items():
                # nameは部分一致でフィルタする
                if (spec == "name") and (criteria_dict.get("name", None) is not None):
                    if criteria_dict["name"] not in val:
                        match_flag = False
                        break
                    continue  # 一致していたら、次の検索条件へ

                # フィールド名にmin, maxが入っているfocus(焦点距離)については先に処理する
                if "focus" in spec and criteria_dict.get(spec, None) is not None:
                    if spec == "min_focus" and criteria_dict[spec] > val:
                        match_flag = False
                        break
                    if spec == "max_focus" and criteria_dict[spec] < val:
                        match_flag = False
                        break
                    continue  # 一致していたら、次の検索条件へ

                # min, maxで絞る条件でない場合（cameraのbooleanの属性値を想定）
                criteria_val = criteria_dict.get(spec, None)
                if criteria_val is not None and len(str(criteria_val)) != 0:
                    if val != criteria_val:
                        match_flag = False
                        break

                min_key = "min_" + spec
                max_key = "max_" + spec

                min_value = criteria_dict.get(min_key, None)
                max_value = criteria_dict.get(max_key, None)

                # 最小値でフィルタ
                if min_value:
                    if val < min_value:
                        match_flag = False
                        break

                # 最大値でフィルタ
                if max_value:
                    if val > max_value:
                        match_flag = False
                        break

            if match_flag is False:
                continue

            results.append(camera_specs)

        # レビュー数降順でカメラをソート
        results = sorted(results, key=lambda camera: camera["review_count"], reverse=True)
        return results