import requests
from bs4 import BeautifulSoup
import pandas as pd

books = []

for i in range(1,51):
    url = f"http://books.toscrape.com/catalogue/category/books_1/page-{i}.html"
    response = requests.get(url)
    #print(response)
    soup = BeautifulSoup(response.text, 'lxml')
    #print(soup)
    ol = soup.find('ol')
    articles = ol.find_all('article', class_ = 'product_pod')
    

    for article in articles:
        image = article.find('img')
        title = image.attrs['alt']
        star = article.find('p')
        star = star['class'][1]
        price = article.find('p', class_= 'price_color').text
        books.append([title, price, star])
    
df = pd.DataFrame(books, columns=['Title', 'Price', 'Star'])
df.to_csv('books.csv')