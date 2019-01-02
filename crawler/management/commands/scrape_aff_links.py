from django.core.management.base import BaseCommand

import requests
from bs4 import BeautifulSoup
import pandas as pd


class Command(BaseCommand):
    help = "カメラのアフィリエイトリンクを取得するカスタムコマンド"

    def handle(self, *args, **options):
        amazon_camera_links = pd.read_csv("crawler/output/amazon_urls.csv")
        result_df = pd.DataFrame(columns=["camera_id", "amazon_afflink"])

        for _, row in amazon_camera_links.iterrows():
            result_row = pd.Series()
            url = row["amazon_url"]
            result_row["amazon_afflink"] = self.scrape_amazon_afflink(url)
            result_row["camera_id"] = row["camera_id"]

            result_df = result_df.append(result_row, ignore_index=True)

        result_df.to_csv("crawler/output/aff_links.csv")

    def scrape_amazon_afflink(self, url):
        # TODO: product apiを使う必要ありそう
        pass
