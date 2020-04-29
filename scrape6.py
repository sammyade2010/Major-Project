#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 09:56:56 2020

@author: geraldine
"""


import requests
import lxml.html
import csv

print ('program started...')

html = requests.get('https://www.currys.ie/ieen/computing/laptops/laptops/315_3226_30328_xx_xx/xx-criteria.html')
pri = lxml.html.fromstring(html.content)

html = requests.get('https://www.currys.ie/ieen/phones-broadband-and-sat-nav/mobile-phones-and-accessories/mobile-phones/362_3412_32041_xx_xx/xx-criteria.html')
pri1 = lxml.html.fromstring(html.content)

html = requests.get('https://www.currys.ie/ieen/dslr-cameras/digital-cameras/dslr-and-compact-system-cameras/344_3757_31522_xx_ba00010675-bv00308606/xx-criteria.html')
pri2 = lxml.html.fromstring(html.content)

html = requests.get('https://www.currys.ie/ieen/household-appliances/refrigeration/fridges/333_3127_30214_xx_xx/xx-criteria.html')
pri3 = lxml.html.fromstring(html.content)

html = requests.get('https://www.currys.ie/ieen/tv-and-home-entertainment/televisions/televisions/301_3002_30002_xx_xx/xx-criteria.html')
pri4 = lxml.html.fromstring(html.content)

html = requests.get('https://www.did.ie/laptops-notebooks')
pri5 = lxml.html.fromstring(html.content)

html = requests.get('https://www.did.ie/smartphones')
pri6 = lxml.html.fromstring(html.content)

html = requests.get('https://www.did.ie/digital-cameras')
pri7 = lxml.html.fromstring(html.content)

html = requests.get('https://euronics.ie/category/laptops/')
pri8 = lxml.html.fromstring(html.content)

html = requests.get('https://euronics.ie/category/smartphones/')
pri9 = lxml.html.fromstring(html.content)

html = requests.get('https://euronics.ie/category/tv-s-televisions/')
pri10 = lxml.html.fromstring(html.content)


with open('prodnames.csv', 'w', newline="") as csvfile:

    myWriter = csv.writer(csvfile, delimiter='\t')

   #this code is instead of you first two loops. the while loop loops through both, and outputs the name and price to the once file. 
   #strip gets rind of additional white space chararters
    laptopnames = pri.xpath('//span[@data-product="name"]/text()')
    currysprices2 = pri.xpath('//strong[@data-product="price"]/text()')

    phonesnames = pri1.xpath('//span[@data-product="name"]/text()')
    currysprices3 = pri1.xpath('//strong[@data-product="price"]/text()')

    Cameranames = pri2.xpath('//span[@data-product="name"]/text()')
    currysprices4 = pri2.xpath('//strong[@class="price"]/text()')

    fridgenames = pri3.xpath('//span[@data-product="name"]/text()')
    currysprices5 = pri3.xpath('//strong[@class="price"]/text()')

    tvnames = pri4.xpath('//span[@data-product="name"]/text()')
    currysprices6 = pri4.xpath('//strong[@class="price"]/text()')

    didNames = pri5.xpath('//h2[@class="product-name"]/a/text()')
    didprices = pri5.xpath('//span[@class="price"]/text()')

    didNames1 = pri6.xpath('//h2[@class="product-name"]/a/text()')
    didprices1 = pri6.xpath('//span[@class="price"]/text()')

    cameraNames1 = pri7.xpath('//h2[@class="product-name"]/a/text()')
    cameraprices1 = pri7.xpath('//span[@class="price"]/text()')

    euronicNames = pri8.xpath('//h3[@class="name"]/a/text()')
    euronicPrices = pri8.xpath('//span[@class="normprice"]/text()')

    euronicNames1 = pri9.xpath('//h3[@class="name"]/a/text()')
    euronicPrices1 = pri9.xpath('//span[@class="normprice"]/text()')

    euronicNames2 = pri10.xpath('//h3[@class="name"]/a/text()')
    euronicPrices2 = pri10.xpath('//span[@class="normprice"]/text()')
    
    
    x=0
    while x < len(laptopnames):
      print('Curries ;' , laptopnames[x], ";", currysprices2[x])
      myWriter.writerow(['Curries' , (laptopnames[x].strip()),  currysprices2[x].strip()])
      x+=1

    x=0
    while x < len(phonesnames):
      print('Curries ;' , phonesnames[x], ";", currysprices3[x])
      myWriter.writerow(['Curries' , (phonesnames[x].strip()),  currysprices3[x].strip()])
      x+=1

    x=0
    while x < len(Cameranames):
      print('Curries ;' , Cameranames[x], ";", currysprices4[x])
      myWriter.writerow(['Curries' , (Cameranames[x].strip()),  currysprices4[x].strip()])
      x+=1

    x=0
    while x < len(fridgenames):
      print('Curries ;' , fridgenames[x], ";", currysprices5[x])
      myWriter.writerow(['Curries' , (fridgenames[x].strip()),  currysprices5[x].strip()])
      x+=1

    x=0
    while x < len(tvnames):
      print('Curries ;' , tvnames[x], ";", currysprices6[x])
      myWriter.writerow(['Curries' , (tvnames[x].strip()),  currysprices6[x].strip()])
      x+=1

    x=0
    while x < len(didNames):
      print('DID ;' , didNames[x], ";", didprices[x])
      myWriter.writerow(['DID' , (didNames[x].strip()),  didprices[x].strip()])
      x+=1

    x=0
    while x < len(didNames1):
      print('DID ;' , didNames1[x], ";", didprices1[x])
      myWriter.writerow(['Curries' , (didNames1[x].strip()),  didprices1[x].strip()])
      x+=1

    x=0
    while x < len(cameraNames1):
      print('DID ;' , cameraNames1[x], ";", cameraprices1[x])
      myWriter.writerow(['Curries' , (cameraNames1[x].strip()),  cameraprices1[x].strip()])
      x+=1

    x=0
    while x < len(euronicNames):
      print('Euronics ;' , euronicNames[x], ";", euronicPrices[x])
      myWriter.writerow(['Euronics' , (euronicNames[x].strip()),  euronicPrices[x].strip()])
      x+=1

    x=0
    while x < len(euronicNames1):
      print('Euronics ;' , euronicNames1[x], ";", euronicPrices1[x])
      myWriter.writerow(['Euronics' , (euronicNames1[x].strip()),  euronicPrices1[x].strip()])
      x+=1

    x=0
    while x < len(euronicNames2):
      print('Euronics ;' , euronicNames2[x], ";", euronicPrices2[x])
      myWriter.writerow(['Euronics' , (euronicNames2[x].strip()),  euronicPrices2[x].strip()])
      x+=1


   
    
    #for line in csvfile:
    
    
    
