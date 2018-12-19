import pytest
from dateutil.parser import *

from .factories import CameraFactory, CameraTypeFactory, FinderFactory, FrameFactory, MakerFactory
from ..services import CameraSearcher


class SetUpCriteria:
    @classmethod
    def create(cls, criteria):
        return {
            'name': criteria.get("name"),
            'min_iso': criteria.get("min_iso"),
            'max_iso': criteria.get("max_iso"),
            'camera_type_id': criteria.get("camera_type_id"),
            'finder_id': criteria.get("finder_id"),
            'frame_id': criteria.get("frame_id"),
            'maker_id': criteria.get("maker_id"),
            'min_focus': criteria.get("min_focus"),
            'max_focus': criteria.get("max_focus"),
            'nearest_shot': criteria.get("nearest_shot"),
            'nearest_shot_with_macro_mode': criteria.get("nearest_shot_with_macro_mode"),
            'min_price': criteria.get("min_price"),
            'max_price': criteria.get("max_price"),
            'min_pixel': criteria.get("min_pixel"),
            'max_pixel': criteria.get("max_pixel"),
            'min_continuous_shooting_performance': criteria.get("min_continuous_shooting_performance"),
            'max_continuous_shooting_performance': criteria.get("max_continuous_shooting_performance"),
            'min_shutter_speed': criteria.get("min_shutter_speed", ""),
            'max_shutter_speed': criteria.get("max_shutter_speed", ""),
            'min_monitor_size': criteria.get("min_monitor_size"),
            'max_monitor_size': criteria.get("max_monitor_size"),
            'min_monitor_pixel': criteria.get("min_monitor_pixel"),
            'max_monitor_pixel': criteria.get("max_monitor_pixel"),
            'min_shooting_num': criteria.get("min_shooting_num"),
            'max_shooting_num': criteria.get("max_shooting_num"),
            'min_weight': criteria.get("min_weight"),
            'max_weight': criteria.get("max_weight"),
            'min_width': criteria.get("min_width"),
            'max_width': criteria.get("max_width"),
            'min_height': criteria.get("min_height"),
            'max_height': criteria.get("max_height"),
            'min_depth': criteria.get("min_depth"),
            'max_depth': criteria.get("max_depth"),
            'min_f_value_wide': criteria.get("min_f_value_wide", ""),
            'max_f_value_wide': criteria.get("max_f_value_wide", ""),
            'min_shooting_num_with_finder': criteria.get("min_shooting_num_with_finder"),
            'max_shooting_num_with_finder': criteria.get("max_shooting_num_with_finder"),
            'min_zoom': criteria.get("min_zoom"),
            'max_zoom': criteria.get("max_zoom"),
            'min_nearest_shot': criteria.get("min_nearest_shot"),
            'max_nearest_shot': criteria.get("max_nearest_shot"),
            'min_nearest_shot_with_macro_mode': criteria.get("min_nearest_shot_with_macro_mode"),
            'max_nearest_shot_with_macro_mode': criteria.get("max_nearest_shot_with_macro_mode"),
            'min_f_value_tele': criteria.get("min_f_value_tele", ""),
            'max_f_value_tele': criteria.get("max_f_value_tele", ""),
            'min_open_date': criteria.get("min_open_date"),
            'max_open_date': criteria.get("max_open_date"),
            'four_k': criteria.get("four_k", ""),
            'wifi': criteria.get("wifi", ""),
            'touch_panel': criteria.get("touch_panel", ""),
            'move_panel': criteria.get("move_panel", ""),
            'bluetooth': criteria.get("bluetooth", ""),
            'selfie': criteria.get("selfie", ""),
            'waterploof': criteria.get("waterploof", ""),
            'gps': criteria.get("gps", ""),
            'anti_shake': criteria.get("anti_shake", ""),
            'five_axis_anti_shake': criteria.get("five_axis_anti_shake", ""),
            'super_wide': criteria.get("super_wide", ""),
        }


