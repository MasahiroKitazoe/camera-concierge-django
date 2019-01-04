import pandas as pd
from django.core.management.base import BaseCommand
import time
import re
import clipboard

from selenium import webdriver
from bs4 import BeautifulSoup

from cam_ranks.settings.base import (
    AMAZON_EMAIL,
    AMAZON_PASSWORD,
    RAKUTEN_EMAIL,
    RAKUTEN_PASSWORD,
)

RAKUTEN_URL_PTN = re.compile(r'<a href="([\w\d -\/:-@\[-~]+?)"')


class Command(BaseCommand):
    help = "カメラのアフィリエイトリンクを取得するカスタムコマンド"

    def handle(self, *args, **options):
        amazon_camera_links = pd.read_csv("crawler/output/camera_ec_urls.csv")
        result_df = pd.DataFrame(columns=["camera_id", "amazon_afflink"])

        for _, row in amazon_camera_links.iterrows():
            result_row = pd.Series()
            result_row["camera_id"] = row["camera_id"]

            # amazonのアフィリエイトリンクの取得
            amazon_url = row["amazon_url"]
            result_row["amazon_afflink"] = self.scrape_amazon_afflink(amazon_url)

            # 楽天のアフィリエイトリンクの取得
            rakuten_url = row["rakuten_url"]
            result_row["rakuten_afflink"] = self.scrape_rakuten_afflink(rakuten_url)

            result_df = result_df.append(result_row, ignore_index=True)

        result_df.to_csv("crawler/output/aff_links.csv")

    def scrape_amazon_afflink(self, camera_url):
        driver = webdriver.Chrome("crawler/management/commands/chromedriver")
        driver.implicitly_wait(10)

        # amazonにログイン
        driver.get("https://www.amazon.co.jp/ap/signin?openid.return_to=https%3A%2F%2Fwww.amazon.co.jp%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=jpflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&&openid.pape.max_auth_age=0")
        driver.find_element_by_css_selector("#ap_email").send_keys(AMAZON_EMAIL)
        driver.find_element_by_css_selector("#ap_password").send_keys(AMAZON_PASSWORD)
        driver.find_element_by_css_selector("#signInSubmit").click()

        # camera_urlのページからアフィリエイトリンクを取得
        driver.get(camera_url)
        driver.find_element_by_css_selector("#amzn-ss-text-link span span strong a").click()
        time.sleep(5)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        aff_link = soup.find(id="amzn-ss-text-shortlink-textarea").string

        driver.close()
        return aff_link

    def scrape_rakuten_afflink(self, camera_url):
        driver = webdriver.Chrome("crawler/management/commands/chromedriver")
        driver.implicitly_wait(10)

        # 楽天アフィリエイトにログイン
        driver.get("https://grp02.id.rakuten.co.jp/rms/nid/vc?__event=login&service_id=p11")
        driver.find_element_by_css_selector("input[type='text']").send_keys(RAKUTEN_EMAIL)
        driver.find_element_by_css_selector("input[type='password']").send_keys(RAKUTEN_PASSWORD)
        driver.find_element_by_css_selector("input[type='submit']").click()

        # アフィリエイトリンク生成
        driver.find_element_by_css_selector("#u").send_keys(camera_url)
        driver.find_element_by_css_selector("#u + .input-group-append button").click()

        # クリップボードにアフィリエイトリンクをコピー
        driver.find_element_by_css_selector("#code_copy").click()

        # アフィリエイトリンクを取得
        aff_tag = clipboard.paste()
        aff_link = self.extract_rakuten_afflink(aff_tag)

        driver.close()
        return aff_link

    def extract_rakuten_afflink(self, aff_tag):
        matched = re.match(RAKUTEN_URL_PTN, aff_tag)
        if matched:
            return matched.group(1)
        else:
            print("正規表現がマッチしませんでした。マッチしなかった文字列: {}".format(aff_tag))
            return "not detected"

