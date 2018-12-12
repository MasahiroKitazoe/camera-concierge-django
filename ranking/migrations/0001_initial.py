# Generated by Django 2.1.1 on 2018-11-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('min_price', models.IntegerField()),
                ('max_price', models.IntegerField()),
                ('min_pixel', models.IntegerField()),
                ('max_pixel', models.IntegerField()),
                ('min_iso', models.IntegerField()),
                ('max_iso', models.IntegerField()),
                ('min_continuous_shooting_performance', models.FloatField()),
                ('max_continuous_shooting_performance', models.FloatField()),
                ('min_shutter_speed', models.CharField(max_length=50)),
                ('max_shutter_speed', models.CharField(max_length=50)),
                ('min_monitor_size', models.FloatField()),
                ('max_monitor_size', models.FloatField()),
                ('min_monitor_pixel', models.FloatField()),
                ('min_num_of_shooting', models.IntegerField()),
                ('max_num_of_shooting', models.IntegerField()),
                ('four_k', models.BooleanField()),
                ('wifi', models.BooleanField()),
                ('touch_panel', models.BooleanField()),
                ('move_panel', models.BooleanField()),
                ('min_weight', models.FloatField()),
                ('max_weight', models.FloatField()),
                ('min_width', models.FloatField()),
                ('max_width', models.FloatField()),
                ('min_height', models.FloatField()),
                ('max_height', models.FloatField()),
                ('min_depth', models.FloatField()),
                ('max_depth', models.FloatField()),
                ('frame_id', models.IntegerField()),
                ('maker_id', models.IntegerField()),
                ('finder_id', models.IntegerField()),
                ('min_f_value', models.FloatField()),
                ('max_f_value', models.FloatField()),
                ('min_num_of_shooting_with_finder', models.IntegerField()),
                ('max_num_of_shooting_with_finder', models.IntegerField()),
                ('bluetooth', models.BooleanField()),
                ('min_zoom', models.FloatField()),
                ('max_zoom', models.FloatField()),
                ('min_focus', models.IntegerField()),
                ('max_focus', models.IntegerField()),
                ('selfie', models.BooleanField()),
                ('waterploof', models.BooleanField()),
                ('min_water_depth', models.IntegerField()),
                ('max_water_depth', models.IntegerField()),
                ('gps', models.BooleanField()),
                ('min_nearest_shot', models.FloatField()),
                ('max_nearest_shot', models.FloatField()),
                ('anti_shake', models.BooleanField()),
                ('five_axis_anti_shake', models.BooleanField()),
                ('min_nearest_shot_with_macro_mode', models.FloatField()),
                ('min_f_value_wide', models.FloatField()),
                ('max_f_value_wide', models.FloatField()),
                ('super_wide', models.BooleanField()),
                ('oldest_open_year', models.IntegerField()),
                ('newest_open_year', models.IntegerField()),
                ('oldest_open_month', models.IntegerField()),
                ('newest_open_month', models.IntegerField()),
                ('camera_type_id', models.IntegerField()),
            ],
        ),
    ]
