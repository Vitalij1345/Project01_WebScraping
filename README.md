# Web Scraping Project

This project is a web scraping tool that extracts job listings from [cvbankas.lt](https://www.cvbankas.lt/?padalinys%5B%5D=88&keyw=). 
It utilizes Selenium for web automation and CSVWriter to save the scraped data to a CSV file.

# Features

- Scrape job listings from [cvbankas.lt](https://www.cvbankas.lt/?padalinys%5B%5D=88&keyw=)
- Navigate through job details pages
- Save scraped data to a CSV file with job URLs

# Code structure:

## Project01_WebScraping

* [src](#src)
  * [scraper.py](#scraperpy)
  * [csv_writer.py](#csv_writerpy)
  * [utils.py](#utilspy)
  * [config.ini](#configini)
* [tests](#tests)
* [requirements.txt](#requirementstxt)
* [main.log](#mainlog)
* [README.md](#readmemd)
* [.gitignore](#gitignore)
* [backup_files](#backup_files)

## src

### [scraper.py](src/scraper.py)
Main script for web scraping

### [csv_writer.py](src/csv_writer.py)
Script to write scraped data to CSV

### [utils.py](src/utils.py)
Utility functions (e.g., logging configuration)

### [config.ini](src/config.ini)
Configuration file with parameters

## [tests](tests)
Folder containing test files

### [requirements.txt](requirements.txt)
File listing project dependencies

### [main.log](main.log)
Log file for storing error logs

### [README.md](README.md)
Project documentation

### [.gitignore](.gitignore)
File to specify files/folders to be ignored by version control

## [backup_files](backup_files)
Folder to store backup files

# Script

- main.py: This script is intended to serve as an entry point for project. When you run main.py, it will configure 
logging using the functions from utils.py and then call the scrape_all_jobs function from scraper.py. 
This, in turn, will execute the web scraping logic.
So, by running main.py, you should achieve the entire process, including logging setup and web scraping.

- csv_writer.py: This script, as provided in the context of this conversation, is responsible for coordinating the 
web scraping, data extraction, and writing the results to a CSV file.
When you run csv_writer.py, it initiates the web scraping process, extracts data from job listings, and then saves 
the data along with job URLs to the output.csv file.