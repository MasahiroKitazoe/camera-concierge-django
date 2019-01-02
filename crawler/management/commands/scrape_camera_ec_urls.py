import requests
from bs4 import BeautifulSoup
import pandas as pd

from django.core.management.base import BaseCommand

from camera.models import Camera


class Command(BaseCommand):
    help = "Cameraモデルの機種名から、amazonの詳細ページと、楽天の検索ページのURLを取得し、csvに出力する"

    def handle(self, *args, **options):
        cameras = Camera.map_cameras()
        result_df = pd.DataFrame(columns=["camera_id", "amazon_url", "rakuten_url"])

        for _, camera in cameras.items():
            row = pd.Series()
            row["camera_id"] = camera["id"]

            keyword = camera["name"].replace(" ", "+")
            row["rakuten_url"] = "https://search.rakuten.co.jp/search/mall/" + keyword + "/"
            amazon_search_url = \
                "https://www.amazon.co.jp/s/ref=nb_sb_noss_2?__mk_ja_JP=カタカナ&url=search-alias%3Daps&field-keywords={}".format(keyword)

            retry_count = 0
            while retry_count <= 10:
                res = requests.get(amazon_search_url)
                print(res.status_code)
                if res.status_code == 200:
                    break

            soup = BeautifulSoup(res.text, "html.parser")
            rank1_product = soup.find(id="result_0")
            print(camera["name"])

            try:
                price_text = rank1_product.find(class_="a-text-bold").text
                price = int(price_text.replace("￥ ", "").replace(",", ""))
            except:
                print("検索結果が見つからなかった")
                row["amazon_url"] = "not detected"
                result_df = result_df.append(row, ignore_index=True)
                continue

            # カメラの値段と50%以上価格に差がある場合、urlは保存しない
            if price >= int(camera["price"]) * 1.5 or price <= int(camera["price"]) * 0.5:
                print("値段離れすぎ。狙いのURLじゃない説")
                row["amazon_url"] = "not detected"
                result_df = result_df.append(row, ignore_index=True)
                continue

            product_url = rank1_product.find("a").get("href")
            print(product_url)
            row["amazon_url"] = product_url
            result_df = result_df.append(row, ignore_index=True)

        result_df.to_csv("crawler/output/camera_ec_urls.csv")