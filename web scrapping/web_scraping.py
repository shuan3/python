#pip install requests lxml bs4
# pip install lxml
# pip insall bs4

import requests
import lxml
import bs4
#check if access is allowed

results=requests.get("https://www.yorkbbs.ca/")
results=requests.get("https://www.example.com/")

results=requests.get("https://en.wikipedia.org/wiki/Avengers_(Marvel_Cinematic_Universe)/")
# print(results.text)

soup=bs4.BeautifulSoup(results.text,"lxml")
# print(soup)
print(soup.select("title")[0].getText())
print(soup.select("p")[0].getText())
