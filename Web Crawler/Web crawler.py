import urllib.request
import bs4 as bs
import re

primaryLinksNames=[]
SecondLinksNames=[]
primaryLinksAmazon={}
primaryLinksEbay={}
FinalLinksAmazon={}
FinalLinksEbay={}



def amazon_scrapper():
    print("amazon_scrapper")
    
    sauce=urllib.request.urlopen("https://www.amazon.in/gp/site-directory?ref_=nav_shopall_btn").read()
    soup=bs.BeautifulSoup(sauce,'lxml')
    body=soup.find('body')
    mainDiv=body.find('div',id="siteDirectory")
    all_link_tags=mainDiv.find_all('a')
    for link in all_link_tags:
        temp=link.get('href')
        if(re.search('https',temp)==None and re.search('http',temp)==None):
            temp1='https://www.amazon.in'+temp
        temp2=(link.text)
        primaryLinksAmazon[temp2]=temp1
        primaryLinksNames.append(temp2)
    

def ebay_scrapper():
    print("ebay_scrapper")
    sauce=urllib.request.urlopen("https://www.ebay.com/v/allcategories").read()
    soup=bs.BeautifulSoup(sauce,'lxml')
    body=soup.find('body')
    Div=body.find('div',class_="all-categories")
    mainDiv=Div.find('div',class_="all-categories__cards")
    Linkli=mainDiv.find_all('li',class_="sub-category")
    for li in Linkli:
        f=0
        link=li.find('a')
        temp1=link.get('href')
        temp2=link.text
        primaryLinksEbay[temp2]=temp1
        for i in primaryLinksNames:
            if(re.match(temp2,i)==None):
                f=1
        if(f==0):
            primaryLinksNames.append(temp2)

def LinkAmazonScapper(link1):
    
    sauce1=urllib.request.urlopen(link1).read()
    soup1=bs.BeautifulSoup(sauce1,'lxml')
    body=soup1.find('body')
    temp=body.find('div',id="mainResults")
    print(link1)
    if(temp==None):
        
        div1=body.find('div',id="centerCol")
        div2=div1.find('div',id="title_feature_div")
        mainSpan=div2.find('span',id='productTitle')
        text=mainSpan.text
        FinalLinksAmazon[text]=link1
        print(text)
    else:
        
        div1=temp
        div2=div1.find_all('div', class_="a-fixed-left-grid-col a-col-right")
        for div in div2:
            div3=div.find('div',class_="a-row a-spacing-none")
            a=div3.find('a')
            if(a!=None):
                link=a.get('href')
                print("link: ",link)
                h=div3.find('h2')
                heading=h.get('data-attribute')
                print("heading: ",heading)
                FinalLinksAmazon[heading]=link
    


    

def LinkEbayScapper(link2):
    sauce2=urllib.request.urlopen(link2).read()
    soup2=bs.BeautifulSoup(sauce2,'lxml')
    body=soup2.find('body')
    print(link2)
    mainDiv=body.find('div',id="mainContent")
    div1=mainDiv.find_all('div',class_="s-item__info clearfix")
    for div in div1:
        a=div.find('a',class_="s-item__link")
        link=a.get('href')
        h=div.find('h3',class_="s-item__title")
        heading=h.text
        FinalLinksEbay[heading]=link
    

      
       
def Option(op):
    f=0
    for i in primaryLinksNames:
        if(re.search(op,i,re.IGNORECASE)):
            f=1
            SecondLinksNames.append(i)
    if(f==0):
        print("not found")
    else:
        print(SecondLinksNames)
   
def FinalOption(op):
    fA=0
    fE=0

    tempAmazon=primaryLinksAmazon.keys()
    for i in tempAmazon:
        if(re.search(op,i)):
            link1=primaryLinksAmazon[i]
            fA=1

    
    tempEbay=primaryLinksEbay.keys()
    for i in tempEbay:
        if(re.search(op,i)):
            link2=primaryLinksEbay[i]
            fE=1

    if(fA==1 and fE==1):
        LinkAmazonScapper(link1)
        LinkEbayScapper(link2)

    if(fE==1 and fA==0):
        LinkEbayScapper(link2)

    if(fA==1 and fE==0):
        LinkAmazonScapper(link1)
