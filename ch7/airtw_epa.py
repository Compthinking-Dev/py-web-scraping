import requests
from bs4 import BeautifulSoup


if __name__ == '__main__':
    URL = 'https://airtw.epa.gov.tw/CHT/Query/Month_Avg.aspx'
    resp = requests.get(URL)
    soup = BeautifulSoup(resp.text, 'html.parser')
    view_state = soup.find(id='__VIEWSTATE')['value']
    event_validation = soup.find(id='__EVENTVALIDATION')['value']
    viewstate_generator = soup.find(id='__VIEWSTATEGENERATOR')['value']
    form_data = {
        '__VIEWSTATE': view_state,
        '__VIEWSTATEGENERATOR': viewstate_generator,
        '__EVENTVALIDATION': event_validation,
        'ctl00$CPH_Content$ddl_Site': '17',
        'ctl00$CPH_Content$ddlQYear': '2022',
        'ctl00$CPH_Content$btnQuery': '查詢'
    }
    resp = requests.post(URL, data=form_data)
    soup = BeautifulSoup(resp.text, 'html.parser')
    for row in soup.find_all('tr'):
        print([content for content in row.stripped_strings])
