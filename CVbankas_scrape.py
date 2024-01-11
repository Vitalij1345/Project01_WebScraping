import requests
from bs4 import BeautifulSoup

url = "https://www.cvbankas.lt/?padalinys%5B%5D=88&keyw="

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract the information you need
    # Modify this part according to the structure of the website
    job_listings = soup.find_all('div', class_='your-target-class')

    for job_listing in job_listings:
        # Extract relevant information from each job listing
        # Example:
        job_title = job_listing.find('span', class_='job-title').text.strip()
        company_name = job_listing.find('span', class_='company-name').text.strip()
        # Add more fields as needed

        # Print or store the extracted information
        print(f"Job Title: {job_title}")
        print(f"Company Name: {company_name}")
        print("=" * 50)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")


url = "https://www.cvbankas.lt/?padalinys%5B%5D=88&keyw="

# Send a GET request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Extract the HTML content
    html_content = response.text

    # Print or process the HTML content
    print(html_content)

    with open('webpage.html', 'w', encoding='utf-8') as file:
        file.write(html_content)

else:
    print(f"Failed to retrieve the page. Status code: {response.status_code}")
