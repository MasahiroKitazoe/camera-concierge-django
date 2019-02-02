from django.utils import timezone
from django.core.management.base import BaseCommand

from crawler.scraper import HashTagScraper
from camera.models import HashTag


class Command(BaseCommand):
    help = "カメラのインスタハッシュタグ数を取得し、csvに出力する。毎週土曜日だけの定期実行"

    def handle(self, *args, **options):
        if timezone.localdate().weekday() == 5:
            HashTagScraper.scrape_insta_hashtags()
            HashTag.import_csv("crawler/output/posted_count_insta.csv")
