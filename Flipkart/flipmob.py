import requests
import bs4
link=[]
lst1=[]#names
lst2=[]#prices
lst3=[]#ratiings and reviews
lst4=[]#description
#headers= {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0']
link.append('https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=576da83a-dc8f-428c-9882-927ceb2412ec&as-searchtext=mobiles')
for j in range(len(link)):
    print('gg')
    res=requests.get(link[j])
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
                        print('ff')
                        name=a.find('div', attrs={'class':'_4rR01T'})#<div class="_4rR01T">Realme Narzo 20 (Glory Silver, 128 GB)</div>
                        print(name)
                        price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
                        #<div class="_30jeq3 _1_WHN1">₹10,999</div>price
                        print(price)
                        rating=a.find('div', attrs={'class':'_3LWZlK'})
                        #<div class="_3LWZlK">4.3<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="_1wB99o"></div>
                        print(rating)
                        desc=a.find('div',attrs={'class':'fMghEO'})
                        #<div class="fMghEO"><ul class="_1xgFaf"><li class="rgWa7D">6 GB RAM | 64 GB ROM | Expandable Upto 512 GB</li><li class="rgWa7D">16.59 cm (6.53 inch) Full HD+ Display</li><li class="rgWa7D">13MP + 8MP + 5MP + 2MP | 8MP Front Camera</li><li class="rgWa7D">5000 mAh Lithium Polymer Battery</li><li class="rgWa7D">MediaTek Helio G80 Processor</li><li class="rgWa7D">1 Year for Handset, 6 Months for Accessories</li></ul></div>
                        #<div class="_30jeq3 _1_WHN1">₹10,999</div>
                        #<li class="rgWa7D">6 GB RAM | 64 GB ROM | Expandable Upto 512 GB</li>
                        #<ul class="_1xgFaf"><li class="rgWa7D">6 GB RAM | 64 GB ROM | Expandable Upto 512 GB</li><li class="rgWa7D">16.59 cm (6.53 inch) Full HD+ Display</li><li class="rgWa7D">13MP + 8MP + 5MP + 2MP | 8MP Front Camera</li><li class="rgWa7D">5000 mAh Lithium Polymer Battery</li><li class="rgWa7D">MediaTek Helio G80 Processor</li><li class="rgWa7D">1 Year for Handset, 6 Months for Accessories</li></ul>
                        print(desc)
                        lst1.append(name.text)
                        lst2.append(price.text)
                        lst3.append(rating.text)
                        lst4.append(desc.text)
for i in range(1,len(lst1)):
        print(i,'...)','Name:',lst1[i],'Price:' , lst2[i],'Ratings:',lst3[i],'Desc:',lst4[i])
