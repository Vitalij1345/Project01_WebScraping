import configparser
import logging
import time
from selenium import webdriver

def configure_logger():
    logging.basicConfig(filename='logs/main.log', level=logging.INFO,
                        format='%(asctime)s [%(levelname)s] - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

def read_config():
    config = configparser.RawConfigParser()
    config.read('config/scraper_config.ini')
    return config['DEFAULT']

def scrape_website(url, selectors, wait_time):
    driver = webdriver.Chrome()  # Use appropriate webdriver for your browser
    driver.get(url)

    # Your scraping logic using Selenium
    # For example, getting text from an element
    element = driver.find_element_by_css_selector(selectors['example_selector'])
    scraped_data = element.text
    print(scraped_data)

    time.sleep(wait_time)  # Optional: Add a delay before accessing the next page

    driver.quit()

if __name__ == "__main__":
    configure_logger()
    config = read_config()

    url = config['url']
    selectors = {
        'example_selector': config['example_selector']
    }
    wait_time = int(config['wait_time'])

    try:
        scrape_website(url, selectors, wait_time)
    except Exception as e:
        logging.error(f"Error during scraping: {str(e)}")
