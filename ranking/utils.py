import math


def assign_item(item, field=None):
    """csvからのデータインポートの時に、空白値や不要表記を整形して保存可能にする"""
    if type(item) == float and math.isnan(item):
        # date系だったらNoneを返す
        if field == "min_open_date" or field == "max_open_date":
            return None
        return 0
    else:
        if type(item) == str:
            item = item.replace("\u3000", " ")
        return item
