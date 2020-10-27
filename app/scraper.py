import logging
import json
from time import time
from app.client import fetch_tag_page, fetch_next_page


logger = logging.getLogger(__name__)


def scrape_tag_pages(tag, pages=1, output_file_name=f'output.{time()}.jsonl'):
    with open(output_file_name, 'a+') as f:
        for i in range(1, pages + 1):
            api_response = fetch_tag_page(tag, i)
            if api_response.get_data():
                logger.debug(f'Fetched {i} page of entries of tag: {tag}')
                write_entries(api_response.get_data(), f)
            elif api_response.get_error_msg():
                logger.error(f'Api returned error: {api_response.get_error_msg()}')
                break
            else:
                logger.error('Unknown error')
                break


def scrape_tag(tag, output_file_name=f'output.{time()}.jsonl'):
    with open(output_file_name, 'a+') as f:
        api_response = fetch_tag_page(tag, 1)
        data = api_response.get_data()
        error_msg = api_response.get_error_msg()
        next_page = api_response.get_next_page()
        page_num = 1

        while data:
            logger.debug(f'Fetched {page_num} page of entries of tag: {tag}')
            write_entries(data, f)
            if next_page:
                api_response = fetch_next_page(next_page)
                data = api_response.get_data()
                error_msg = api_response.get_error_msg()
                next_page = api_response.get_next_page()
                page_num += 1

        if error_msg:
            logger.error(f'Api returned error: {error_msg}')


def write_entries(entries, output_file):
    for entry in entries:
        json.dump(entry, output_file)
        output_file.write('\n')

    logger.debug(f'Written {len(entries)} entries')
