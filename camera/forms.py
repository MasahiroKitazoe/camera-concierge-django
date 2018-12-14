from django import forms
from django.forms import ModelForm

from .models import Camera
from .consts import SHUTTER_SPEED, F_VALUE, BOOLEAN


class SearchForm(ModelForm):
    min_price = forms.IntegerField(label="価格(下限)", required=False)
    max_price = forms.IntegerField(label="価格(上限)", required=False)
    min_pixel = forms.IntegerField(label="有効画素数(下限)", required=False)
    max_pixel = forms.IntegerField(label="有効画素数(上限)", required=False)
    min_continuous_shooting_performance = \
      forms.FloatField(label="連写性能(下限)", required=False)
    max_continuous_shooting_performance = \
      forms.FloatField(label="連写性能(上限)", required=False)
    min_shutter_speed = forms.ChoiceField(label="シャッタースピード(下限)", required=False, choices=SHUTTER_SPEED)
    max_shutter_speed = forms.ChoiceField(label="シャッタースピード(上限)", required=False, choices=SHUTTER_SPEED)
    min_monitor_size = forms.FloatField(label="モニターサイズ(下限)", required=False)
    max_monitor_size = forms.FloatField(label="モニターサイズ(上限)", required=False)
    min_monitor_pixel = forms.IntegerField(label="モニター解像度(下限)", required=False)
    max_monitor_pixel = forms.IntegerField(label="モニター解像度(上限)", required=False)
    min_shooting_num = forms.IntegerField(label="撮影可能枚数(下限)", required=False)
    max_shooting_num = forms.IntegerField(label="撮影可能枚数(上限)", required=False)
    min_weight = forms.FloatField(label="重さ(下限)", required=False)
    max_weight = forms.FloatField(label="重さ(上限)", required=False)
    min_width = forms.FloatField(label="幅(下限)", required=False)
    max_width = forms.FloatField(label="幅(上限)", required=False)
    min_height = forms.FloatField(label="高さ(下限)", required=False)
    max_height = forms.FloatField(label="高さ(上限)", required=False)
    min_depth = forms.FloatField(label="奥行(下限)", required=False)
    max_depth = forms.FloatField(label="奥行(上限)", required=False)
    min_f_value = forms.ChoiceField(label="F値(下限)", required=False, choices=F_VALUE)
    max_f_value = forms.ChoiceField(label="F値(上限)", required=False, choices=F_VALUE)
    min_shootin_num_with_finder = \
      forms.IntegerField(label="ファインダー使用時の撮影可能枚数(下限)", required=False)
    max_shootin_num_with_finder = \
      forms.IntegerField(label="ファインダー使用時の撮影可能枚数(上限)", required=False)
    min_zoom = forms.IntegerField(label="ズーム(下限)", required=False)
    max_zoom = forms.IntegerField(label="ズーム(上限)", required=False)
    min_nearest_shot = forms.FloatField(label="最短撮影距離(下限)", required=False)
    max_nearest_shot = forms.FloatField(label="最短撮影距離(上限)", required=False)
    min_nearest_shot_with_macro_mode = \
      forms.FloatField(label="マクロモード時最短撮影距離(下限)", required=False)
    max_nearest_shot_with_macro_mode = \
      forms.FloatField(label="マクロモード時最短撮影距離(上限)", required=False)
    min_f_value_wide = forms.ChoiceField(label="ワイド端F値(下限)", required=False, choices=F_VALUE)
    max_f_value_wide = forms.ChoiceField(label="ワイド端F値(上限)", required=False, choices=F_VALUE)
    min_open_date = forms.DateTimeField(label="発売日(下限)", required=False)
    max_open_date = forms.DateTimeField(label="発売日(上限)", required=False)

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["name"].required = False
        self.fields["min_iso"].required = False
        self.fields["max_iso"].required = False
        self.fields["four_k"].required = False
        self.fields["wifi"].required = False
        self.fields["touch_panel"].required = False
        self.fields["move_panel"].required = False
        self.fields["frame"].required = False
        self.fields["maker"].required = False
        self.fields["finder"].required = False
        self.fields["bluetooth"].required = False
        self.fields["min_focus"].required = False
        self.fields["max_focus"].required = False
        self.fields["selfie"].required = False
        self.fields["waterploof"].required = False
        self.fields["gps"].required = False
        self.fields["nearest_shot"].required = False
        self.fields["anti_shake"].required = False
        self.fields["five_axis_anti_shake"].required = False
        self.fields["nearest_shot_with_macro_mode"].required = False
        self.fields["f_value_wide"].required = False
        self.fields["super_wide"].required = False
        self.fields["camera_type"].required = False

    class Meta:
        model = Camera
        fields = [
        "name",
        "min_iso",
        "max_iso",
        "four_k",
        "wifi",
        "touch_panel",
        "move_panel",
        "frame",
        "maker",
        "finder",
        "bluetooth",
        "min_focus",
        "max_focus",
        "selfie",
        "waterploof",
        "gps",
        "nearest_shot",
        "anti_shake",
        "five_axis_anti_shake",
        "nearest_shot_with_macro_mode",
        "f_value_wide",
        "super_wide",
        "camera_type",
        ]
        widgets = {
                "four_k": forms.Select(choices=BOOLEAN),
                "wifi": forms.Select(choices=BOOLEAN),
                "touch_panel": forms.Select(choices=BOOLEAN),
                "move_panel": forms.Select(choices=BOOLEAN),
                "bluetooth": forms.Select(choices=BOOLEAN),
                "selfie": forms.Select(choices=BOOLEAN),
                "waterploof": forms.Select(choices=BOOLEAN),
                "gps": forms.Select(choices=BOOLEAN),
                "anti_shake": forms.Select(choices=BOOLEAN),
                "five_axis_anti_shake": forms.Select(choices=BOOLEAN),
                "anti_shake": forms.Select(choices=BOOLEAN),
                "super_wide": forms.Select(choices=BOOLEAN),
        }
        labels = {
        "name": "機種名",
        "min_iso": "最小ISO感度",
        "max_iso": "最大ISO感度",
        "four_k": "4K動画撮影",
        "wifi": "WiFi機能",
        "touch_panel": "タッチパネル",
        "move_panel": "可動式パネル",
        "frame": "センサーサイズ",
        "maker": "メーカー",
        "finder": "ファインダー",
        "bluetooth": "Bluetooth機能",
        "min_focus": "最短焦点距離",
        "max_focus": "最長焦点距離",
        "selfie": "自撮り",
        "waterploof": "防水",
        "gps": "GPS機能",
        "anti_shake": "手ぶれ補正",
        "five_axis_anti_shake": "5軸手ぶれ補正",
        "super_wide": "超広角",
        "camera_type": "カメラタイプ",
        }
