import pandas as pd

from django.db import models
from django.utils import timezone

from camera.models import CameraType, Finder, Frame, Maker
from ranking.utils import assign_item


class Rank(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    min_price = models.IntegerField("price", null=True)
    max_price = models.IntegerField("price", null=True)
    min_pixel = models.IntegerField("pixel", null=True)
    max_pixel = models.IntegerField("pixel", null=True)
    min_iso = models.IntegerField("iso", null=True)
    max_iso = models.IntegerField("iso", null=True)
    min_continuous_shooting_performance = \
                models.FloatField("continuous_shooting_performance", null=True)
    max_continuous_shooting_performance = \
                models.FloatField("continuous_shooting_performance", null=True)
    min_shutter_speed = \
                models.CharField("shutter_speed", max_length=50, null=True)
    max_shutter_speed = \
                models.CharField("shutter_speed", max_length=50, null=True)
    min_monitor_size = models.FloatField("monitor_size", null=True)
    max_monitor_size = models.FloatField("monitor_size", null=True)
    min_monitor_pixel = models.FloatField("monitor_pixel", null=True)
    max_monitor_pixel = models.FloatField("monitor_pixel", null=True)
    min_shooting_num = models.IntegerField("num_of_shooting", null=True)
    max_shooting_num = models.IntegerField("num_of_shooting", null=True)
    four_k = models.BooleanField("four_k", null=True)
    wifi = models.BooleanField("wifi", null=True)
    touch_panel = models.BooleanField("touch_panel", null=True)
    move_panel = models.BooleanField("move_panel", null=True)
    min_weight = models.FloatField("weight", null=True)
    max_weight = models.FloatField("weight", null=True)
    min_width = models.FloatField("width", null=True)
    max_width = models.FloatField("width", null=True)
    min_height = models.FloatField("height", null=True)
    max_height = models.FloatField("height", null=True)
    min_depth = models.FloatField("depth", null=True)
    max_depth = models.FloatField("depth", null=True)
    frame_id = models.IntegerField("frame_id", null=True)
    maker_id = models.IntegerField("maker_id", null=True)
    finder_id = models.IntegerField("finder_id", null=True)
    min_f_value_tele = models.FloatField("f_value", null=True)
    max_f_value_tele = models.FloatField("f_value", null=True)
    min_shooting_num_with_finder = \
                models.IntegerField("num_of_shooting_with_finder", null=True)
    max_shooting_num_with_finder = \
                models.IntegerField("num_of_shooting_with_finder", null=True)
    bluetooth = models.BooleanField("bluetooth", null=True)
    min_zoom = models.FloatField("zoom", null=True)
    max_zoom = models.FloatField("zoom", null=True)
    min_focus = models.IntegerField("min_focus", null=True)
    max_focus = models.IntegerField("max_focus", null=True)
    selfie = models.BooleanField("selfie", null=True)
    waterploof = models.BooleanField("waterploof", null=True)
    min_water_depth = models.IntegerField("water_depth", null=True)
    max_water_depth = models.IntegerField("water_depth", null=True)
    gps = models.BooleanField("gps", null=True)
    min_nearest_shot = models.FloatField("nearest_shot", null=True)
    max_nearest_shot = models.FloatField("nearest_shot", null=True)
    anti_shake = models.BooleanField("anti_shake", null=True)
    five_axis_anti_shake = \
                models.BooleanField("five_axis_anti_shake", null=True)
    min_nearest_shot_with_macro_mode = \
                models.FloatField("nearest_shot_with_macro_mode", null=True)
    max_nearest_shot_with_macro_mode = \
                models.FloatField("nearest_shot_with_macro_mode", null=True)
    min_f_value_wide = models.FloatField("f_value_wide", null=True)
    max_f_value_wide = models.FloatField("f_value_wide", null=True)
    super_wide = models.BooleanField("super_wide", null=True)
    min_open_date = models.DateField("min_open_date", null=True)
    max_open_date = models.DateField("max_open_date", null=True)
    camera_type_id = models.IntegerField("camera_type_id", null=True)
    target_keyword = models.CharField("target_keyword", max_length=255, null=True)
    created_at = models.DateTimeField("created_at", null=True)
    updated_at = models.DateTimeField("updated_at", null=True)

    def map_rank(self):
        rank = {
            "min_iso": self.min_iso,
            "max_iso": self.max_iso,
            "min_price": self.min_price,
            "max_price": self.max_price,
            "min_pixel": self.min_pixel,
            "max_pixel": self.max_pixel,
            "min_continuous_shooting_performance": self.min_continuous_shooting_performance,
            "max_continuous_shooting_performance": self.max_continuous_shooting_performance,
            "min_shutter_speed": self.min_shutter_speed,
            "max_shutter_speed": self.max_shutter_speed,
            "min_monitor_size": self.min_monitor_size,
            "max_monitor_size": self.max_monitor_size,
            "min_monitor_pixel": self.min_monitor_pixel,
            "max_monitor_pixel": self.max_monitor_pixel,
            "min_shooting_num": self.min_shooting_num,
            "max_shooting_num": self.max_shooting_num,
            "min_weight": self.min_weight,
            "max_weight": self.max_weight,
            "min_width": self.min_width,
            "max_width": self.max_width,
            "min_height": self.min_height,
            "max_height": self.max_height,
            "min_depth": self.min_depth,
            "max_depth": self.max_depth,
            "min_f_value_wide": self.min_f_value_wide,
            "max_f_value_wide": self.max_f_value_wide,
            "min_f_value_tele": self.min_f_value_tele,
            "max_f_value_tele": self.max_f_value_tele,
            "min_shooting_num_with_finder": self.min_shooting_num_with_finder,
            "max_shooting_num_with_finder": self.max_shooting_num_with_finder,
            "min_zoom": self.min_zoom,
            "max_zoom": self.max_zoom,
            "min_focus": self.min_focus,
            "max_focus": self.max_focus,
            "min_nearest_shot": self.min_nearest_shot,
            "max_nearest_shot": self.max_nearest_shot,
            "min_nearest_shot_with_macro_mode": self.min_nearest_shot_with_macro_mode,
            "max_nearest_shot_with_macro_mode": self.max_nearest_shot_with_macro_mode,
            "min_open_date": self.min_open_date,
            "max_open_date": self.max_open_date,
            "four_k": self.four_k,
            "wifi": self.wifi,
            "touch_panel": self.touch_panel,
            "move_panel": self.move_panel,
            "bluetooth": self.bluetooth,
            "selfie": self.selfie,
            "waterploof": self.waterploof,
            "gps": self.gps,
            "anti_shake": self.anti_shake,
            "five_axis_anti_shake": self.five_axis_anti_shake,
            "super_wide": self. super_wide,
            "camera_type_id": self.camera_type_id,
            "frame_id": self.frame_id,
            "finder_id": self.finder_id,
            "maker_id": self.maker_id
        }
        return rank

    @classmethod
    def import_csv(cls, file_path):
        df = pd.read_csv(file_path, encoding="utf-8")
        for _, row in df.iterrows():
            rank = Rank()

            rank.title = assign_item(row[1])
            rank.description = assign_item(row[2])
            rank.min_price = assign_item(row[3])
            rank.max_price = assign_item(row[4])
            rank.min_pixel = assign_item(row[5])
            rank.max_pixel = assign_item(row[6])
            rank.min_iso = assign_item(row[7])
            rank.max_iso = assign_item(row[8])
            rank.min_continuous_shooting_performance = assign_item(row[9])
            rank.max_continuous_shooting_performance = assign_item(row[10])
            rank.min_shutter_speed = assign_item(row[11])
            rank.max_shutter_speed = assign_item(row[12])
            rank.min_monitor_size = assign_item(row[13])
            rank.max_monitor_size = assign_item(row[14])
            rank.min_monitor_pixel = assign_item(row[15])
            rank.max_monitor_pixel = assign_item(row[16])
            rank.min_shooting_num = assign_item(row[17])
            rank.max_shooting_num = assign_item(row[18])
            rank.four_k = assign_item(row[19])
            rank.wifi = assign_item(row[20])
            rank.touch_panel = assign_item(row[21])
            rank.move_panel = assign_item(row[22])
            rank.min_weight = assign_item(row[23])
            rank.max_weight = assign_item(row[24])
            rank.min_width = assign_item(row[25])
            rank.max_width = assign_item(row[26])
            rank.min_height = assign_item(row[27])
            rank.max_height = assign_item(row[28])
            rank.min_depth = assign_item(row[29])
            rank.max_depth = assign_item(row[30])
            rank.frame_id = assign_item(row[31])
            rank.maker_id = assign_item(row[32])
            rank.finder_id = assign_item(row[33])
            rank.min_f_value_tele = assign_item(row[34])
            rank.max_f_value_tele = assign_item(row[35])
            rank.min_shooting_num_with_finder = assign_item(row[36])
            rank.max_shooting_num_with_finder = assign_item(row[37])
            rank.bluetooth = assign_item(row[38])
            rank.min_zoom = assign_item(row[39])
            rank.max_zoom = assign_item(row[40])
            rank.min_focus = assign_item(row[41])
            rank.max_focus = assign_item(row[42])
            rank.selfie = assign_item(row[43])
            rank.waterploof = assign_item(row[44])
            rank.min_water_depth = assign_item(row[45])
            rank.max_water_depth = assign_item(row[46])
            rank.gps = assign_item(row[47])
            rank.min_nearest_shot = assign_item(row[48])
            rank.max_nearest_shot = assign_item(row[49])
            rank.anti_shake = assign_item(row[50])
            rank.five_axis_anti_shake = assign_item(row[51])
            rank.min_nearest_shot_with_macro_mode = assign_item(row[52])
            rank.max_nearest_shot_with_macro_mode = assign_item(row[53])
            rank.min_f_value_wide = assign_item(row[54])
            rank.max_f_value_wide = assign_item(row[55])
            rank.super_wide = assign_item(row[56])
            rank.min_open_date = assign_item(row[57], "min_open_date")
            rank.max_open_date = assign_item(row[58], "max_open_date")
            rank.camera_type_id = assign_item(row[59])
            rank.target_keyword = assign_item(row[60])
            rank.created_at = "2019-1-15"
            rank.updated_at = timezone.localtime()

            rank.save()

    @classmethod
    def map_ranks(cls):
        ranks = Rank.objects.all()
        results = {}
        for rank in ranks:
            results[rank.id] = {
                "title": rank.title,
                "description": rank.description,
                "price": {"min": rank.min_price, "max": rank.max_price},
                "pixel": {"min": rank.min_pixel, "max": rank.max_pixel},
                "min_iso": rank.min_iso,
                "max_iso": rank.max_iso,
                "continuous_shooting_performance": {
                    "min": rank.min_continuous_shooting_performance,
                    "max": rank.max_continuous_shooting_performance
                },
                "shutter_speed": {
                    "min": rank.min_shutter_speed,
                    "max": rank.max_shutter_speed
                },
                "monitor_size": {
                    "min": rank.min_monitor_size,
                    "max": rank.max_monitor_size
                },
                "monitor_pixel": {
                    "min": rank.min_monitor_pixel,
                    "max": rank.max_monitor_pixel
                },
                "shooting_num": {
                    "min": rank.min_shooting_num,
                    "max": rank.max_shooting_num
                },
                "four_k": rank.four_k,
                "wifi": rank.wifi,
                "touch_panel": rank.touch_panel,
                "move_panel": rank.move_panel,
                "weight": {"min": rank.min_weight, "max": rank.max_weight},
                "width": {"min": rank.min_width, "max": rank.max_width},
                "height": {"min": rank.min_height, "max": rank.max_height},
                "depth": {"min": rank.min_depth, "max": rank.max_depth},
                "frame_id": rank.frame_id,
                "maker_id": rank.maker_id,
                "finder_id": rank.finder_id,
                "f_value": {"min": rank.min_f_value, "max": rank.max_f_value},
                "shooting_num_with_finder": {
                    "min": rank.min_shooting_num,
                    "max": rank.max_shooting_num
                },
                "bluetooth": rank.bluetooth,
                "zoom": {"min": rank.min_zoom, "max": rank.max_zoom},
                "min_focus": rank.min_focus,
                "max_focus": rank.max_focus,
                "selfie": rank.selfie,
                "waterploof": rank.waterploof,
                "gps": rank.gps,
                "nearest_shot": {
                    "min": rank.min_nearest_shot,
                    "max": rank.max_nearest_shot
                },
                "anti_shake": rank.anti_shake,
                "five_axis_anti_shake": rank.five_axis_anti_shake,
                "nearest_shot_with_macro_mode": {
                    "min": rank.min_nearest_shot_with_macro_mode,
                    "max": rank.max_nearest_shot_with_macro_mode
                },
                "f_value_wide": {
                    "min": rank.min_f_value_wide,
                    "max": rank.max_f_value_wide
                },
                "super_wide": rank.super_wide,
                "open_year": {
                    "min": rank.oldest_open_year,
                    "max": rank.newest_open_year
                },
                "open_month": {
                    "min": rank.oldest_open_month,
                    "max": rank.newest_open_month
                },
                "camera_type_id": rank.camera_type_id,
                "target_keyword": rank.target_keyword,
            }
        return results
