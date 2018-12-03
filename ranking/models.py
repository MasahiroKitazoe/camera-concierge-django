from django.db import models

from camera.models import Frame
from camera.models import Finder
from camera.models import Maker
from camera.models import CameraType
from ranking.data_import import import_csv_into_model


class Rank(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    min_price = models.IntegerField("price")
    max_price = models.IntegerField("price")
    min_pixel = models.IntegerField("pixel")
    max_pixel = models.IntegerField("pixel")
    min_iso = models.IntegerField("iso")
    max_iso = models.IntegerField("iso")
    min_continuous_shooting_performance = \
                models.FloatField("continuous_shooting_performance")
    max_continuous_shooting_performance = \
                models.FloatField("continuous_shooting_performance")
    min_shutter_speed = \
                models.CharField("shutter_speed", max_length=50)
    max_shutter_speed = \
                models.CharField("shutter_speed", max_length=50)
    min_monitor_size = models.FloatField("monitor_size")
    max_monitor_size = models.FloatField("monitor_size")
    min_monitor_pixel = models.FloatField("monitor_pixel")
    min_monitor_pixel = models.FloatField("monitor_pixel")
    min_num_of_shooting = models.IntegerField("num_of_shooting")
    max_num_of_shooting = models.IntegerField("num_of_shooting")
    four_k = models.BooleanField("four_k", null=True)
    wifi = models.BooleanField("wifi", null=True)
    touch_panel = models.BooleanField("touch_panel", null=True)
    move_panel = models.BooleanField("move_panel", null=True)
    min_weight = models.FloatField("weight")
    max_weight = models.FloatField("weight")
    min_width = models.FloatField("width")
    max_width = models.FloatField("width")
    min_height = models.FloatField("height")
    max_height = models.FloatField("height")
    min_depth = models.FloatField("depth")
    max_depth = models.FloatField("depth")
    frame_id = models.IntegerField("frame_id")
    maker_id = models.IntegerField("maker_id")
    finder_id = models.IntegerField("finder_id")
    min_f_value = models.FloatField("f_value")
    max_f_value = models.FloatField("f_value")
    min_num_of_shooting_with_finder = \
                models.IntegerField("num_of_shooting_with_finder")
    max_num_of_shooting_with_finder = \
                models.IntegerField("num_of_shooting_with_finder")
    bluetooth = models.BooleanField("bluetooth", null=True)
    min_zoom = models.FloatField("zoom")
    max_zoom = models.FloatField("zoom")
    min_focus = models.IntegerField("focus")
    max_focus = models.IntegerField("focus")
    selfie = models.BooleanField("selfie", null=True)
    waterploof = models.BooleanField("waterploof", null=True)
    min_water_depth = models.IntegerField("water_depth")
    max_water_depth = models.IntegerField("water_depth")
    gps = models.BooleanField("gps", null=True)
    min_nearest_shot = models.FloatField("nearest_shot")
    max_nearest_shot = models.FloatField("nearest_shot")
    anti_shake = models.BooleanField("anti_shake", null=True)
    five_axis_anti_shake = \
                models.BooleanField("five_axis_anti_shake", null=True)
    min_nearest_shot_with_macro_mode = \
                models.FloatField("nearest_shot_with_macro_mode")
    min_nearest_shot_with_macro_mode = \
                models.FloatField("nearest_shot_with_macro_mode")
    min_f_value_wide = models.FloatField("f_value_wide")
    max_f_value_wide = models.FloatField("f_value_wide")
    super_wide = models.BooleanField("super_wide", null=True)
    oldest_open_year = models.IntegerField("oldest_open_year")
    newest_open_year = models.IntegerField("newest_open_year")
    oldest_open_month = models.IntegerField("oldest_open_month")
    newest_open_month = models.IntegerField("newest_open_month")
    camera_type_id = models.IntegerField("camera_type_id")
    target_keyword = models.CharField("target_keyword", max_length=255, null=True)

    @classmethod
    def import_csv(cls):
      file_path = "dataset/ranking.csv"
      import_csv_into_model(file_path, Rank)
