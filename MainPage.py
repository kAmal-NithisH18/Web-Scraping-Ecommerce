import math
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox
import sqlite3 as sq
import random
import password1 as p1
import webbrowser
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import bs4
import requests
#import pandas as pd
from PIL import ImageTk,Image
import time
import csv
from googlesearch import search 
no=0
cons=sq.connect('store.db')
cur_=cons.cursor()
z=cur_.execute
def displaytkamz(lst1,lst2,lst3):
            def next1():
                global no
                no+=1
                if len(lst1)>=no:
                    lbn=Label(top,text='Name:'+lst1[no],font=('arial',15),fg='black',bg='white').place(x=10,y=150)
                    lbp=Label(top,text='Price:'+lst2[no],font=('arial',15),fg='black',bg='white').place(x=10,y=200)
                    lbr=Label(top,text='Ratings:'+lst3[no],font=('arial',15),fg='black',bg='white').place(x=10,y=250)
                else:
                    pass
            def prev():
                global no
                no-=1
                lbn=Label(top,text='Name:'+lst1[no],font=('arial',15),fg='black',bg='white').place(x=10,y=150)
                lbp=Label(top,text='Price:'+lst2[no],font=('arial',15),fg='black',bg='white').place(x=10,y=200)
                lbr=Label(top,text='Ratings:'+lst3[no],font=('arial',15),fg='black',bg='white').place(x=10,y=250)

            i=len(lst1)
            pre=Button(top,text='Previous',font=('jokerman','20'),fg='red',bg='blue',command=prev).place(x=0,y=450)
            nex=Button(top,text='Next',font=('jokerman','20'),fg='red',bg='blue',command=next1).place(x=510,y=450)
            nop=Label(top,text='No of pgs....'+str(i),font=('jokerman','20'),fg='red',bg='black').place(x=240,y=450)
def displaytkflip(lst1,lst2,lst4):
            def next1():
                global no
                no+=1
                if len(lst1)>=no:
                    lbn=Label(top,text='Name:'+lst1[no],font=('arial',15),fg='black',bg='white').place(x=10,y=150)
                    lbp=Label(top,text='Price:'+lst2[no],font=('arial',15),fg='black',bg='white').place(x=10,y=200)
                    #lbr=Label(top,text='Ratings:'+lst3[no],font=('arial',15),fg='black',bg='white').place(x=10,y=250)
                    lbd=Label(top,text='Desc:'+lst4[no],font=('arial',10),fg='black',bg='white').place(x=10,y=300)
                else:
                    pass
            def prev():
                global no
                no-=1
                lbn=Label(top,text='Name:'+lst1[no],font=('arial',15),fg='black',bg='white').place(x=10,y=150)
                lbp=Label(top,text='Price:'+lst2[no],font=('arial',15),fg='black',bg='white').place(x=10,y=200)
                #lbr=Label(top,text='Ratings:'+lst3[no],font=('arial',15),fg='black',bg='white').place(x=10,y=250)
                lbd=Label(top,text='Desc:'+lst4[no],font=('arial',10),fg='black',bg='white').place(x=5,y=300)

            i=len(lst1)
            pre=Button(top,text='Previous',font=('jokerman','20'),fg='red',bg='blue',command=prev).place(x=0,y=450)
            nex=Button(top,text='Next',font=('jokerman','20'),fg='red',bg='blue',command=next1).place(x=510,y=450)
            nop=Label(top,text='No of pgs....'+str(i),font=('jokerman','20'),fg='red',bg='black').place(x=240,y=450)

def quit1():
    rate=Tk()
    rate.geometry('300x600')
    rate.title("RATINGS")
    rate.configure(bg='yellow')
    r=Label(rate,text='U R comments down',font=('jokerman',20)).pack()
    e=Entry(rate)
    e.pack()
    y=['*1*','*2*','*3*','*4*','*5*']
    
    st=Label(rate,text='RATE US',font=('jokerman',20)).pack()
    def r1():
        global star
        star=1
    def r2():
        global star
        star=2
    def r3():
        global star
        star=3
    def r4():
        global star
        star=4
    def r5():
        global star
        star=5
    o=[r1,r2,r3,r4,r5]
    l=Label(rate,text='THANK YOU !',font=('jokerman',20)).pack()
    def h():
        ev=str(e.get())
        #print(star)
        playsound.playsound(r'E:\c drive\all music\favourites\Usure-Masstamilan.In.mp3')
        z('insert into RATINGS values("{}","{}","User");'.format(ev,star))
        cons.commit()
       
        dest=[rate,f,r,t1k]
        for i in range(len(dest)):
                dest[i].destroy()
                time.sleep(1)
    for i in range(5):
        b=Button(rate,text=y[i],font=('jokerman',20),command=o[i]).pack()
    qu=Button(rate,text='QUIT',font=('jokerman',20),command=h).pack()
    
