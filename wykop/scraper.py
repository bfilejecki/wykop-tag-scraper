import logging
from time import time
from client import fetch_tag_page


logger = logging.getLogger(__name__)


def scrape_tag_pages(tag, pages=1, output_file=f'output.{time()}.json'):

    pass