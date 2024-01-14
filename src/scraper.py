from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import logging
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

logging.basicConfig(filename='../main.log', level=config['SCRAPER']['LOGGING_LEVEL'])
logger = logging.getLogger(__name__)

statistics_element = None


def extract_job_details(driver):
    global statistics_element
    job_data = {}
    try:
        # Extract job title
        try:
            title_element = driver.find_element(By.CSS_SELECTOR, 'h1.heading1[itemprop="title"]')
            job_data['Job Title'] = title_element.text
            print("Job Title:", job_data['Job Title'])
        except NoSuchElementException:
            job_data['Job Title'] = "Job title not available."

        # Extract salary (if available)
        try:
            salary_element = driver.find_element(By.CSS_SELECTOR, 'span.salary_text')
            job_data['Salary'] = salary_element.text
            print("Salary:", job_data['Salary'])
        except NoSuchElementException:
            job_data['Salary'] = "Salary information not available."

        # Extract job location
        try:
            location_element = driver.find_element(By.CSS_SELECTOR,
                                                   'div#jobad_location span[itemprop="addressLocality"]')
            job_data['Location'] = location_element.text
            print("Location:", job_data['Location'])
        except NoSuchElementException:
            job_data['Location'] = "Location information not available."

        # Extract job statistics (views)
        try:
            statistics_element = driver.find_element(By.CSS_SELECTOR, 'div.jobad_stat')
            views_element = statistics_element.find_element(By.CLASS_NAME, 'jobad_stat_value')
            job_data['Views'] = views_element.text
            print("Views:", job_data['Views'])
        except NoSuchElementException:
            job_data['Views'] = "Views information not available."

        # Extract job statistics (candidates)
        try:
            candidates_element = statistics_element.find_element(By.CLASS_NAME, 'jobad_stat_value')
            job_data['Candidates'] = candidates_element.text
            print("Candidates:", job_data['Candidates'])
        except NoSuchElementException:
            job_data['Candidates'] = "Candidates information not available."

        # Wait for the job details page to load using an element unique to the details page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'section[itemprop="description"]'))
        )

        # Extract job details
        job_details_element = driver.find_element(By.CSS_SELECTOR, 'section[itemprop="description"]')
        job_data['Job Description'] = job_details_element.text
        print("Job Description:", job_data['Job Description'])

    except NoSuchElementException as e:
        print(f"Error extracting job details: {str(e)}")

    return job_data


def scrape_all_jobs(url_jobs):
    driver = webdriver.Chrome()
    driver.get(url_jobs)

    try:
        # Wait for job listings to be present
        WebDriverWait(driver, 10).until(
            EC.presence_of_all_elements_located((By.CLASS_NAME, 'list_article_rememberable'))
        )

        # Extract all job listings
        job_listings = driver.find_elements(By.CLASS_NAME, 'list_article_rememberable')

        if not job_listings:
            raise Exception("No job listings found on the page.")

        print("Job listings found:")
        data = []
        job_urls = []
        for i, job_listing in enumerate(job_listings):
            # Extract basic information from the job listing
            job_url_element = job_listing.find_element(By.CSS_SELECTOR, 'a.list_a')
            job_url = job_url_element.get_attribute("href")
            job_urls.append(job_url)

            # Navigate to the job details page using the job URL
            print(f"Navigating to the job details page: {job_url}")
            driver.execute_script("window.open();")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(job_url)

            # Extract job details
            job_data = extract_job_details(driver)
            if job_data:
                data.append(job_data)

            # Close the tab and switch back to the main window
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            print("--------------------------------------------------------------------------------------------------")

        return data, job_urls  # Return both data and job URLs

    except Exception as e:
        print(f"Error scraping job listings: {str(e)}")
        return None, None  # Return None in case of an error

    finally:
        driver.quit()


if __name__ == "__main__":
    url = config['SCRAPER']['URL']
    scrape_all_jobs(url)