def websearch():
    rtt=Tk()
    rtt.title('websearch')
    print(cusserch,'k')
    global entweb
    query=str(entweb.get())
    print(query,'kk')
    l=[]
    for j in search(query, tld="co.in", num=10, stop=10, pause=2): 
        l.append(j)
    print(l[0])
    res=requests.get(l[0])
    appending=''
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for i in soup.select('p'):
        appending+=(i.text).strip()
        print(appending,type(appending))    
   # entweb.get\
    add=0
    print(appending[add:add+120],'tt')
    rtt.geometry('1200x1200')
    length=math.ceil(len(appending)/120)
    rem=len(appending)%120
    add=0
    for i in range(length):
        try:
           tdis1=Label(rtt,text=appending[add:add+120],font=('arial',15)).pack()
           add+=120
        except:
            tdis2=Label(rtt,text=appending[add:],font=('arial',15)).pack()
    def request():
        for iee in l:
            if 'flipkart' in iee:
                print(iee,'in flik')
                webbrowser.open(iee)
                
    button_1=Button(rtt,text='Buy now',command=request,fg='red',bg='yellow',font=('arial',20)).pack()
            
           
       
    
def weeball():
    global t1k
    t1k=Tk()
    t1k.title('STARTING')
    t1k.configure(bg='black')
    t1k.geometry('300x300')
    #img=ImageTk.PhotoImage(Image.open('chck.jpg'))
    #l=Label(t1k,image=img)
    #l.pack()

    def oc_check():
        che=str(otp1.get())
        if str(aotp)==che:
            z("select * from storage;")
            lst1=cur_.fetchall()
            ECHECK=str(re1.get())
            CCHECK=str(xye2.get())
            for i in range(len(lst1)):
                    checklst=lst1[i]
                    eidcheck=checklst[1]
                    countcheck=checklst[4]
                    e123=checklst[2]
                    refeid=checklst[5]
                    usg=str(geu.get())
                    if ECHECK==eidcheck and CCHECK==countcheck:
                        if refeid==usg:
                            print(e123)
                            ump='                '
                            jjo=Label(refotp,text='YOUR PASSWORD IS:'+e123+ump,fg='white',bg='red',font=('arial',15)).place(x=10,y=200)
                            break
                        else:
                            jjo=Label(refotp,text='WE R NOT SURE THIS BELONGS 2  U',fg='white',bg='black',font=('arial',15)).place(x=10,y=260)
                            break
                            
        else:
            #jjo=Label(refotp,text='SOMETHING ENTERED WRONG',fg='white',bg='black',font=('arial',15)).place(x=10,y=260)
            messagebox.showinfo('Wrong input','Something entered wrong')

    def OTPC():
        global aotp
        aotp=random.randint(1001,9999)
        mail_content = 'OTP From KKK web scrapers:'+' '+str(aotp)
        sender_address = 'webscraping12345@gmail.com'
        sender_pass = p1.Pass()
        readd=str(geu.get())
        receiver_address = readd
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = receiver_address
        message['Subject'] = 'u r one time password'
        message.attach(MIMEText(mail_content, 'plain'))
        session = smtplib.SMTP('smtp.gmail.com', 465) 
        session.starttls() 
        session.login(sender_address, sender_pass)
        text = message.as_string()
        session.sendmail(sender_address, receiver_address, text)
        session.quit()
        print('Mail Sent')

    def passw():
        OTPC()
        global refotp
        refotp=Tk()
        refotp.title('OTP CHECK')
        refotp.geometry('300x300')
        refotp.configure(bg='black')
        #Otp=Label(refotp,text='Enter OTP SENT:',font=('arial',10),fg='white',bg='black').place(x=10,y=10)
        messagebox.showinfo('OTP','Otp send to mail succesfully')
        global otp1
        otp1=Entry(refotp)
        otp1.place(x=150,y=10)
        testotp=Button(refotp,text='ENTER',font=('arial',10),fg='white',bg='red',command=oc_check).place(x=50,y=150)
                        
    def fpp():
        global xy
        xy=Tk()
        xy.geometry('300x300')
        xy.configure(bg='black')
        xy.title('FORGOT PASSWORD')
        xyl=Label(xy,text='Email Id:',font=('arial',20),fg='white',bg='black').place(x=10,y=10)
        global re1
        re1=Entry(xy)
        re1.place(x=150,y=20)
        global xye2
        xyl=Label(xy,text='Country given:',font=('arial',15),fg='white',bg='black').place(x=10,y=50)
        xye2=Entry(xy)
        xye2.place(x=150,y=60)
        guess=Label(xy,text='EMAIL ID FOR OTP:',font=('arial',10),fg='white',bg='black').place(x=10,y=100)
        global geu
        geu=Entry(xy,width=40)
        geu.place(x=150,y=120)
        xtb=Button(xy,text="CLICK 2 GET OUR PASSWORD@@",command=passw,font=('arial',10),fg='white',bg='red').place(x=20,y=160)
        ###sendOTP

    def web():
        global top
        top=Tk()
        top.title('Processing...........................................................................!')
        top.configure(bg='blue')
        top.geometry('1000x1000')
        scr=str(ent1.get())
        lol=Label(top,text='WEB SCRAPING '+scr,font=('arial',15),fg='white',bg='black').place(x=10,y=10)
        def aws():
            if scr=='Laptops':
                  lst1=[]
                  lst2=[]
                  lst3=[]
                  res=requests.get('https://www.snapdeal.com/search?keyword=laptop&santizedKeyword=mobile+phone&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy')
                  res=res.text
                  data=bs4.BeautifulSoup(res,'lxml')
                  r=data.select('.product-desc-rating')
                  for i in r:
                        p=i.select('.product-title')
                        a=p[0].getText()
                        op=i.find_all('span','lfloat product-desc-price strike')
                        op=str(op[0].getText())
                        lst1.append(p)
                        lst2.append(op)
                  displaytkamz(lst1,lst2,lst3)
                  pass
            if scr=='Mobiles':
               lst1=[]#Names
               lst2=[]#Prices
               lst3=[]#Ratings
               res=requests.get('https://www.snapdeal.com/search?keyword=mobile%20phone&santizedKeyword=mobile+phone+back+cover&catId=0&categoryId=0&suggested=false&vertical=p&noOfResults=20&searchState=&clickSrc=go_header&lastKeyword=&prodCatId=&changeBackToAll=false&foundInAll=false&categoryIdSearched=&cityPageUrl=&categoryUrl=&url=&utmContent=&dealDetail=&sort=rlvncy')
               res=res.text
               data=bs4.BeautifulSoup(res,'lxml')
               r=data.select('.product-desc-rating')
               for i in r:
                  p=i.select('.product-title')
                  a=p[0].getText()
                  op=i.find_all('span','lfloat product-desc-price strike')
                  op=op[0].getText()
                  lst1.append(str(a))
                  lst2.append(str(op))
               displaytkamz(lst1,lst2,lst3)
        def kart():
            if scr=='Mobiles':
                lst1=[]#names
                lst2=[]#prices
                lst3=[]#ratiings and reviews
                lst4=[]#description
                link=[]
                link.append('https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_7_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=576da83a-dc8f-428c-9882-927ceb2412ec&as-searchtext=mobiles')
                for j in range(len(link)):
                    res=requests.get(link[j])
                    soup=bs4.BeautifulSoup(res.text,'lxml')
                    for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
                        name=a.find('div', attrs={'class':'_4rR01T'})#<div class="_4rR01T">Realme Narzo 20 (Glory Silver, 128 GB)</div>
                        print(name)
                        price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
                        #<div class="_30jeq3 _1_WHN1">₹10,999</div>price
                        print(price)
                        rating=a.find('div', attrs={'class':'_3LWZlK'})
                        #<div class="_3LWZlK">4.3<img src="data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIxMyIgaGVpZ2h0PSIxMiI+PHBhdGggZmlsbD0iI0ZGRiIgZD0iTTYuNSA5LjQzOWwtMy42NzQgMi4yMy45NC00LjI2LTMuMjEtMi44ODMgNC4yNTQtLjQwNEw2LjUuMTEybDEuNjkgNC4wMSA0LjI1NC40MDQtMy4yMSAyLjg4Mi45NCA0LjI2eiIvPjwvc3ZnPg==" class="_1wB99o"></div>
                        print(rating)
                        desc=a.find('div',attrs={'class':'fMghEO'})
                        print(desc)
                        lst1.append(name.text)
                        lst2.append(price.text)
                        #lst3.append(rating.text)
                        lst4.append(desc.text)
                    displaytkflip(lst1,lst2,lst4)

                        ##########
            if scr=='Laptops':
                lst1=[]#names
                lst2=[]#prices
                lst3=[]#ratiings and reviews
                lst4=[]#description
                link=['https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=6c5fc294-b616-40f9-99e8-95c3ab996bce&as-backfill=on','https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_HistoryAutoSuggest_1_2_na_na_na&otracker1=AS_QueryStore_HistoryAutoSuggest_1_2_na_na_na&as-pos=1&as-type=HISTORY&suggestionId=laptop%7CLaptops&requestId=f344c299-9126-41a3-80c0-01ca84da5bfb&page=2']
                headers= {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
                for i in range(len(link)):
                    res=requests.get(link[i],headers=headers)
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
                        print(desc)
                        lst1.append(name.text)
                        lst2.append(price.text)
                        #lst3.append(rating.text)
                        lst4.append(desc.text)
                    displaytkflip(lst1,lst2,lst4)
            if scr=='Smart Tv':
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
                                        #lst3.append(rating.text)
                                        lst4.append(desc.text)
                    displaytkflip(lst1,lst2,lst4)
            if scr=='Washing Machine':
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
                                        #lst3.append(rating.text)
                                        lst4.append(desc.text)
                    displaytkflip(lst1,lst2,lst4)
                                    
                    

            
        amzn=Button(top,text='Get in AMAZON',font=('arial',15),fg='white',bg='red',command=aws).place(x=10,y=50)
        flipk=Button(top,text='Get in FLIPKART',font=('arial',15),fg='white',bg='red',command=kart).place(x=10,y=100)

        
    def pop():
            q=Tk()
            q.title('CONTACT US')
            q.geometry('500x100')
            q.configure(bg='black')
            def uo():
                q.destroy()
            pri='EmailId=kkk@gmail.com,phone no=1234'
            lol=Label(q,text=pri,font=('arial',15),fg='white',bg='black').place(x=10,y=10)
            bh=Button(q,text='QUIT',command=uo).place(x=50,y=60)
    def opo():
            q=Tk()
            q.title('WHAT ABOUT')
            q.geometry('1000x200')
            q.configure(bg='black')
            pri='WEB SCRAPING:IT IS A TOOL WHICH GIVES/EXTRACTS A LARGE AMOUNT OF DATA AT A TIME.'
            OPPO='FOR RECENT INCIDENTS/EVENTS/SOMETHING IT GIVES ALL POSSIBLE DATA @ ALL PRESENT WEB(www.)'
            R='FOR PRODUCTS IT GIVES BEST PRICES,DEALS,MOST RATED,CHEAP@ ALL PRESENT ONLINE STORES'
            lol=Label(q,text=pri,font=('arial',15),fg='white',bg='black').place(x=10,y=10)
            lol=Label(q,text=OPPO,font=('arial',10),fg='white',bg='black').place(x=10,y=50)
            lol=Label(q,text=R,font=('arial',15),fg='white',bg='black').place(x=10,y=80)
            lol=Label(q,text='from amazon,flipkart,snapdeal,,etc with analyser,graphs etc..',font=('arial',15),fg='white',bg='black').place(x=10,y=110)

    def au():
        z("select * from storage;")
        lst1=cur_.fetchall()
        def hhh():
            pasc=str(EE.get())
            eidc=str(PP.get())
            d1={pasc:eidc}
            for i in range(len(lst1)):
                checklst=lst1[i]
                eidcheck=checklst[1]
                pcheck=checklst[2]
                dc2={eidcheck:pcheck}
                checking=0
                if d1==dc2:
                    checking=1
                    r1=Tk()
                    r1.geometry('1400x1200')
                    r1.title('WEB SCRAPPING')
                    r1.config(bg='black')
                    lab1=Label(r1,text='WELCOME',fg='red',bg='yellow',font=('arial',30)).place(x=400,y=50)
                    w='We r here to make u r analysis,information gathering in a simple way.'
                    u='For products v give best deals,and offers in all the web and many others '
                    lab2=Label(r1,text=w,fg='white',bg='black',font=('arial',20)).place(x=0,y=100)
                    lab2=Label(r1,text=u,fg='white',bg='black',font=('arial',20)).place(x=0,y=150)
                    lab3=Label(r1,text='ENTER:',fg='green',bg='pink',font=('arial',20)).place(x=200,y=300)

                    #ent1=Entry(r1,width=30)
                    #ent1.place(x=350,y=310)
                    var=StringVar()
                    data=['Mobiles','Laptops','Washing Machine','Smart Tv','More..comming soon']
                    var.set(data)
                    global ent1
                    ent1=Combobox(r1,text="select country!",values=data)
                    ent1.place(x=350,y=310)
                
                    def c1():
                        e=str(ent1.get())
                        if e=='':
                            labc=Label(r1,text='*Enter is compulsory',fg='red',bg='pink',font=('arial',20)).place(x=100,y=500)
                            l1=['orange','red','pink','yellow','blue','brown','white']
                            for i in range(1):
                                a=random.randint(0,6)
                                lc1=l1[a]
                                lab3=Label(r1,text='ENTER:',fg='green',bg=lc1,font=('arial',20)).place(x=200,y=300)
                        else:
                            #abc=Label(r1,text='',fg='red').place(x=100,y=500)
                            print('web scrapping')
                            web()
                            #here comes  our code
                    f=checklst[4]
            #glbal eidc
                    eidc=str(EE.get())
                    lablog=Label(r1,text='Entering as:email id='+eidc,fg='white',bg='black',font=('arial',15)).place(x=25,y=600)
                    lablog=Label(r1,text='Location='+f,fg='white',bg='black',font=('arial',15)).place(x=25,y=650)
                    but1=Button(r1,text='Search',fg='red',bg='green',font=('arial',15),command=c1).place(x=550,y=300)
                    but2=Button(r1,text='Contact us:',fg='white',bg='red',font=('arial',15),command=pop).place(x=600,y=600)
                    but3=Button(r1,text='Quit',fg='white',bg='red',font=('arial',15),command=quit1).place(x=640,y=640)
                    labweb=Label(r1,text="Customized search:",fg='white',bg='black',font=('arial',15)).place(x=25,y=450)
                    global entweb
                    entweb=Entry(r1)
                    entweb.place(x=230,y=459)
                    butweb=Button(r1,text='serach',fg='white',bg='red',font=('arial',15),command=websearch).place(x=400,y=450)
                    break
                if checking==0:# d1!=dc2:
                    looo=Label(ff,text='*Invalid Username or Password',fg='green',bg='pink',font=('arial',15)).place(x=10,y=220)
                    messagebox.askretrycancel("Wrong", "Invalid Username or Password please correct password and press submit")
                    ##############################################################################################33#
        global ff
        ff=Tk()
        ff.title('CHECK')
        ff.geometry('300x300')
        ff.configure(bg='black')
        ER=Label(ff,text='EMAIL ID:',bg='black',fg='white',font=('arial',15)).place(x=10,y=50)
        EE=Entry(ff)
        EE.place(x=150,y=50)
        PR=Label(ff,text='PASSWORD:',bg='black',fg='white',font=('arial',15)).place(x=10,y=100)
        PP=Entry(ff,show="*")
        PP.place(x=150,y=100)
        FOR=Button(ff,text='Forgot Password??',bg='red',fg='yellow',command=fpp,font=('arial',10)).place(x=10,y=250)
        bbbbb=Button(ff,text='SUBMIT',font=('arial',15),bg='yellow',fg='red',command=hhh).place(x=150,y=170)
            
    def nor():
        global r#nam,eid,pass,gender,country,refeid
        r=Tk()
        r.geometry('700x700')
        r.title("Registration form")
        r.config(bg='black')
        def c1():
            f=str(fgg.get())
            nam=str(fne.get())
            global eid
            eid=str(ee1.get())
            v1=str(v.get())
            h=[f,nam,eid,v1]
            passs=str(psw1.get())
            reff=str(refe.get())    
            for i in range(len(h)):
                if h[i]=='':
                    #erl=Label(r,text='*ALL REQUIRED!',fg='red',bg='black',font=('bold',20)).place(x=400,y=550)
                    messagebox.askretrycancel('All required','Please enter all the data')
            if int(v1)!=0:
                    if int(v1)==1:
                        gender='Male'
                    else:
                        gender='Female'
            z('select *from storage;')
            dupcheck=cur_.fetchall()
            lstdup=()
            

            for i in range(len(dupcheck)):
                    lstdup=dupcheck[i]
                    if lstdup==(nam,eid,passs,v1,f):
                        dupfind=Label(r,text='THE EMAILID,PASSWORD IS ALREADY TAKEN BY SOMEONE',fg='red',bg='black',font=('bold',10)).place(x=0,y=500)
                        break
            else:
                    if len(passs)<6:
                            #erl=Label(r,text='LENGTH OF PASSWORD SHOULD B STRONG',fg='red',bg='black',font=('bold',20)).place(x=0,y=500)
                        messagebox.showwarning('Length','Password must be strong')
                        
                    elif len(passs)>=6:
                        print('hi')
                        print(str(refe.get()))
                        '''try:
                            mail_content = 'OTP From KKK web scrapers:'+' '
                            sender_address = 'webscrapingcs12345@gmail.com'
                            sender_pass = p1.Pass()
                            receiver_address = str(refe.get())
                            message = MIMEMultipart()
                            message['From'] = sender_address
                            message['To'] = receiver_address
                            message['Subject'] = 'Sesion initiated pls keep ur password safe'
                            message.attach(MIMEText(mail_content, 'plain'))
                            session = smtplib.SMTP('smtp.gmail.com', 465) 
                            session.starttls() 
                            session.login(sender_address, sender_pass)
                            text = message.as_string()
                            session.sendmail(sender_address, receiver_address, text)
                            session.quit()
                            print('Mail Sent')'''
                            ##################################################################################################
                        z('insert into storage values("{}","{}","{}","{}","{}","{}");'.format(nam,eid,passs,v1,f,reff))
                        cons.commit()
                        import random
                    #######################################################################
                        r1=Tk()
                        r1.geometry('1400x1200')
                        r1.title('WEB SCRAPPING login')
                        r1.config(bg='black')
                        lab1=Label(r1,text='WELCOME',fg='red',bg='yellow',font=('arial',30)).place(x=400,y=50)
                        w='We r here to make u r analysis,information gathering in a simple way.'
                        u='For products v give best eeeeeedeals,and offers in all the web and many others '
                        lab2=Label(r1,text=w,fg='white',bg='black',font=('arial',20)).place(x=0,y=100)
                        lab2=Label(r1,text=u,fg='white',bg='black',font=('arial',20)).place(x=0,y=150)
                        lab3=Label(r1,text='ENTER:',fg='green',bg='pink',font=('arial',20)).place(x=200,y=300)
                        but3=Button(r1,text='Quit',fg='white',bg='red',font=('arial',15),command=quit1).place(x=640,y=640)
                        var=StringVar()
                        data=['Mobiles','Laptops','Washing Machine','Smart Tv','More..comming soon']
                        var.set(data)
                        global ent1
                        ent1=Combobox(r1,text="select country!",values=data)
                        ent1.place(x=350,y=310)
                    #######################################################################
                        def c11():
                            e=str(ent1.get())
                            if e=='':
                                #labc=Label(r1,text='*Enter is compulsory',fg='red',bg='pink',font=('arial',20)).place(x=100,y=500)
                                messagebox.showerror('Empty','Cant be empty')
                                l1=['orange','red','pink','yellow','blue','brown','white']
                                for i in range(15):
                                    a=random.randint(0,6)
                                    lc1=l1[a]
                                    lab3=Label(r1,text='ENTER:',fg='green',bg=lc1,font=('arial',20)).place(x=200,y=300)
                            else:
                                print('web scrapping')
                                web()    
                        lablog=Label(r1,text='Entering as:email id='+eid,fg='white',bg='black',font=('arial',15)).place(x=25,y=600)
                        lablog=Label(r1,text='Location='+f,fg='white',bg='black',font=('arial',15)).place(x=25,y=650)
                        but1=Button(r1,text='Search',fg='red',bg='green',font=('arial',15),command=c11).place(x=550,y=300)
                        but2=Button(r1,text='Contact us:',fg='white',bg='red',font=('arial',15),command=pop).place(x=600,y=600)
                        labweb=Label(r1,text="Customized search:",fg='white',bg='black',font=('arial',15)).place(x=25,y=450)
                        global entweb
                        entweb=Entry(r1)
                        entweb.place(x=230,y=459)
                        butweb=Button(r1,text='serach',fg='white',bg='red',font=('arial',15),command=websearch).place(x=400,y=450)
                ##########
                        '''except:
                            erl=Label(r,text='ENTER AN VALID REFERENE EMAIL',fg='red',bg='black',font=('bold',20)).place(x=0,y=550)'''
                            
        l=Label(r,text='Registration Form',width=20,bg='red',fg='yellow',font=('bold',30))
        l.place(x=90,y=53)

        fn=Label(r,text='Fullname:',bg='black',fg='white',font=('bold',20))
        fn.place(x=80,y=130)

        e=Label(r,text='Email-id:',bg='black',fg='white',font=('bold',20))
        e.place(x=70,y=180)

        fne=Entry(r,width=30)
        fne.place(x=250,y=130)

        ee1=Entry(r,width=30)
        ee1.place(x=250,y=180)

        g=Label(r,text='Gender:',bg='black',fg='white',font=('bold',20))
        g.place(x=70,y=230)
        v=IntVar()
        rb=Radiobutton(r,text="Male",padx=5,variable=v,value=1,bg='red')
        rb.place(x=250,y=230)

        rb=Radiobutton(r,text="Female",padx=20,variable=v,value=2,bg='red')
        rb.place(x=320,y=230)

        con=Label(r,text='Select Country:',bg='black',fg='white',font=('bold',20))
        con.place(x=0,y=280)

        var=StringVar()
        data=['India','Russia','UK','USA','UAE','Australia','Pakisthan','Brazil',"South Africa",'Saudi','Spain','Germany']
        var.set(data)
        fgg=Combobox(r,text="select country!",values=data)
        fgg.place(x=250,y=280)

        psw=Label(r,text='Password:',bg='black',fg='white',font=('bold',20)).place(x=40,y=330)

        psw1=Entry(r,width=30)
        psw1.place(x=250,y=350)

        p=Label(r,text="Programing:",bg='black',fg='white',font=('bold',20)).place(x=30,y=380)
        pg=BooleanVar()
        pg.set(True)
        pgb=Checkbutton(r,text=':PYTHON',font=('bold',20)).place(x=250,y=390)
        pgb=Checkbutton(r,text=':JAVA',font=('bold',20)).place(x=400,y=390)
        refno=Label(r,text='REFERENCE EMAILID',font=('arial',20),fg='white',bg='black').place(x=0,y=440)
        refe=Entry(r,width=30)
        refe.place(x=250,y=490)

        bs=Button(r,text='SUBMIT',bg='yellow',fg='red',font=('bold',20),command=c1).place(x=220,y=600)
        r.mainloop()
        #endnor

    la1_=Label(t1k,text='$WELCOME$',bg='black',fg='white',font=('arial',30)).pack()
    but1k=Button(t1k,text='ALREADY A USER press',command=au,bg='red',fg='white',font=('arial',15)).place(x=20,y=70)
    but2k=Button(t1k,text='NO REGISTER!Signup press',command=nor,bg='red',fg='white',font=('arial',15)).place(x=10,y=130)
    but3k=Button(t1k,text='WHAT ABOUT;',bg='green',fg='yellow',command=opo,font=('arial',10)).place(x=10,y=210)
    but1k=Button(t1k,text='CONTACT US @',bg='red',fg='white',font=('arial',10),command=pop).place(x=150,y=210)

f=Tk()
f.title("WELCOME!!")
cusserch=''
f.configure(bg='black')
e=Label(f,text='Click Me',fg='yellow',bg='red',font=('jokerman',20,'bold')).pack()
photo=PhotoImage(file='p1.png')
b=Button(f,image=photo,command=weeball).pack()









