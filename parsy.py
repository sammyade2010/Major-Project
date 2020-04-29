import csv
from tkinter import *

#html_output = ''
names = []
self = ''
#END = []
nameList = ['Curries', 'DID', 'Euronics', 'iPhone', 'Samsung', 'HP']

with open('temp.csv', 'r', encoding='utf8') as pdata_files:
    csv_data = csv.DictReader(pdata_files)

    next(csv_data)

    for line in csv_data:
        def retrieve_input():
            input = self.myText_Box.get("1.0",END)
            if input in line[1]:
                print(line)
                filteredList = filter(None, nameList)
                names.append(f"{line[0]} {line[1]}")
#reading text box
#if statement
#append
#compar
#when writing price remove first character

with open('temp1.csv', 'w', newline="", encoding='utf8') as new_file:
#                    for line in csv_data:
    print(line)
    new_file.writerow(line)