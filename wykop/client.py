import hashlib
import requests
from config import Config
from string import Template

TAGS_ENTRIES_BASE_URI_TEMPLATE = Template("https://a2.wykop.pl/Tags/Entries/$tag/page/$page/appkey/$appkey")

def fetch_all_entries_for_tag(tag):
    first_page_url = TAGS_ENTRIES_BASE_URI_TEMPLATE.substitute(tag=tag, page=1, appkey=Config.APP_KEY)
    response = get_for_url(first_page_url)

    


def fetch_entries_for_tag(tag, page=1):
    u = TAGS_ENTRIES_BASE_URI_TEMPLATE.substitute(tag=tag, page=page, appkey=Config.APP_KEY)
    return get_for_url(u)


def get_for_url(url):
    h = {"apisign": generate_signature(url)}
    response = requests.get(url=url, headers=h).json()

    return response


def generate_signature(endpoint_url):
    hash_alg = hashlib.md5()
    signature_string = f'{Config.APP_SECRET}{endpoint_url}'
    return hash_alg.digest(signature_string)
