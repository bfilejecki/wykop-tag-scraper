import logging
import argparse
import time
from app import scraper


def main():
    parser = configure_argparser()
    args = parser.parse_args()
    logger = configure_logging(args.debug)

    logger.debug("Started fetching")
    start = time.perf_counter()
    if args.pages is not None:
        scraper.scrape_tag_pages(args.tag, args.output, args.pages)
    else: 
        scraper.scrape_tag(args.tag, args.output)
    end = time.perf_counter()
    logger.debug(f"Finished fetching, took: {(end - start):.3f} seconds")


def configure_logging(debug):
    level = logging.DEBUG if debug else logging.ERROR

    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[logging.StreamHandler()],
    )

    return logging.getLogger(__name__)


def configure_argparser():
    parser = argparse.ArgumentParser(prog="Wykop tag scraper")

    parser.add_argument("tag", help="tag name to scrape")
    parser.add_argument("-o", "--output", help="output file name", default=f"output.{time.time()}.jsonl")
    parser.add_argument("-d", "--debug", help="turn debug logs", action="store_true")
    parser.add_argument("-p", "--pages", help="number of pages to return", type=int)

    return parser


if __name__ == "__main__":
    main()
