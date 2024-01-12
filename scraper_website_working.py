from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException


def extract_job_details(driver):
    global statistics_element
    try:
        # Extract salary (if available)
        try:
            salary_element = driver.find_element(By.CSS_SELECTOR, 'span.salary_text')
            salary = salary_element.text
            print("Salary:", salary)
        except NoSuchElementException:
            print("Salary information not available.")

        # Extract job location
        try:
            location_element = driver.find_element(By.CSS_SELECTOR, 'div#jobad_location span[itemprop="addressLocality"]')
            location = location_element.text
            print("Location:", location)
        except NoSuchElementException:
            print("Location information not available.")

        # Extract job statistics (views)
        try:
            statistics_element = driver.find_element(By.CSS_SELECTOR, 'div.jobad_stat')
            views_element = statistics_element.find_element(By.CLASS_NAME, 'jobad_stat_value')
            views = views_element.text
            print("Views:", views)
        except NoSuchElementException:
            print("Views information not available.")

        # Extract job statistics (candidates)
        try:
            candidates_element = statistics_element.find_element(By.CLASS_NAME, 'jobad_stat_value')
            candidates = candidates_element.text
            print("Candidates:", candidates)
        except NoSuchElementException:
            print("Candidates information not available.")

        # Wait for the job details page to load using an element unique to the details page
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'section[itemprop="description"]'))
        )

        # Extract job details
        job_details_element = driver.find_element(By.CSS_SELECTOR, 'section[itemprop="description"]')
        job_description = job_details_element.text
        print("Job Description:", job_description)

    except NoSuchElementException as e:
        print(f"Error extracting job details: {str(e)}")


def scrape_all_jobs(url):
    driver = webdriver.Chrome()
    driver.get(url)

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
        for i, job_listing in enumerate(job_listings):
            # Extract basic information from the job listing
            job_url_element = job_listing.find_element(By.CSS_SELECTOR, 'a.list_a')
            job_url = job_url_element.get_attribute("href")

            # Navigate to the job details page using the job URL
            print(f"Navigating to the job details page: {job_url}")
            driver.execute_script("window.open();")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(job_url)

            # Extract job details
            extract_job_details(driver)

            # Close the tab and switch back to the main window
            driver.close()
            driver.switch_to.window(driver.window_handles[0])
            print("--------------------------------------------------------------------------------------------------")

    except Exception as e:
        print(f"Error scraping job listings: {str(e)}")

    finally:
        driver.quit()


if __name__ == "__main__":
    url = "https://www.cvbankas.lt/?padalinys%5B%5D=88&keyw="
    scrape_all_jobs(url)
