from bs4 import BeautifulSoup
import requests

re=requests.get('https://www.cwb.gov.tw/V8/C/L/Mountain/Mountain.html')
soup = BeautifulSoup(re.text, 'html.parser')
result=soup.title.text