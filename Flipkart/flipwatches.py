import requests
import bs4
link=['https://www.flipkart.com/search?q=washing+machines&sid=j9e%2Cabm%2C8qx&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=washing+machines%7CWashing+Machines+%26+Dryers&requestId=ec45d364-754b-457b-b28c-d55d8b671792&as-searchtext=was']
lst1=[]#names
lst2=[]#prices
lst3=[]#ratiings and reviews
lst4=[]#description
#headers= {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0']
for j in range(len(link)):
    print('gg')
    res=requests.get(link[j])
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for a in soup.findAll('a',href=True, attrs={ 'class':"_1fQZEK"}):
                        name=a.find('div', attrs={'class':'_4rR01T'})
                        price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})

                        rating=a.find('div', attrs={'class':'_3LWZlK'})

                        desc=a.find('div',attrs={'class':'fMghEO'})

                        lst1.append(name.text)
                        lst2.append(price.text)
                        lst3.append(rating.text)
                        lst4.append(desc.text)
for i in range(1,len(lst1)):
        print(i,'...)','Name:',lst1[i],'Price:' , lst2[i],'Ratings:',lst3[i],'Desc:',lst4[i])
