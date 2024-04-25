from bs4 import BeautifulSoup
import pandas as pd
import requests
import re

def filter_and_transform_links(links):
    transformed_links = []
    for link in links:
        if re.search(r'exhibitor2-\d+\.html', link):
            transformed_link = 'https://www.ie-expo.com/exhibitors/' + link
            transformed_links.append(transformed_link)
    return transformed_links

base_url = "https://www.ie-expo.com/exhibitors/Exhibitorslist.html?page={}"

urls = [base_url.format(page) for page in range(1, 62)]
all_links = []

for url in urls:
    response = requests.get(url)
    html_content = response.content
    soup = BeautifulSoup(html_content, 'html.parser')

    a_tags = soup.find_all('a')
    
    href_links = [a.get('href') for a in a_tags]

    transformed_links = filter_and_transform_links(href_links)
    
    all_links.extend(transformed_links)

df = pd.DataFrame({'Links': all_links})

df.to_csv('exhibitor_links.csv', index=False)

print("Links saved to 'exhibitor_links.csv'")
