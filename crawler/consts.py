import re

EC_DOMAINS = [
    "www.yodobashi.com",
    "www.biccamera.com",
    "www.edion.com",
    "joshinweb.jp",
    "www.ksdenki.com",
    "www.kojima.net",
    "www.yamada-denkiweb.com",
    "www.amazon.co.jp",
    "www.rakuten.co.jp",
    "online.nojima.co.jp",
    "product.rakuten.co.jp",
    "shopping.yahoo.co.jp",
    "www.askul.co.jp",
    "www.tanomail.com",
    "www.mapcamera.com",
    "www.kitamura.jp",
]

EC_WORDS = [
    "通販",
    "送料無料",
    "楽天市場",
    "ヤフオク",
    "中古",
    "新品",
    "価格.com",
    "保証付",
]

DOMAIN_PTN = re.compile(r"https?:\/\/([\w\.-]+)\/")