@pytest.mark.django_db(transaction=True)
class TestCameraSearcher:
    def test_filter_by_name(self):
        """機種名での絞り込みができているか"""
        CameraFactory.create(name="α")
        CameraFactory.create(name="kiss")

        criteria = SetUpCriteria.create({"name": "α"})

        actual = CameraSearcher.filter(criteria)

        assert len(actual) == 1
        assert actual[0]["name"] == "α"

    def test_filter_by_min_price(self):
        """最低価格での絞り込みができているか"""
        CameraFactory.create(price=99999)
        CameraFactory.create(price=100000)
        CameraFactory.create(price=100001)

        criteria = SetUpCriteria.create({"min_price": 100000})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["price"] == 100000
        assert actual[1]["price"] == 100001

    def test_filter_by_max_price(self):
        """最高価格での絞り込みができているか"""
        CameraFactory.create(price=99999)
        CameraFactory.create(price=100000)
        CameraFactory.create(price=100001)

        criteria = SetUpCriteria.create({"max_price": 100000})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["price"] == 99999
        assert actual[1]["price"] == 100000

    def test_filter_by_min_pixel(self):
        """最低有効画素数での絞り込みができているか"""
        CameraFactory.create(pixel=1999)
        CameraFactory.create(pixel=2000)
        CameraFactory.create(pixel=2001)

        criteria = SetUpCriteria.create({"min_pixel": 2000})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["pixel"] == 2000
        assert actual[1]["pixel"] == 2001

    def test_filter_by_max_pixel(self):
        """最高有効画素数での絞り込みができているか"""
        CameraFactory.create(pixel=1999)
        CameraFactory.create(pixel=2000)
        CameraFactory.create(pixel=2001)

        criteria = SetUpCriteria.create({"max_pixel": 2000})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["pixel"] == 1999
        assert actual[1]["pixel"] == 2000

    def test_filter_by_min_continuous_shooting_performance(self):
        """最低連写性能での絞り込みができているか"""
        CameraFactory.create(continuous_shooting_performance=9)
        CameraFactory.create(continuous_shooting_performance=10)
        CameraFactory.create(continuous_shooting_performance=11)

        criteria = SetUpCriteria.create({"min_continuous_shooting_performance": 10})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["continuous_shooting_performance"] == 10
        assert actual[1]["continuous_shooting_performance"] == 11

    def test_filter_by_max_continuous_shooting_performance(self):
        """最高連写性能での絞り込みができているか"""
        CameraFactory.create(continuous_shooting_performance=9)
        CameraFactory.create(continuous_shooting_performance=10)
        CameraFactory.create(continuous_shooting_performance=11)

        criteria = SetUpCriteria.create({"max_continuous_shooting_performance": 10})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["continuous_shooting_performance"] == 9
        assert actual[1]["continuous_shooting_performance"] == 10

    def test_filter_by_min_shutter_speed(self):
        """最低シャッタースピードでの絞り込みができているか"""
        # TODO: シャッタースピード絞り込み機能が未実装。スクレイピング段階では、最低ssと最高ssの区別ができてない
        pass

    def test_filter_by_max_shutter_speed(self):
        """最高シャッタースピードでの絞り込みができているか"""
        pass

    def test_filter_by_min_monitor_size(self):
        """最低モニターサイズでの絞り込みができているか"""
        CameraFactory.create(monitor_size=2.9)
        CameraFactory.create(monitor_size=3)
        CameraFactory.create(monitor_size=3.1)

        criteria = SetUpCriteria.create({"min_monitor_size": 3})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["monitor_size"] == 3
        assert actual[1]["monitor_size"] == 3.1

    def test_filter_by_max_monitor_size(self):
        """最高モニターサイズでの絞り込みができているか"""
        CameraFactory.create(monitor_size=2.9)
        CameraFactory.create(monitor_size=3)
        CameraFactory.create(monitor_size=3.1)

        criteria = SetUpCriteria.create({"max_monitor_size": 3})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["monitor_size"] == 2.9
        assert actual[1]["monitor_size"] == 3

    def test_filter_by_min_monitor_pixel(self):
        """最低モニター解像度での絞り込みができているか"""
        CameraFactory.create(monitor_pixel=99)
        CameraFactory.create(monitor_pixel=100)
        CameraFactory.create(monitor_pixel=101)

        criteria = SetUpCriteria.create({"min_monitor_pixel": 100})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["monitor_pixel"] == 100
        assert actual[1]["monitor_pixel"] == 101

    def test_filter_by_max_monitor_pixel(self):
        """最高モニター解像度での絞り込みができているか"""
        CameraFactory.create(monitor_pixel=99)
        CameraFactory.create(monitor_pixel=100)
        CameraFactory.create(monitor_pixel=101)

        criteria = SetUpCriteria.create({"max_monitor_pixel": 100})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["monitor_pixel"] == 99
        assert actual[1]["monitor_pixel"] == 100

    def test_filter_by_min_shooting_num(self):
        """最低撮影可能枚数での絞り込みができているか"""
        CameraFactory.create(shooting_num=299)
        CameraFactory.create(shooting_num=300)
        CameraFactory.create(shooting_num=301)

        criteria = SetUpCriteria.create({"min_shooting_num": 300})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["shooting_num"] == 300
        assert actual[1]["shooting_num"] == 301

    def test_filter_by_max_shooting_num(self):
        """最高撮影可能枚数での絞り込みができているか"""
        CameraFactory.create(shooting_num=299)
        CameraFactory.create(shooting_num=300)
        CameraFactory.create(shooting_num=301)

        criteria = SetUpCriteria.create({"max_shooting_num": 300})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["shooting_num"] == 299
        assert actual[1]["shooting_num"] == 300

    def test_filter_by_min_weight(self):
        """最低重量での絞り込みができているか"""
        CameraFactory.create(weight=299)
        CameraFactory.create(weight=300)
        CameraFactory.create(weight=301)

        criteria = SetUpCriteria.create({"min_weight": 300})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["weight"] == 300
        assert actual[1]["weight"] == 301

    def test_filter_by_max_weight(self):
        """最高重量での絞り込みができているか"""
        CameraFactory.create(weight=299)
        CameraFactory.create(weight=300)
        CameraFactory.create(weight=301)

        criteria = SetUpCriteria.create({"max_weight": 300})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["weight"] == 299
        assert actual[1]["weight"] == 300

    def test_filter_by_min_width(self):
        """最低幅での絞り込みができているか"""
        CameraFactory.create(width=99)
        CameraFactory.create(width=100)
        CameraFactory.create(width=101)

        criteria = SetUpCriteria.create({"min_width": 100})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["width"] == 100
        assert actual[1]["width"] == 101

    def test_filter_by_max_width(self):
        """最高幅での絞り込みができているか"""
        CameraFactory.create(width=99)
        CameraFactory.create(width=100)
        CameraFactory.create(width=101)

        criteria = SetUpCriteria.create({"max_width": 100})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["width"] == 99
        assert actual[1]["width"] == 100

    def test_filter_by_min_height(self):
        """最低高さでの絞り込みができているか"""
        CameraFactory.create(height=99)
        CameraFactory.create(height=100)
        CameraFactory.create(height=101)

        criteria = SetUpCriteria.create({"min_height": 100})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["height"] == 100
        assert actual[1]["height"] == 101

    def test_filter_by_max_height(self):
        """最高高さでの絞り込みができているか"""
        CameraFactory.create(height=99)
        CameraFactory.create(height=100)
        CameraFactory.create(height=101)

        criteria = SetUpCriteria.create({"max_height": 100})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["height"] == 99
        assert actual[1]["height"] == 100

    def test_filter_by_min_depth(self):
        """最低奥行での絞り込みができているか"""
        CameraFactory.create(depth=49)
        CameraFactory.create(depth=50)
        CameraFactory.create(depth=51)

        criteria = SetUpCriteria.create({"min_depth": 50})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["depth"] == 50
        assert actual[1]["depth"] == 51

    def test_filter_by_max_depth(self):
        """最高奥行での絞り込みができているか"""
        CameraFactory.create(depth=49)
        CameraFactory.create(depth=50)
        CameraFactory.create(depth=51)

        criteria = SetUpCriteria.create({"max_depth": 50})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["depth"] == 49
        assert actual[1]["depth"] == 50

    def test_filter_by_min_f_value_wide(self):
        """最低ワイド端F値での絞り込みができているか"""
        CameraFactory.create(f_value_wide=1.4)
        CameraFactory.create(f_value_wide=2.0)
        CameraFactory.create(f_value_wide=2.8)

        criteria = SetUpCriteria.create({"min_f_value_wide": 2})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["f_value_wide"] == 2
        assert actual[1]["f_value_wide"] == 2.8

    def test_filter_by_max_f_value_wide(self):
        """最高ワイド端F値での絞り込みができているか"""
        CameraFactory.create(f_value_wide=4)
        CameraFactory.create(f_value_wide=5.6)
        CameraFactory.create(f_value_wide=8)

        criteria = SetUpCriteria.create({"max_f_value_wide": 5.6})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["f_value_wide"] == 4
        assert actual[1]["f_value_wide"] == 5.6

    def test_filter_by_min_shooting_num_with_finder(self):
        """最低ファインダー使用時撮影可能枚数での絞り込みができているか"""
        CameraFactory.create(shooting_num_with_finder=299)
        CameraFactory.create(shooting_num_with_finder=300)
        CameraFactory.create(shooting_num_with_finder=301)

        criteria = SetUpCriteria.create({"min_shooting_num_with_finder": 300})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["shooting_num_with_finder"] == 300
        assert actual[1]["shooting_num_with_finder"] == 301

    def test_filter_by_max_shooting_num_with_finder(self):
        """最高ファインダー使用時撮影可能枚数での絞り込みができているか"""
        CameraFactory.create(shooting_num_with_finder=299)
        CameraFactory.create(shooting_num_with_finder=300)
        CameraFactory.create(shooting_num_with_finder=301)

        criteria = SetUpCriteria.create({"max_shooting_num_with_finder": 300})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["shooting_num_with_finder"] == 299
        assert actual[1]["shooting_num_with_finder"] == 300

    def test_filter_by_min_focus(self):
        """最低焦点距離での絞り込みができているか"""
        CameraFactory.create(min_focus=19)
        CameraFactory.create(min_focus=20)
        CameraFactory.create(min_focus=21)

        criteria = SetUpCriteria.create({"min_focus": 20})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["min_focus"] == 20
        assert actual[1]["min_focus"] == 21

    def test_filter_by_max_focus(self):
        """最高焦点距離での絞り込みができているか"""
        CameraFactory.create(max_focus=19)
        CameraFactory.create(max_focus=20)
        CameraFactory.create(max_focus=21)

        criteria = SetUpCriteria.create({"max_focus": 20})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["max_focus"] == 19
        assert actual[1]["max_focus"] == 20

    def test_filter_by_min_zoom(self):
        """最低ズーム倍率での絞り込みができているか"""
        CameraFactory.create(zoom=4.9)
        CameraFactory.create(zoom=5)
        CameraFactory.create(zoom=5.1)

        criteria = SetUpCriteria.create({"min_zoom": 5})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["zoom"] == 5
        assert actual[1]["zoom"] == 5.1

    def test_filter_by_max_zoom(self):
        """最高ズーム倍率での絞り込みができているか"""
        CameraFactory.create(zoom=4.9)
        CameraFactory.create(zoom=5)
        CameraFactory.create(zoom=5.1)

        criteria = SetUpCriteria.create({"max_zoom": 5})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["zoom"] == 4.9
        assert actual[1]["zoom"] == 5

    def test_filter_by_min_nearest_shot(self):
        """最低最短撮影距離での絞り込みができているか"""
        CameraFactory.create(nearest_shot=9)
        CameraFactory.create(nearest_shot=10)
        CameraFactory.create(nearest_shot=11)

        criteria = SetUpCriteria.create({"min_nearest_shot": 10})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["nearest_shot"] == 10
        assert actual[1]["nearest_shot"] == 11

    def test_filter_by_max_nearest_shot(self):
        """最高最短撮影距離での絞り込みができているか"""
        CameraFactory.create(nearest_shot=9)
        CameraFactory.create(nearest_shot=10)
        CameraFactory.create(nearest_shot=11)

        criteria = SetUpCriteria.create({"max_nearest_shot": 10})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["nearest_shot"] == 9
        assert actual[1]["nearest_shot"] == 10

    def test_filter_by_min_nearest_shot_with_macro_mode(self):
        """最低マクロモード時最短撮影距離での絞り込みができているか"""
        CameraFactory.create(nearest_shot_with_macro_mode=9)
        CameraFactory.create(nearest_shot_with_macro_mode=10)
        CameraFactory.create(nearest_shot_with_macro_mode=11)

        criteria = SetUpCriteria.create({"min_nearest_shot_with_macro_mode": 10})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["nearest_shot_with_macro_mode"] == 10
        assert actual[1]["nearest_shot_with_macro_mode"] == 11

    def test_filter_by_max_nearest_shot_with_macro_mode(self):
        """最高マクロモード時最短撮影距離での絞り込みができているか"""
        CameraFactory.create(nearest_shot_with_macro_mode=9)
        CameraFactory.create(nearest_shot_with_macro_mode=10)
        CameraFactory.create(nearest_shot_with_macro_mode=11)

        criteria = SetUpCriteria.create({"max_nearest_shot_with_macro_mode": 10})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["nearest_shot_with_macro_mode"] == 9
        assert actual[1]["nearest_shot_with_macro_mode"] == 10

    def test_filter_by_min_f_value_tele(self):
        """最低テレ端F値での絞り込みができているか"""
        CameraFactory.create(f_value_tele=1.4)
        CameraFactory.create(f_value_tele=2.0)
        CameraFactory.create(f_value_tele=2.8)

        criteria = SetUpCriteria.create({"min_f_value_tele": 2})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["f_value_tele"] == 2
        assert actual[1]["f_value_tele"] == 2.8

    def test_filter_by_max_f_value_tele(self):
        """最高テレ端F値での絞り込みができているか"""
        CameraFactory.create(f_value_tele=4)
        CameraFactory.create(f_value_tele=5.6)
        CameraFactory.create(f_value_tele=8)

        criteria = SetUpCriteria.create({"max_f_value_tele": 5.6})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["f_value_tele"] == 4
        assert actual[1]["f_value_tele"] == 5.6

    def test_filter_by_min_open_date(self):
        """最古発売日での絞り込みができているか"""
        CameraFactory.create(open_year=2018, open_month=10)
        CameraFactory.create(open_year=2018, open_month=11)
        CameraFactory.create(open_year=2018, open_month=12)

        criteria = SetUpCriteria.create({"min_open_date": parse("2018/11")})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["open_date"].year == 2018
        assert actual[0]["open_date"].month == 11
        assert actual[1]["open_date"].year == 2018
        assert actual[1]["open_date"].month == 12

    def test_filter_by_max_open_date(self):
        """最新発売日での絞り込みができているか"""
        CameraFactory.create(open_year=2018, open_month=10)
        CameraFactory.create(open_year=2018, open_month=11)
        CameraFactory.create(open_year=2018, open_month=12)

        criteria = SetUpCriteria.create({"max_open_date": parse("2018/11")})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["open_date"].year == 2018
        assert actual[0]["open_date"].month == 10
        assert actual[1]["open_date"].year == 2018
        assert actual[1]["open_date"].month == 11

    def test_filter_by_four_k_true(self):
        """4k動画撮影有りで絞り込みができているか"""
        CameraFactory.create(four_k=True)
        CameraFactory.create(four_k=False)

        criteria = SetUpCriteria.create({"four_k": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["four_k"] == True

    def test_filter_by_four_k_false(self):
        """4k動画撮影無しで絞り込みができているか"""
        CameraFactory.create(four_k=True)
        CameraFactory.create(four_k=False)

        criteria = SetUpCriteria.create({"four_k": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["four_k"] == False

    def test_filter_by_wifi_true(self):
        """WiFi機能有りで絞り込みができているか"""
        CameraFactory.create(wifi=True)
        CameraFactory.create(wifi=False)

        criteria = SetUpCriteria.create({"wifi": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["wifi"] == True

    def test_filter_by_wifi_false(self):
        """WiFi機能無しで絞り込みができているか"""
        CameraFactory.create(wifi=True)
        CameraFactory.create(wifi=False)

        criteria = SetUpCriteria.create({"wifi": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["wifi"] == False

    def test_filter_by_touch_panel_true(self):
        """タッチパネル有りで絞り込みができているか"""
        CameraFactory.create(touch_panel=True)
        CameraFactory.create(touch_panel=False)

        criteria = SetUpCriteria.create({"touch_panel": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["touch_panel"] == True

    def test_filter_by_touch_panel_false(self):
        """タッチパネル無しで絞り込みができているか"""
        CameraFactory.create(touch_panel=True)
        CameraFactory.create(touch_panel=False)

        criteria = SetUpCriteria.create({"touch_panel": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["touch_panel"] == False

    def test_filter_by_move_panel_true(self):
        """可動式パネル有りで絞り込みができているか"""
        CameraFactory.create(move_panel="チルト液晶")
        CameraFactory.create(move_panel="")

        criteria = SetUpCriteria.create({"move_panel": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["move_panel"] == True

    def test_filter_by_move_panel_false(self):
        """可動式パネル無しで絞り込みができているか"""
        CameraFactory.create(move_panel="チルト液晶")
        CameraFactory.create(move_panel="")

        criteria = SetUpCriteria.create({"move_panel": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["move_panel"] == False

    def test_filter_by_bluetooth_true(self):
        """Bluetooth有りで絞り込みができているか"""
        CameraFactory.create(bluetooth="○")
        CameraFactory.create(bluetooth="")

        criteria = SetUpCriteria.create({"bluetooth": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["bluetooth"] == True

    def test_filter_by_bluetooth_false(self):
        """Bluetooth無しで絞り込みができているか"""
        CameraFactory.create(bluetooth="○")
        CameraFactory.create(bluetooth="")

        criteria = SetUpCriteria.create({"bluetooth": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["bluetooth"] == False

    def test_filter_by_selfie_true(self):
        """自撮り有りで絞り込みができているか"""
        CameraFactory.create(selfie=True)
        CameraFactory.create(selfie=False)

        criteria = SetUpCriteria.create({"selfie": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["selfie"] == True

    def test_filter_by_selfie_false(self):
        """自撮り無しで絞り込みができているか"""
        CameraFactory.create(selfie=True)
        CameraFactory.create(selfie=False)

        criteria = SetUpCriteria.create({"selfie": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["selfie"] == False

    def test_filter_by_waterploof_true(self):
        """防水有りで絞り込みができているか"""
        CameraFactory.create(waterploof="10m")
        CameraFactory.create(waterploof="")

        criteria = SetUpCriteria.create({"waterploof": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["waterploof"] == True

    def test_filter_by_waterploof_false(self):
        """防水無しで絞り込みができているか"""
        CameraFactory.create(waterploof="10m")
        CameraFactory.create(waterploof="")

        criteria = SetUpCriteria.create({"waterploof": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["waterploof"] == False

    def test_filter_by_gps_true(self):
        """GPS有りで絞り込みができているか"""
        CameraFactory.create(gps=True)
        CameraFactory.create(gps=False)

        criteria = SetUpCriteria.create({"gps": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["gps"] == True

    def test_filter_by_gps_false(self):
        """GPS無しで絞り込みができているか"""
        CameraFactory.create(gps=True)
        CameraFactory.create(gps=False)

        criteria = SetUpCriteria.create({"gps": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["gps"] == False

    def test_filter_by_anti_shake_true(self):
        """手ぶれ補正有りで絞り込みができているか"""
        CameraFactory.create(anti_shake="5軸手ぶれ補正")
        CameraFactory.create(anti_shake="")

        criteria = SetUpCriteria.create({"anti_shake": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["anti_shake"] == True

    def test_filter_by_anti_shake_false(self):
        """手ぶれ補正有りで絞り込みができているか"""
        CameraFactory.create(anti_shake="5軸手ぶれ補正")
        CameraFactory.create(anti_shake="")

        criteria = SetUpCriteria.create({"anti_shake": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["anti_shake"] == True

    def test_filter_by_five_axis_anti_shake_true(self):
        """GPS有りで絞り込みができているか"""
        CameraFactory.create(five_axis_anti_shake=True)
        CameraFactory.create(five_axis_anti_shake=False)

        criteria = SetUpCriteria.create({"five_axis_anti_shake": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["five_axis_anti_shake"] == True

    def test_filter_by_five_axis_anti_shake_false(self):
        """GPS無しで絞り込みができているか"""
        CameraFactory.create(five_axis_anti_shake=True)
        CameraFactory.create(five_axis_anti_shake=False)

        criteria = SetUpCriteria.create({"five_axis_anti_shake": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["five_axis_anti_shake"] == False

    def test_filter_by_super_wide_true(self):
        """超広角有りで絞り込みができているか"""
        CameraFactory.create(super_wide=True)
        CameraFactory.create(super_wide=False)

        criteria = SetUpCriteria.create({"super_wide": True})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["super_wide"] == True

    def test_filter_by_super_wide_false(self):
        """超広角無しで絞り込みができているか"""
        CameraFactory.create(super_wide=True)
        CameraFactory.create(super_wide=False)

        criteria = SetUpCriteria.create({"super_wide": False})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["super_wide"] == False

    def test_filter_by_camera_type(self):
        cam_type1 = CameraTypeFactory.create(cam_type="一眼レフ")
        cam_type2 = CameraTypeFactory.create(cam_type="ミラーレス一眼")
        CameraFactory(camera_type=cam_type1)
        CameraFactory(camera_type=cam_type2)

        criteria = SetUpCriteria.create({"camera_type_id": cam_type2.id})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["camera_type_id"] == cam_type2.id

    def test_filter_by_frame(self):
        frame1 = FrameFactory.create(frame_type="フルサイズ")
        frame2 = FrameFactory.create(frame_type="APS-C")
        CameraFactory(frame=frame1)
        CameraFactory(frame=frame2)

        criteria = SetUpCriteria.create({"frame_id": frame2.id})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["frame_id"] == frame2.id

    def test_filter_by_finder(self):
        finder1 = FinderFactory.create(finder_type="光学式ファインダー")
        finder2 = FinderFactory.create(finder_type="電子式ファインダー")
        CameraFactory(finder=finder1)
        CameraFactory(finder=finder2)

        criteria = SetUpCriteria.create({"finder_id": finder2.id})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["finder_id"] == finder2.id

    def test_filter_by_maker(self):
        maker1 = MakerFactory.create(name="ソニー")
        maker2 = MakerFactory.create(name="オリンパス")
        CameraFactory(maker=maker1)
        CameraFactory(maker=maker2)

        criteria = SetUpCriteria.create({"maker_id": maker2.id})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 1
        assert actual[0]["maker_id"] == maker2.id
