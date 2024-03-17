from bs4 import BeautifulSoup
import requests

html_text = requests.get("https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html").text;
soup = BeautifulSoup(html_text, features=  'html.parser')

print('-'*50)
print(soup.title.string)

authorName = soup.find(class_ = "byline__name")
print('By: ' + authorName.string, end = '\n\n')

paragraphs = soup.find_all(attrs={'data-component-name':'paragraph'})
for i in paragraphs: 
    if i.string != None: 
        print(i.string.strip(), end = '\n\n')


