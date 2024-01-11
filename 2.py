from selenium import webdriver
from selenium.webdriver.common.by import By

url = "https://www.cvbankas.lt/?padalinys%5B%5D=88&keyw="

# Set up the Chrome WebDriver (you need to have chromedriver installed)
driver = webdriver.Chrome()

# Open the URL
driver.get(url)

# Extract the HTML content after the dynamic content has loaded
html_content = driver.page_source

# Close the WebDriver
driver.quit()

# Now you can process the HTML content using BeautifulSoup or other methods

print(html_content)

# html_content = response.text

with open("output.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("HTML content has been saved to output.html")