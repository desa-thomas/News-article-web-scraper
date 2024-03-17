from bs4 import BeautifulSoup
import requests

def scrapeWebsite (url): 
    response = requests.get(url)
    if response.status_code == 200: 
        soup = BeautifulSoup(response.text, 'html.parser')
        title = soup.title.string
        authorName = soup.find(class_ = "byline__name").string
        paragraphs = soup.find_all(attrs={'data-component-name':'paragraph'})
        content = ''

        for i in paragraphs: 
            if i.string != None: 
                content += (i.string.strip() + '\n\n')

        return title, authorName, content
    
    else: 
        print("Failed to fetch request")
        return None, None, None
    

url = "https://edition.cnn.com/travel/article/scenic-airport-landings-2020/index.html"; 
title, authorname, content = scrapeWebsite(url)
print('-'*50)
if(title != None and authorname != None and content != None): 
    print(title)
    print("By:" + authorname + '\n') 
    print(content)



