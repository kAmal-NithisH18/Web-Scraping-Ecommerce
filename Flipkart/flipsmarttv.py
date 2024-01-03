import requests
import bs4
link=[]
lst1=[]#names
lst2=[]#prices
lst3=[]#ratiings and reviews
lst4=[]#description
#headers= {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0']
link.append('https://www.flipkart.com/search?q=smart+tv&as=on&as-show=on&otracker=AS_Query_OrganicAutoSuggest_3_5_na_na_na&otracker1=AS_Query_OrganicAutoSuggest_3_5_na_na_na&as-pos=3&as-type=RECENT&suggestionId=smart+tv&requestId=179f02d6-c093-4276-9416-e96130a59201&as-searchtext=smart')
for j in range(len(link)):
    res=requests.get(link[j])
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
                        name=a.find('div', attrs={'class':'_4rR01T'})#<div class="_4rR01T">Realme Narzo 20 (Glory Silver, 128 GB)</div>
                        price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
                        rating=a.find('div', attrs={'class':'_3LWZlK'})
                        desc=a.find('div',attrs={'class':'fMghEO'})

                        lst1.append(name.text)
                        lst2.append(price.text)
                        lst3.append(rating.text)
                        lst4.append(desc.text)
for i in range(1,len(lst1)):
        print(i,'...)','Name:',lst1[i],'Price:' , lst2[i],'Ratings:',lst3[i],'Desc:',lst4[i])
