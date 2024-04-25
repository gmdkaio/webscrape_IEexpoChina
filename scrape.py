from bs4 import BeautifulSoup
import pandas as pd
import requests
import re
from links import links

def find_data(url):
    response = requests.get(url)
    html_content = response.content

    soup = BeautifulSoup(html_content, 'html.parser')
    data_dict = {}

    company_tag = soup.find('td', string='Company')
    company_name = company_tag.find_next_sibling('td').get_text(strip=True)
    data_dict['Company'] = company_name

    country_tag = soup.find('td', string='Country')
    country_name = country_tag.find_next_sibling('td').get_text(strip=True)
    data_dict['Country'] = country_name

    products_tag = soup.find('td', string='Products')
    products_name = products_tag.find_next_sibling('td').get_text(strip=True)
    data_dict['Products'] = products_name

    website_tag = soup.find('td', string='Website')
    website_name = website_tag.find_next_sibling('td').get_text(strip=True)
    data_dict['Website'] = website_name

    return data_dict

data_list = []

for url in links:
    data_dict = find_data(url)
    data_list.append(data_dict)

df_data = pd.DataFrame(data_list)

df_data.to_csv('exhibitor_data.csv', index=False)

print("Data saved to 'exhibitor_data.csv'")
