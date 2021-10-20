from bs4 import BeautifulSoup
import requests
import pandas as pd
import openpyxl
webpage = requests.get('https://www.banggood.in/search/jumpsuits.html?from=nav&ab_version=1')

sp = BeautifulSoup(webpage.content, 'html.parser')

# print hole content in webpage
#print(sp)
#print text only of webpage
#print(sp.text)

title = sp.find_all('a', 'title')
sellprice = sp.find_all('span', 'price-box')
review = sp.find_all('a','review')

tittleloop = [titles.text for titles in title]
sellpriceloop = [sells.text for sells in sellprice]
reviewloop = [reviews.text for reviews in review]

print(sellpriceloop)


data = {
    'Name_of_Product':tittleloop,
    'selling_price':sellpriceloop,
    'review': reviewloop
}

# print(len(tittleloop))
# print(len(reviewloop))
# print(len(sellpriceloop))

df = pd.DataFrame(data,columns=['Name_of_Product',
                                'selling_price',
                                'review'])


print(df)

df = pd.DataFrame(data,columns=['Name_of_Product',
                            'review'])

df2= pd.DataFrame(data,columns=['selling_price'])

sellprice = df2['selling_price']

df = df.join(sellprice)

print(df)

df.to_excel('E:/meanstack/data.xlsx',index=False)