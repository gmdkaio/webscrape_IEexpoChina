import requests
from bs4 import BeautifulSoup


url = "https://www.ie-expo.com/exhibitors/exhibitor2-5188.html"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

def find_data():
  company_tag = soup.find('td', text='Company')

  company_name = company_tag.find_next_sibling('td').get_text(strip=True)

  print("Company:", company_name)