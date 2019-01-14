# coding: utf-8

from dateutil.parser import *
from django.db import models

import pandas as pd
import math

from ranking.utils import assign_item


class CameraType(models.Model):
    cam_type = models.CharField(max_length=50)

    def __str__(self):
        return str(self.__dict__)

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
        return str(self.__dict__)

    def choice_name(self):
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
        return str(self.__dict__)

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
        return str(self.__dict__)

    def choice_name(self):
        return self.name

    @classmethod
    def import_csv(cls):
        file_path = "dataset/makers.csv"

        df = pd.read_csv(file_path, encoding='utf-8')
        for _, row in df.iterrows():
            maker = Maker()
            maker.name = row[1]
            maker.save()


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
    f_value_wide = models.FloatField()
    f_value_tele = models.FloatField()
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
    super_wide = models.BooleanField()
    open_year = models.IntegerField()
    open_month = models.IntegerField()
    camera_type = models.ForeignKey("CameraType", on_delete=models.PROTECT)
    amazon_link = models.TextField()
    rakuten_link = models.TextField()
    image_url = models.TextField()

    def open_date(self):
        if not self.open_year or not self.open_month:
            return None
        year = str(self.open_year)
        month = str(self.open_month)

        open_date_str = "{}/{}".format(year, month)
        return parse(open_date_str)

    def move_panel_mounted(self):
        if self.move_panel:
            return True
        else:
            return False

    def bluetooth_mounted(self):
        if self.bluetooth:
            return True
        else:
            return False

    def is_waterploof(self):
        if self.waterploof:
            return True
        else:
            return False

    def is_anti_shake(self):
        if self.anti_shake:
            return True
        else:
            return False

    @classmethod
    def import_csv(cls, file_path):
        df = pd.read_csv(file_path, encoding='utf-8')
        for _, row in df.iterrows():
            camera = Camera()

            camera.name = assign_item(row[1])
            camera.price = assign_item(row[2])
            camera.pixel = assign_item(row[3])
            camera.min_iso = assign_item(row[4])
            camera.max_iso = assign_item(row[5])
            camera.continuous_shooting_performance = assign_item(row[6])
            camera.shutter_speed = assign_item(row[7])
            camera.monitor_size = assign_item(row[8])
            camera.monitor_pixel = assign_item(row[9])
            camera.shooting_num = assign_item(row[10])
            camera.four_k = assign_item(row[11])
            camera.wifi = assign_item(row[12])
            camera.touch_panel = assign_item(row[13])
            camera.move_panel = assign_item(row[14])
            camera.weight = assign_item(row[15])
            camera.width = assign_item(row[16])
            camera.height = assign_item(row[17])
            camera.depth = assign_item(row[18])
            camera.frame_id = assign_item(row[19])
            camera.maker_id = assign_item(row[20])
            camera.finder_id = assign_item(row[21])
            camera.f_value_wide = assign_item(row[22])
            camera.shooting_num_with_finder = assign_item(row[23])
            camera.bluetooth = assign_item(row[24])
            camera.zoom = assign_item(row[25])
            camera.min_focus = assign_item(row[26])
            camera.max_focus = assign_item(row[27])
            camera.selfie = assign_item(row[28])
            camera.waterproof = assign_item(row[29])
            camera.gps = assign_item(row[30])
            camera.nearest_shot = assign_item(row[31])
            camera.anti_shake = assign_item(row[32])
            camera.five_axis_anti_shake = assign_item(row[33])
            camera.nearest_shot_with_macro_mode = assign_item(row[34])
            camera.f_value_tele = assign_item(row[35])
            camera.super_wide = assign_item(row[36])
            camera.open_year = assign_item(row[37])
            camera.open_month = assign_item(row[38])
            camera.camera_type_id = assign_item(row[39])
            camera.amazon_link = assign_item(row[40])
            camera.rakuten_link = assign_item(row[41])
            camera.image_url = assign_item(row[42])

            camera.save()

    @classmethod
    def delete_all_records(cls):
        cameras = Camera.objects.all()
        for camera in cameras:
            camera.delete()

    @classmethod
    def map_cameras(cls):
        """
        カメラの機種データを1レコードずつ取り出して、辞書形式にマッピングし、配列に格納するメソッド。
        ※ 発売日に関しては、str型からdatetime型に整形して、"open_date"として格納している
        :return: カメラのスペック情報が入った辞書を格納した配列
        """
        cameras = Camera.objects.all().select_related("maker", "frame", "finder", "camera_type", "hashtag")
        reviews = Review.map_reviews_by_camera_id()
        results = {}
        for camera in cameras:
            results[camera.id] = {
                "id": camera.id,
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
                "move_panel": camera.move_panel_mounted(),
                "weight": camera.weight,
                "width": camera.width,
                "height": camera.height,
                "depth": camera.depth,
                "frame_id": camera.frame.id,
                "frame": {
                    "frame_type": camera.frame.frame_type
                },
                "maker_id": camera.maker.id,
                "maker": {
                    "name": camera.maker.name
                },
                "finder_id": camera.finder.id,
                "finder": {
                    "finder_type": camera.finder.finder_type
                },
                "f_value_wide": camera.f_value_wide,
                "shooting_num_with_finder": camera.shooting_num_with_finder,
                "bluetooth": camera.bluetooth_mounted(),
                "zoom": camera.zoom,
                "min_focus": camera.min_focus,
                "max_focus": camera.max_focus,
                "selfie": camera.selfie,
                "waterploof": camera.is_waterploof(),
                "gps": camera.gps,
                "nearest_shot": camera.nearest_shot,
                "anti_shake": camera.is_anti_shake(),
                "five_axis_anti_shake": camera.five_axis_anti_shake,
                "nearest_shot_with_macro_mode": camera.nearest_shot_with_macro_mode,
                "f_value_tele": camera.f_value_tele,
                "super_wide": camera.super_wide,
                "open_date": camera.open_date(),
                "camera_type_id": camera.camera_type.id,
                "camera_type": {
                    "cam_type": camera.camera_type.cam_type
                },
                "amazon_link": camera.amazon_link,
                "rakuten_link": camera.rakuten_link,
                "image_url": camera.image_url,
                "review_count": len(reviews[camera.id]),
                "hashtag_count": camera.hashtag.count,
                "hashtag_increase_count": camera.hashtag.week_increase
            }
        return results, reviews


