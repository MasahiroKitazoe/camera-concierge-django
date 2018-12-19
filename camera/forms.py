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
    min_f_value_wide = forms.ChoiceField(label="ワイド端F値(下限)", required=False, choices=F_VALUE)
    max_f_value_wide = forms.ChoiceField(label="ワイド端F値(上限)", required=False, choices=F_VALUE)
    min_f_value_tele = forms.ChoiceField(label="テレ端F値(下限)", required=False, choices=F_VALUE)
    max_f_value_tele = forms.ChoiceField(label="テレ端F値(上限)", required=False, choices=F_VALUE)
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

    class Meta:
        model = Camera
        fields = [
        "name",
        "min_iso",
        "max_iso",
        "frame",
        "maker",
        "finder",
        "min_focus",
        "max_focus",
        "nearest_shot",
        "nearest_shot_with_macro_mode",
        "f_value_wide",
        "camera_type",
        ]
        labels = {
        "name": "機種名",
        "min_iso": "最小ISO感度",
        "max_iso": "最大ISO感度",
        "frame": "センサーサイズ",
        "maker": "メーカー",
        "finder": "ファインダー",
        "min_focus": "最短焦点距離",
        "max_focus": "最長焦点距離",
        "camera_type": "カメラタイプ",
        "nearest_shot": "最短撮影距離"
        }

    def __init__(self, *args, **kwargs):
        super(SearchForm, self).__init__(*args, **kwargs)
        self.fields["name"].required = False
        self.fields["min_iso"].required = False
        self.fields["max_iso"].required = False
        self.fields["frame"].required = False
        self.fields["maker"].required = False
        self.fields["finder"].required = False
        self.fields["bluetooth"].required = False
        self.fields["min_focus"].required = False
        self.fields["max_focus"].required = False
        self.fields["nearest_shot"].required = False
        self.fields["anti_shake"].required = False
        self.fields["five_axis_anti_shake"].required = False
        self.fields["nearest_shot_with_macro_mode"].required = False
        self.fields["camera_type"].required = False
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-fields'

    def clean(self):
        """ForeignKeyFieldは、レコードのidを返すようにする"""
        if self.cleaned_data.get("camera_type") is not None:
            self.cleaned_data["camera_type"] = self.cleaned_data["camera_type"].id
        if self.cleaned_data.get("frame") is not None:
            self.cleaned_data["frame"] = self.cleaned_data["frame"].id
        if self.cleaned_data.get("finder") is not None:
            self.cleaned_data["finder"] = self.cleaned_data["finder"].id
        if self.cleaned_data.get("maker") is not None:
            self.cleaned_data["maker"] = self.cleaned_data["maker"].id
