import requests
from bs4 import BeautifulSoup

news_url = "https://www.livemint.com/latest-news"

response = requests.get(news_url)

soup = BeautifulSoup(response.text,'html.parser')
news_headlines = soup.find_all('h2')

print('Latests headline:')
for index , news_headlines in enumerate(news_headlines , 1):
    print(f"{index} {news_headlines.text.strip()}")
    news_link = news_headlines.find('a')
    if news_link and 'href' in news_link.attrs:
        link = news_link['href']
        if link.startswith('/'):
            link= f"https://www.livemint.com{link}"

    print(f" news link: {link}\n")