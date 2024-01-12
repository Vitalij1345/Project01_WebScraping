from scraper import scrape_all_jobs
from utils import configure_logging
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

if __name__ == "__main__":
    configure_logging(config['SCRAPER']['LOGGING_LEVEL'])
    url = config['SCRAPER']['URL']
    scrape_all_jobs(url)