class Review(models.Model):
    title = models.TextField()
    body = models.TextField()
    url = models.TextField()
    camera = models.ForeignKey("Camera", on_delete=models.PROTECT)

    @classmethod
    def import_csv(cls, file_path):
        df = pd.read_csv(file_path, encoding='utf-8')
        for _, row in df.iterrows():
            review = Review()
            review.title = row[1]
            review.body = row[2]
            review.url = row[3]
            review.camera_id = row[4]
            review.save()

    @classmethod
    def map_reviews_by_camera_id(cls):
        mapped_reviews = {}
        reviews = Review.objects.all()
        for review in reviews:
            review_dict = {
                "id": review.id,
                "title": review.title,
                "body": review.body,
                "url": review.url,
            }
            mapped_reviews.setdefault(review.camera_id, [])
            mapped_reviews[review.camera_id].append(review_dict)
        return mapped_reviews


class HashTag(models.Model):
    camera = models.OneToOneField(Camera, on_delete=models.CASCADE, primary_key=True)
    count = models.IntegerField("ハッシュタグ数")
    week_increase = models.IntegerField("週間ハッシュタグ増加数")

    @classmethod
    def import_csv(cls, file_path):
        df = pd.read_csv(file_path)
        for _, row in df.iterrows():
            hashtag = HashTag()

            hashtag.camera_id = assign_item(row[1])
            hashtag.count = assign_item(row[3])
            hashtag.week_increase = assign_item(row[4])

            hashtag.save()
