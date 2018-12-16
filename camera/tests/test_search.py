import pytest

from .factories import CameraFactory
from ..services import CameraSearcher


class SetUpCriteria:
    @classmethod
    def create(cls, criteria):
        return {
            'name': criteria.get("name"),
            'min_iso': criteria.get("min_iso"),
            'max_iso': criteria.get("max_iso"),
            'frame': criteria.get("frame"),
            'maker': criteria.get("maker"),
            'finder': criteria.get("finder"),
            'min_focus': criteria.get("min_focus"),
            'max_focus': criteria.get("max_focus"),
            'nearest_shot': criteria.get("nearest_shot"),
            'nearest_shot_with_macro_mode': criteria.get("nearest_shot_with_macro_mode"),
            'f_value_wide_wide_tele': criteria.get("f_value_wide_wide_tele"),
            'camera_type': criteria.get("camera_type"),
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
            'min_f_value_wide_tele': criteria.get("min_f_value_wide_tele", ""),
            'max_f_value_wide_tele': criteria.get("max_f_value_wide_tele", ""),
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
        assert actual[0]["f_value"] == 2
        assert actual[1]["f_value"] == 2.8

    def test_filter_by_max_f_value_wide(self):
        """最低ワイド端F値での絞り込みができているか"""
        CameraFactory.create(f_value_wide=4)
        CameraFactory.create(f_value_wide=5.6)
        CameraFactory.create(f_value_wide=8)

        criteria = SetUpCriteria.create({"max_f_value_wide": 5.6})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["f_value"] == 4
        assert actual[1]["f_value"] == 5.6

    def test_filter_by_min_shooting_num_with_finder(self):
        """最低ファインダー使用時撮影可能枚数での絞り込みができているか"""
        CameraFactory.create(shooting_num_with_finder=1.4)
        CameraFactory.create(shooting_num_with_finder=2.0)
        CameraFactory.create(shooting_num_with_finder=2.8)

        criteria = SetUpCriteria.create({"min_shooting_num_with_finder": 2})

        actual = CameraSearcher().filter(criteria)

        assert len(actual) == 2
        assert actual[0]["shooting_num_with_finder"] == 2
        assert actual[1]["shooting_num_with_finder"] == 2.8

    def test_filter_by_max_shooting_num_with_finder(self):
        pass

    def test_filter_by_min_focus(self):
        pass

    def test_filter_by_max_focus(self):
        pass

    def test_filter_by_min_zoom(self):
        pass

    def test_filter_by_max_zoom(self):
        pass

    def test_filter_by_min_nearest_shot(self):
        pass

    def test_filter_by_max_nearest_shot(self):
        pass

    def test_filter_by_min_nearest_shot_with_macro_mode(self):
        pass

    def test_filter_by_max_nearest_shot_with_macro_mode(self):
        pass

    def test_filter_by_min_f_value_tele(self):
        pass

    def test_filter_by_max_f_value_tele(self):
        pass

    def test_filter_by_min_open_date(self):
        pass

    def test_filter_by_max_open_date(self):
        pass

    def test_filter_by_four_k(self):
        pass

    def test_filter_by_wifi(self):
        pass

    def test_filter_by_touch_panel(self):
        pass

    def test_filter_by_move_panel(self):
        pass

    def test_filter_by_bluetooth(self):
        pass

    def test_filter_by_selfie(self):
        pass

    def test_filter_by_waterploof(self):
        pass

    def test_filter_by_gps(self):
        pass

    def test_filter_by_anti_shake(self):
        pass

    def test_filter_by_five_axis_anti_shake(self):
        pass

    def test_filter_by_super_wide(self):
        pass

    def test_filter_by_camera_type(self):
        pass

    def test_filter_by_frame(self):
        pass

    def test_filter_by_finder(self):
        pass

    def test_filter_by_maker(self):
        pass