import hashlib
import requests
from config import Config
from string import Template

TAGS_ENTRIES_BASE_URI_TEMPLATE = Template("https://a2.wykop.pl/Tags/Entries/page/$page/$tag/appkey/$appkey")


def get_entries_for_tag(tag, page=1):
    u = TAGS_ENTRIES_BASE_URI_TEMPLATE.substitute(tag=tag, page=page, appkey=Config.APP_KEY)
    h = {"apisign": generate_signature(u)}
    response = requests.get(url=u, headers=h).json()

    return response


def generate_signature(endpoint_url):
    hash_alg = hashlib.md5()
    signature_string = f'{Config.APP_SECRET}{endpoint_url}'
    return hash_alg.digest(signature_string)
