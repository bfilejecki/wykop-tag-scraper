import logging
import argparse
from time import time
from app import scraper


def main():
    parser = configure_argparser()
    logger = configure_logging()

    logger.debug('Started fetching')
    start = time()
    scraper.scrape_tag('api')
    end = time()
    logger.debug(f'Finished fetching, took: {(end - start):.3f} seconds')


def configure_logging():
    logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()]
    )

    return logging.getLogger(__name__)


def configure_argparser():
    parser = argparse.ArgumentParser(prog="Wykop tag scraper")
    parser.add_argument()

    return parser


if __name__ == '__main__':
    main()
