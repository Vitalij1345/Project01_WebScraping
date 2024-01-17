# WEB SCRAPING PROJECT

This project is a web scraping tool that extracts job listings from [cvbankas.lt](https://www.cvbankas.lt/?padalinys%5B%5D=88&keyw=). 
It utilizes Selenium for web automation and CSVWriter to save the scraped data to a CSV file.

## FEATURES

- Scrape job listings from [**cvbankas.lt**](https://www.cvbankas.lt/?padalinys%5B%5D=88&keyw=)
- Navigate through job details pages
- Save scraped data to a CSV file with job URLs
- Custom Configuration: Easily configure the scraping parameters by updating `config.ini` and `csv_writer.py`. Modify 
the URL or adjust the wait time according to your preferences. 
- Flexible Usage: Adapt the web scraping process by updating `config.ini` and `csv_writer.py` with your specific 
requirements. Customize the script to suit different filters on the [**cvbankas.lt**](https://www.cvbankas.lt/?padalinys%%5B%%5D=88&keyw=) website.

## CODE STRUCTURE

### Project01_WebScraping

* [src](#src)
  * [config.ini](#configini)
  * [csv_writer.py](#csv_writerpy)
  * [output.csv](#outputcsv)
  * [main.py](#mainpy)
  * [scraper.py](#scraperpy)
  * [utils.py](#utilspy)
* [.gitignore](#gitignore)
* [main.log](#mainlog)
* [README.md](#readmemd)
* [requirements.txt](#requirementstxt)

### src

#### [config.ini](src/config.ini)
Configuration file with parameters

#### [csv_writer.py](src/csv_writer.py)
Script to write scraped data to CSV

#### [output.csv](src/output.csv)
Script to write scraped data to CSV

#### [main.py](src/main.py)
Main script for executing the web scraping

#### [scraper.py](src/scraper.py)
Main script for web scraping

#### [utils.py](src/utils.py)
Utility functions (e.g., logging configuration)

#### [.gitignore](.gitignore)
File to specify files/folders to be ignored by version control

#### [main.log](main.log)
Log file for storing error logs

#### [README.md](README.md)
Project documentation

#### [requirements.txt](requirements.txt)
File listing project dependencies

## SCRIPT

- `main.py`: This script serves as an entry point for the project. Running main.py configures logging using functions 
from utils.py and then calls the scrape_all_jobs function from scraper.py, executing the web scraping process.


- `csv_writer.py`: This script coordinates web scraping, data extraction, and writing results to a CSV file. When 
run, it initiates the web scraping process, extracts data from job listings, and saves the data with job URLs to output.csv.


## INSTALLATION

### Requirements

- Python 3.12.0
- Requirements listed in [requirements.txt](requirements.txt)
- Web Browser Driver: Selenium requires a web browser driver. This project uses the Chrome browser, so make sure to 
have the ChromeDriver version **71.0.3542.0** executable compatible with your Chrome browser version.

### Configuration

If you want to scrape website [cvbankas.lt](https://www.cvbankas.lt/?padalinys%%5B%%5D=88&keyw=) with different filters 
make sure to follow instructions.
- Update the [config.ini](src/config.ini) file to customize the URL, make sure to add extra symbol "%" after or before 
symbol "%" for _example_: **_UNEDITED_** URL = https://www.cvbankas.lt/?padalinys%5B%5D=85&keyw= 
**_EDITED_** URL = https://www.cvbankas.lt/?padalinys%%5B%%5D=85&keyw=.
- Update the [csv_writer.py](src/csv_writer.py) file to customize the URL, just copy URL of the website and change it with 
current. 

## Usage

1. Clone the repository.
2. Install dependencies using `pip install -r requirements.txt`.
3. Update [config.ini](src/config.ini) with your desired configuration **if needed**.
4. Update [csv_writer.py](src/csv_writer.py) with your desired configuration **if needed**. 
5. Run `main.py` to start the web scraping process. It initializes the web scraping but does not create the CSV file.
6. Run `csv_writer.py` to generate the CSV file with extracted data. 