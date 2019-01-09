import math


def assign_item(item):
    """csvからのデータインポートの時に、空白値や不要表記を整形して保存可能にする"""
    if type(item) == float and math.isnan(item):
        return None
    else:
        if type(item) == str:
            item = item.replace("\u3000", " ")
        return item
