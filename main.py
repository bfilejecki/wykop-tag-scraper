import logging
from time import time
from wykop import scraper


def main():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()]
    )

    logger = logging.getLogger(__name__)

    logger.debug('Started fetching')
    start = time()
    scraper.scrape_tag_pages('api')
    end = time()
    logger.debug(f'Finished fetching, took: {(end - start):.3f} seconds')


if __name__ == '__main__':
    main()
