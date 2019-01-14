from django import forms
from django.forms import ModelForm

from .models import Camera
from .consts import SHUTTER_SPEED, F_VALUE, BOOLEAN, CAMERA_TYPE_CHOICES, FINDER_CHOICES, FRAME_CHOICES, MAKER_CHOICES


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
    min_f_value_wide = forms.ChoiceField(label="ワイド端F値(下限)", required=False, choices=F_VALUE)
    max_f_value_wide = forms.ChoiceField(label="ワイド端F値(上限)", required=False, choices=F_VALUE)
    min_f_value_tele = forms.ChoiceField(label="テレ端F値(下限)", required=False, choices=F_VALUE)
    max_f_value_tele = forms.ChoiceField(label="テレ端F値(上限)", required=False, choices=F_VALUE)
    min_shooting_num_with_finder = \
      forms.IntegerField(label="ファインダー使用時の撮影可能枚数(下限)", required=False)
    max_shooting_num_with_finder = \
      forms.IntegerField(label="ファインダー使用時の撮影可能枚数(上限)", required=False)
    min_zoom = forms.IntegerField(label="ズーム(下限)", required=False)
    max_zoom = forms.IntegerField(label="ズーム(上限)", required=False)
    min_nearest_shot = forms.FloatField(label="最短撮影距離(下限)", required=False)
    max_nearest_shot = forms.FloatField(label="最短撮影距離(上限)", required=False)
    min_nearest_shot_with_macro_mode = \
      forms.FloatField(label="マクロモード時最短撮影距離(下限)", required=False)
    max_nearest_shot_with_macro_mode = \
      forms.FloatField(label="マクロモード時最短撮影距離(上限)", required=False)
    min_open_date = forms.DateField(label="発売日(下限)", required=False)
    max_open_date = forms.DateField(label="発売日(上限)", required=False)
    four_k = forms.ChoiceField(label="4K動画撮影", required=False, choices=BOOLEAN)
    wifi = forms.ChoiceField(label="Wifi機能", required=False, choices=BOOLEAN)
    touch_panel = forms.ChoiceField(label="タッチパネル", required=False, choices=BOOLEAN)
    move_panel = forms.ChoiceField(label="可動式モニター", required=False, choices=BOOLEAN)
    bluetooth = forms.ChoiceField(label="Bluetooth", required=False, choices=BOOLEAN)
    selfie = forms.ChoiceField(label="自撮り", required=False, choices=BOOLEAN)
    waterploof = forms.ChoiceField(label="防水", required=False, choices=BOOLEAN)
    gps = forms.ChoiceField(label="GPS", required=False, choices=BOOLEAN)
    anti_shake = forms.ChoiceField(label="手ぶれ補正", required=False, choices=BOOLEAN)
    five_axis_anti_shake = forms.ChoiceField(label="ボディ内5軸手ぶれ補正", required=False, choices=BOOLEAN)
    super_wide = forms.ChoiceField(label="超広角", required=False, choices=BOOLEAN)
    camera_type_id = forms.ChoiceField(label="カメラタイプ", required=False, choices=CAMERA_TYPE_CHOICES)
    frame_id = forms.ChoiceField(label="センサーサイズ", required=False, choices=FRAME_CHOICES)
    finder_id = forms.ChoiceField(label="ファインダー", required=False, choices=FINDER_CHOICES)
    maker_id = forms.ChoiceField(label="メーカー", required=False, choices=MAKER_CHOICES)

    class Meta:
        model = Camera
        fields = [
        "name",
        "min_iso",
        "max_iso",
        "min_focus",
        "max_focus",
        ]
        labels = {
        "name": "機種名",
        "min_iso": "最小ISO感度",
        "max_iso": "最大ISO感度",
        "min_focus": "最短焦点距離",
        "max_focus": "最長焦点距離",
        }

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["name"].required = False
        self.fields["min_iso"].required = False
        self.fields["max_iso"].required = False
        self.fields["bluetooth"].required = False
        self.fields["min_focus"].required = False
        self.fields["max_focus"].required = False
        self.fields["anti_shake"].required = False
        self.fields["five_axis_anti_shake"].required = False
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-fields'

    def clean_camera_type_id(self):
        return int(self.cleaned_data["camera_type_id"]) if self.cleaned_data["camera_type_id"] else None

    def clean_frame_id(self):
        return int(self.cleaned_data["frame_id"]) if self.cleaned_data["frame_id"] else None

    def clean_finder_id(self):
        return int(self.cleaned_data["finder_id"]) if self.cleaned_data["finder_id"] else None

    def clean_maker_id(self):
        return int(self.cleaned_data["maker_id"]) if self.cleaned_data["maker_id"] else None

    def clean_wifi(self):
        return bool(self.cleaned_data["wifi"]) if self.cleaned_data["wifi"] else None

    def clean_four_k(self):
        return bool(self.cleaned_data["four_k"]) if self.cleaned_data["four_k"] else None

    def clean_touch_panel(self):
        return bool(self.cleaned_data["touch_panel"]) if self.cleaned_data["touch_panel"] else None

    def clean_move_panel(self):
        return bool(self.cleaned_data["move_panel"]) if self.cleaned_data["move_panel"] else None

    def clean_bluetooth(self):
        return bool(self.cleaned_data["bluetooth"]) if self.cleaned_data["bluetooth"] else None

    def clean_selfie(self):
        return bool(self.cleaned_data["selfie"]) if self.cleaned_data["selfie"] else None

    def clean_waterploof(self):
        return bool(self.cleaned_data["waterploof"]) if self.cleaned_data["waterploof"] else None

    def clean_gps(self):
        return bool(self.cleaned_data["gps"]) if self.cleaned_data["gps"] else None

    def clean_anti_shake(self):
        return bool(self.cleaned_data["anti_shake"]) if self.cleaned_data["anti_shake"] else None

    def clean_five_axis_anti_shake(self):
        return bool(self.cleaned_data["five_axis_anti_shake"]) if self.cleaned_data["five_axis_anti_shake"] else None

    def clean_super_wide(self):
        return bool(self.cleaned_data["super_wide"]) if self.cleaned_data["super_wide"] else None
