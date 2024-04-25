from bs4 import BeautifulSoup

html_content = '''
<tr>
    <td width="20%" style="color:#333333;text-align: center;"><strong>Company</strong></td>
    <td>JINGJIN  EQUIPMENT  INC.</td>
</tr>
'''

soup = BeautifulSoup(html_content, 'html.parser')

company_tag = soup.find('td', text='Company')

company_name = company_tag.find_next_sibling('td').get_text(strip=True)

print("Company:", company_name)