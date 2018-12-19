import factory
from factory.django import DjangoModelFactory

from camera.models import Camera, CameraType, Finder, Frame, Maker


class CameraTypeFactory(DjangoModelFactory):
    class Meta:
        model = CameraType

    cam_type = "ミラーレス一眼"


class FinderFactory(DjangoModelFactory):
    class Meta:
        model = Finder

    finder_type = "電子式ビューファインダー"


class FrameFactory(DjangoModelFactory):
    class Meta:
        model = Frame

    frame_type = "フルサイズ"


class MakerFactory(DjangoModelFactory):
    class Meta:
        model = Maker

    name = "ソニー"


class CameraFactory(DjangoModelFactory):
    class Meta:
        model = Camera

    name = "α1000"
    price = 100000
    pixel = 1800
    min_iso = 30
    max_iso = 12800
    continuous_shooting_performance = 10
    shutter_speed = "1/4000～30 秒"
    monitor_size = 3
    monitor_pixel = 92.16
    shooting_num = 360
    four_k = False
    wifi = True
    touch_panel = False
    move_panel = "チルト式"
    weight = 285
    width = 120.0
    height = 66.9
    depth = 45.1
    frame = factory.SubFactory(FrameFactory)
    maker = factory.SubFactory(MakerFactory)
    finder = factory.SubFactory(FinderFactory)
    f_value_wide = 1.8
    f_value_tele = 4
    shooting_num_with_finder = 310
    bluetooth = "○"
    zoom = 2.9
    min_focus = 24
    max_focus = 70
    selfie = True
    waterploof = ""
    gps = False
    nearest_shot = 5
    anti_shake = "電子式"
    five_axis_anti_shake = False
    nearest_shot_with_macro_mode = 0
    super_wide = False
    open_year = 2014
    open_month = 5
    camera_type = factory.SubFactory(CameraTypeFactory)
