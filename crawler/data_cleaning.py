import pandas as pd
import re

from camera.models import Camera
from crawler.consts import EC_DOMAINS, DOMAIN_PTN, EC_WORDS


def clean_reviews(path):
    """
    CSVファイル内のデータから、カメラのレビュー以外のノイズを取り除くメソッド
    CSVファイルは引数のpathで指定されたもので、カラムはtitle, body, url, camera_idの想定
    :return: クリーニングしたcsvファイルを./outputフォルダ内に格納する
    """
    cameras = Camera.map_cameras()
    review_df = pd.read_csv(path, index_col=0)
    cleaned_df = pd.DataFrame(columns=["title", "body", "url", "camera_id"])
    excluded_df = pd.DataFrame(columns=["title", "body", "url", "camera_id"])

    for index, row in review_df.iterrows():
        # カメラの名前がタイトルに含まれていないレコードを見つけ出す
        if not is_camera_name_included(row.title, cameras[row.camera_id]):
            excluded_df = excluded_df.append(row, ignore_index=True)
            continue

        # ECのドメインのレコードを見つけ出す
        if is_ec_domain(row.url):
            excluded_df = excluded_df.append(row, ignore_index=True)
            continue

        # EC特有のワードがタイトルに入っているレコードを見つけだす
        if ec_word_included(row.title):
            excluded_df = excluded_df.append(row, ignore_index=True)
            continue

        # ここまできたレコードはカメラのレビュー記事と認める
        cleaned_df = cleaned_df.append(row, ignore_index=True)

    excluded_df.to_csv("crawler/output/excluded.csv")
    cleaned_df.to_csv("crawler/output/cleaned_review.csv")


def is_camera_name_included(title, camera):
    """
    カメラの機種名がtitleに含まれているか判定するメソッド
    機種名は空白区切りで情報が入っているので、分けてどちらかが含まれていればTrueとする
    例) "サイバーショット RX100M6"は"サイバーショット"か"RX100M6"のどちらかが入っていればOK
    """
    # サイバーショットシリーズの型番の頭文字"DSC"とその後ろの型番文字列を空白区切りにする
    if "DSC" in camera["name"]:
        camera["name"] = split_dsc(camera["name"])

    camera_names = camera["name"].split(" ")
    for name in camera_names:
        if name in title:
            return True
    return False


def split_dsc(name):
    return name.replace("DSC-", "DSC ")


def is_ec_domain(url):
    # ドメイン部分を正規表現で抜き出す
    matched = re.search(DOMAIN_PTN, url)
    if matched:
        domain = matched.group(1)
    else:
        raise ValueError("URLからドメインを抽出できませんでした。正規表現を確認してください。失敗したURL:{}".format(url))

    if domain in EC_DOMAINS:
        return True
    else:
        return False


def ec_word_included(title):
    for ec_word in EC_WORDS:
        if ec_word in title:
            return True
    return False
