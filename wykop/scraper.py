import logging
import json
from time import time
from wykop.client import fetch_tag_page


logger = logging.getLogger(__name__)


def scrape_tag_pages(tag, pages=1, output_file_name=f'output.{time()}.jsonl'):
    with open(output_file_name, 'a+') as f:
        for i in range(1, pages + 1):
            body = fetch_tag_page(tag, i)
            if body and 'data' in body and body['data']:
                logger.debug(f'Fetched {i} page of entries of tag: {tag}')
                write_entries(body['data'], f)
            if not body or 'pagination' not in body or not body['pagination']:
                break


def write_entries(entries, output_file):
    for entry in entries:
        json.dump(entry, output_file)
        output_file.write('\n')

    logger.debug(f'Written {len(entries)} entries')