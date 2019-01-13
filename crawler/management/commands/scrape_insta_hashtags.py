import pandas as pd
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

from camera.models import Camera

# メーカー名やブランド名など、邪魔になる単語に含まれるであろうwords
# このリストの文字列が含まれている単語自体を取り除く想定
STOP_WORDS = [
    'サイバーショット',
    'COOLPIX',
    'FUJIFILM',
    'OLYMPUS',
    'PowerShot',
    'FinePix',
    'LUMIX',
    'EXILIM',
    'RICOH',
    'キット',
    'ソニー',
    'SONY',
    'RICOH',
    'リコー',
    'オリンパス',
    'パナソニック',
    'ボディ',
    'Canon',
    'Nikon',
    'キャノン',
    'ニコン',
    'ILCE',
    'ILCA',
]

# 型番の頭文字など、邪魔だが同じ単語内に必要な文字も含まれている可能性の高いwords
# このリストの文字列は、replaceメソッドで取り除く想定
REPLACE_WORDS = [
    'DSC-',
    'Tough',
    'DC-',
    'DMC-',
    'HIGH SPEED EXILIM',
    '-',
    "ボディ",
    "[ブラック]",

]


class Command(BaseCommand):
    help = "カメラのインスタハッシュタグ数を取得し、csvに出力する"

    def handle(self, *args, **options):
        hashtags_before_df = pd.read_csv("crawler/output/posted_count_insta.csv")
        result_df = pd.DataFrame(columns=["camera_id", "hashtag_name", "hashtag_count", "hashtag_increase"])

        cameras = Camera.map_cameras()
        for camera_id, camera in cameras.items():
            posted_count_series = pd.Series()
            shaped_camera_name = self.shape_camera_name(camera["name"])
            posted_count = self.scrape_hashtag_count(shaped_camera_name)
            posted_count_series["camera_id"] = camera_id
            posted_count_series["hashtag_name"] = shaped_camera_name
            posted_count_series["hashtag_count"] = posted_count
            posted_count_series["hashtag_increase"] = int(posted_count) - int(hashtags_before_df.iat[camera_id - 1, 3])
            result_df = result_df.append(posted_count_series, ignore_index=True)

        result_df.to_csv("crawler/output/posted_count_insta.csv")

    def shape_camera_name(self, camera_name):
        """
        ハッシュタグ検索に適した形に機種名を加工して返すメソッド
        :param camera_name: カメラの機種名
        :return: 加工ずみのカメラの機種名(str型)
        """
        #  STOP_WORDSが含まれる部分をで取り除く
        split_names = camera_name.split(" ")
        for name in split_names:
            for stop_word in STOP_WORDS:
                if stop_word in name:
                    split_names.remove(name)
                    break

        camera_name = "".join(split_names)

        # REPLACE_WORDSを取り除く
        for replace_word in REPLACE_WORDS:
            if replace_word in camera_name:
                camera_name = camera_name.replace(replace_word, "")

        return camera_name

    def scrape_hashtag_count(self, camera_name):
        """
        整形済みの機種名のハッシュタグ数を取得する
        :param camera_name: shape_camera_nameメソッドで整形された機種名を想定
        :return: ハッシュタグ投稿数
        """
        driver = webdriver.Chrome("crawler/management/commands/chromedriver")
        driver.get('https://www.instagram.com/explore/tags/' + camera_name + '/?hl=ja')

        # 読み込み待ち
        try:
            WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "g47SY"))
            )
        except TimeoutException:
            driver.quit()
            return "0"

        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")

        try:
            posted_count = soup.find(class_='g47SY').string
        except AttributeError:
            posted_count = "0"

        if ',' in posted_count:
            posted_count = posted_count.replace(',', '')

        driver.quit()

        return posted_count
