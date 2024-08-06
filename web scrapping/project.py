

import requests
import lxml
import bs4


author_list=set()
base_url="http://quotes.toscrape.com/"
res=requests.get(base_url)
soup=bs4.BeautifulSoup(res.text,"lxml")
authors=soup.select('.author')
for author in authors:
        author_list.add(author.text)

print(author_list)

quotes=[]
for quote in soup.select('.text'):
        quotes.append(quote.text)



tags=[]
for tag in soup.select('.tag-item'):
        tags.append(tag.text)
print(tags)