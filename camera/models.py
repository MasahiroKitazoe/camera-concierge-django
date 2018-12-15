# coding: utf-8

from django.db import models

import pandas as pd
import math


class CameraType(models.Model):
    cam_type = models.CharField(max_length=50)

    def __str__(self):
        return self.cam_type

    @classmethod
    def import_csv(cls):
        file_path = "dataset/camera_types.csv"

        df = pd.read_csv(file_path, encoding='utf-8')
        for _, row in df.iterrows():
            c_type = CameraType()

            c_type.cam_type = row[1]
            c_type.save()


class Finder(models.Model):
    finder_type = models.CharField(max_length=50)

    def __str__(self):
        return self.finder_type

    @classmethod
    def import_csv(cls):
        file_path = "dataset/finders.csv"

        df = pd.read_csv(file_path, encoding='utf-8')
        for _, row in df.iterrows():
            finder = Finder()
            finder.finder_type = row[1]
            finder.save()


class Frame(models.Model):
    frame_type = models.CharField(max_length=50)

    def __str__(self):
        return self.frame_type

    @classmethod
    def import_csv(cls):
        file_path = "dataset/frames.csv"

        df = pd.read_csv(file_path, encoding='utf-8')
        for _, row in df.iterrows():
            frame = Frame()
            frame.frame_type = row[1]
            frame.save()


