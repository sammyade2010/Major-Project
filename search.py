
import csv

def searchByCompany():
    company=input('Enter Company\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if company==row[1]:
            print(row)


def searchByProduct():
    product=input('Enter Product name\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if product in row[0]:
            print(row)

def searchByPrice():
    price=input('Enter Price\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if price in row[1]:
            print(row)

def searchByApple():
    apple=input('Enter Apple\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if apple in row[0]:
            print(row)

def searchByLenovo():
    lenovo=input('Enter Lenovo\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if lenovo in row[0]:
            print(row)

def searchByHP():
    hp=input('Enter HP\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if hp in row[0]:
            print(row)

def searchByIphone():
    iphone=input('Enter iPhone\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if iphone in row[0]:
            print(row)

def searchByTV():
    tv=input('Enter TV\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if tv in row[0]:
            print(row)

def searchBySamsung():
    samsung=input('Enter Samsung\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if samsung in row[0]:
            print(row)

def searchByCamera():
    camera=input('Enter Camera\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if camera in row[0]:
            print(row)

def searchByLaptop():
    laptop=input('Enter Laptop\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if laptop in row[0]:
            print(row)

def searchByFridge():
    fridge=input('Enter Fridge\n')
    csv_file=csv.reader(open('prodnames.csv', 'r', encoding='utf8'))

    for row in csv_file:
        if fridge in row[0]:
            print(row)

print('Search company')
print('Search product')
print('search price')
print('Search Apple products')
print('Search Lenovo')
print('Search HP')
print('Search iPhone')
print('Search TV')
print('Search Samsung')
print('Search Camera')
print('Search Laptop')
print('Search Fridge')

src=str(input('Enter here: '))

if src=='company':
    searchByCompany()
elif src=='product':
    searchByProduct()
elif src=='price':
    searchByPrice()
elif src=='apple':
    searchByApple()
elif src=='lenovo':
    searchByLenovo()
elif src=='hp':
    searchByHP()
elif src=='iphone':
    searchByIphone()
elif src=='TV':
    searchByTV()
elif src=='Samsung':
    searchBySamsung()
elif src=='Camera':
    searchByCamera()
elif src=='Laptop':
    searchByLaptop()
elif src=='Fridge':
    searchByFridge()
else:
    print('wrong input')