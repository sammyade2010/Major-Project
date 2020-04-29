
# Python program to convert  
# CSV to HTML Table 
  
from prettytable import PrettyTable
import pandas as pd 
  
# to read csv file named "samplee" 
a = pd.read_csv("prodnames.csv", sep='\t', encoding='utf8')

#a = open("prodnames.csv", 'r', encoding='utf8') 
  
# read the csv file 
#a = a.readlines() 
  
# to save as html file 
# named as "Table" 
a.to_html("app/templates/app/productsNew.html") 
  
# assign it to a  
# variable (string) 
html_file = a.to_html() 

#l1 = a[0] 
#l1 = l1.split('/t') 
  
# headers for table 
#t = PrettyTable([l1[0],l1[1]]) 
  
# Adding the data 
#for i in range(1, len(a)) : 
#    t.add_row(a[i].split('/t')) 
  
#code = t.get_html_string() 
#html_file = open('app/templates/app/products.html', 'w') 
#html_file = html_file.write(code) 