class Maker(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    @classmethod
    def import_csv(cls):
        file_path = "dataset/makers.csv"

        df = pd.read_csv(file_path, encoding='utf-8')
        for _, row in df.iterrows():
            maker = Maker()
            maker.name = row[1]
            maker.save()


class Review(models.Model):
    title = models.CharField(max_length=255)
    body = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    camera = models.ForeignKey("Camera", on_delete=models.PROTECT)

    # TODO: Reviewのimport失敗してる
    @classmethod
    def import_csv(cls):
        file_path = "dataset/reviews.csv"

        df = pd.read_csv(file_path, encoding='utf-8')
        for _, row in df.iterrows():
            review = Review()
            review.title = row[1]
            review.body = row[2]
            review.url = row[3]
            review.camera_id = row[4]
            review.save()


class Camera(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    pixel = models.IntegerField()
    min_iso = models.IntegerField()
    max_iso = models.IntegerField()
    continuous_shooting_performance = models.FloatField()
    shutter_speed = models.CharField(max_length=50)
    monitor_size = models.FloatField()
    monitor_pixel = models.FloatField()
    shooting_num = models.IntegerField()
    four_k = models.BooleanField()
    wifi = models.BooleanField()
    touch_panel = models.BooleanField()
    move_panel = models.CharField(max_length=50)
    weight = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    depth = models.FloatField()
    frame = models.ForeignKey("Frame", on_delete=models.PROTECT)
    maker = models.ForeignKey("Maker", on_delete=models.PROTECT)
    finder = models.ForeignKey("Finder", on_delete=models.PROTECT)
    f_value = models.FloatField()
    shooting_num_with_finder = models.IntegerField()
    bluetooth = models.CharField(max_length=20)
    zoom = models.FloatField()
    min_focus = models.IntegerField()
    max_focus = models.IntegerField()
    selfie = models.BooleanField()
    waterploof = models.CharField(max_length=50)
    gps = models.BooleanField()
    nearest_shot = models.FloatField()
    anti_shake = models.CharField(max_length=50)
    five_axis_anti_shake = models.BooleanField()
    nearest_shot_with_macro_mode = models.FloatField()
    f_value_wide = models.FloatField()
    super_wide = models.BooleanField()
    open_year = models.IntegerField()
    open_month = models.IntegerField()
    camera_type = models.ForeignKey("CameraType", on_delete=models.PROTECT)

    def assign_item(self, item):
      if type(item) == float and math.isnan(item):
        return 0
      else:
        if type(item) == str:
          item = item.replace("\u3000", " ")
        return item

    @classmethod
    def import_csv(cls):
      file_path = "dataset/cameras.csv"

      df = pd.read_csv(file_path, encoding='utf-8')
      for _, row in df.iterrows():
        camera = Camera()

        camera.name = camera.assign_item(row[1])
        camera.price = camera.assign_item(row[2])
        camera.pixel = camera.assign_item(row[3])
        camera.min_iso = camera.assign_item(row[4])
        camera.max_iso = camera.assign_item(row[5])
        camera.continuous_shooting_performance = camera.assign_item(row[6])
        camera.shutter_speed = camera.assign_item(row[7])
        camera.monitor_size = camera.assign_item(row[8])
        camera.monitor_pixel = camera.assign_item(row[9])
        camera.shooting_num = camera.assign_item(row[10])
        camera.four_k = camera.assign_item(row[11])
        camera.wifi = camera.assign_item(row[12])
        camera.touch_panel = camera.assign_item(row[13])
        camera.move_panel = camera.assign_item(row[14])
        camera.weight = camera.assign_item(row[15])
        camera.width = camera.assign_item(row[16])
        camera.height = camera.assign_item(row[17])
        camera.depth = camera.assign_item(row[18])
        camera.frame_id = camera.assign_item(row[19])
        camera.maker_id = camera.assign_item(row[20])
        camera.finder_id = camera.assign_item(row[21])
        camera.f_value = camera.assign_item(row[22])
        camera.shooting_num_with_finder = camera.assign_item(row[23])
        camera.bluetooth = camera.assign_item(row[24])
        camera.zoom = camera.assign_item(row[25])
        camera.min_focus = camera.assign_item(row[26])
        camera.max_focus = camera.assign_item(row[27])
        camera.selfie = camera.assign_item(row[28])
        camera.waterproof = camera.assign_item(row[29])
        camera.gps = camera.assign_item(row[30])
        camera.nearest_shot = camera.assign_item(row[31])
        camera.anti_shake = camera.assign_item(row[32])
        camera.five_axis_anti_shake = camera.assign_item(row[33])
        camera.nearest_shot_with_macro_mode = camera.assign_item(row[34])
        camera.f_value_wide = camera.assign_item(row[35])
        camera.super_wide = camera.assign_item(row[36])
        camera.open_year = camera.assign_item(row[37])
        camera.open_month = camera.assign_item(row[38])
        camera.camera_type_id = camera.assign_item(row[39])

        camera.save()

    @classmethod
    def delete_all_records(cls):
        cameras = Camera.objects.all()
        for camera in cameras:
            camera.delete()

    @classmethod
    def map_cameras(cls):
        cameras = Camera.objects.all().select_related("maker", "frame", "finder", "camera_type")
        results = {}
        for camera in cameras:
            results[camera.id] = {
                "name": camera.name,
                "price": camera.price,
                "pixel": camera.pixel,
                "min_iso": camera.min_iso,
                "max_iso": camera.max_iso,
                "continuous_shooting_performance": camera.continuous_shooting_performance,
                "shutter_speed": camera.shutter_speed,
                "monitor_size": camera.monitor_size,
                "monitor_pixel": camera.monitor_pixel,
                "shooting_num": camera.shooting_num,
                "four_k": camera.four_k,
                "wifi": camera.wifi,
                "touch_panel": camera.touch_panel,
                "move_panel": camera.move_panel,
                "weight": camera.weight,
                "width": camera.width,
                "height": camera.height,
                "depth": camera.depth,
                "frame_id": camera.frame.id,
                "maker_id": camera.maker.id,
                "finder_id": camera.finder.id,
                "f_value": camera.f_value,
                "shooting_num_with_finder": camera.shooting_num_with_finder,
                "bluetooth": camera.bluetooth,
                "zoom": camera.zoom,
                "min_focus": camera.min_focus,
                "max_focus": camera.max_focus,
                "selfie": camera.selfie,
                "waterploof": camera.waterploof,
                "gps": camera.gps,
                "nearest_shot": camera.nearest_shot,
                "anti_shake": camera.anti_shake,
                "five_axis_anti_shake": camera.five_axis_anti_shake,
                "nearest_shot_with_macro_mode": camera.nearest_shot_with_macro_mode,
                "f_value_wide": camera.f_value_wide,
                "super_wide": camera.super_wide,
                "open_year": camera.open_year,
                "open_month": camera.open_month,
                "camera_type_id": camera.camera_type.id
            }
        return results
