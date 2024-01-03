import requests
import bs4
lst1=[]#names
lst2=[]#prices
lst3=[]#ratiings and reviews
lst4=[]#description
headers= {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
res=requests.get('https://www.flipkart.com/search?q=computer&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_2_4_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_2_4_na_na_na&as-pos=2&as-type=RECENT&suggestionId=computer&requestId=0e607119-882c-440d-b914-504dea9890a1&as-backfill=on',headers=headers)
soup=bs4.BeautifulSoup(res.text,'lxml')
for a in soup.findAll('a',href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    #rating=a.find('div', attrs={'class':'hGSR34 _2beYZw'})
    rating=a.find('div', attrs={'class':'niH0FQ'})
    desc=a.find('div',attrs={'class':'_3ULzGw'})
    lst1.append(name.text)
    lst2.append(price.text)
    lst3.append(rating.text)
    print(name.text,price.text,rating.text,desc.text)
