from tkinter import*
from PIL import Image,ImageTk
from tkinter import messagebox
import requests
import bs4
lst1=[]#names
lst2=[]#prices
lst3=[]#ratiings and reviews
lst4=[]#description
link=['https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_2_1_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_2_1_na_na_na&as-pos=2&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=96a5328b-a5aa-4d6f-b3cb-5712291c4839&as-searchtext=l']
#link=['https://www.flipkart.com/search?q=speakers&sid=0pm%2C0o7&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_5_na_na_na&as-pos=1&as-type=RECENT&suggestionId=speakers%7CSpeakers&requestId=0c2c01bb-6fcb-4859-867e-895921444828&as-searchtext=speak']
for i in range(len(link)):
    res=requests.get(link[i])
    soup=bs4.BeautifulSoup(res.text,'lxml')
    for a in soup.findAll('a',href=True, attrs={'class':'_1fQZEK'}):
                        #print('ff')
                        name=a.find('div', attrs={'class':'_4rR01T'})
                        price=a.find('div', attrs={'class':'_30jeq3 _1_WHN1'})
                        rating=a.find('div', attrs={'class':'_3LWZlK'})
                        desc=a.find('div',attrs={'class':'fMghEO'})
                        lst1.append(name.text)
                        lst2.append(price.text)
                        #lst3.append(rating.text)
                        lst4.append(desc.text)
for i in lst1:
    print(i,end='')
for i in lst2:
    print(i,end='')
for i in lst4:
    print(i,end='')


no=0
def scr():
    #print('hi')
    def next1():
        global no
        no+=1
        print('hi')
        if len(lst1)>=no:
            lbn=Label(top,text='Name:'+lst1[no],font=('arial',15),fg='black',bg='white').place(x=10,y=10)
            lbp=Label(top,text='Price:'+lst2[no],font=('arial',15),fg='black',bg='white').place(x=10,y=60)
            #lbr=Label(top,text='Ratings:'+lst3[no],font=('arial',15),fg='black',bg='white').place(x=10,y=110)
            lbd=Label(top,text='Desc:'+lst4[no],font=('arial',10),fg='black',bg='white').place(x=10,y=160)
        else:
            pass
    def prev():
        global no
        no-=1
        lbn=Label(top,text='Name:'+lst1[no],font=('arial',15),fg='black',bg='white').place(x=10,y=10)
        lbp=Label(top,text='Price:'+lst2[no],font=('arial',15),fg='black',bg='white').place(x=10,y=60)
        #lbr=Label(top,text='Ratings:'+lst3[no],font=('arial',15),fg='black',bg='white').place(x=10,y=110)
        lbd=Label(top,text='Desc:'+lst4[no],font=('arial',10),fg='black',bg='white').place(x=5,y=160)
            
    global filename
    top = Tk()
    top.geometry('600x500')
    C = Canvas(top, bg="blue", height=250, width=300)
    filename = PhotoImage(file = "C:\\Users\\SOBIKA\\Downloads\\Cars (16).png")
    background_label = Label(top, image=filename)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    C.pack()
    i=len(lst1)
    pre=Button(top,text='Previous',font=('jokerman','20'),fg='red',bg='blue',command=prev).place(x=0,y=450)
    nex=Button(top,text='Next',font=('jokerman','20'),fg='red',bg='blue',command=next1).place(x=510,y=450)
    nop=Label(top,text='No of pgs....'+str(i),font=('jokerman','20'),fg='red',bg='black').place(x=240,y=450)
scr()

