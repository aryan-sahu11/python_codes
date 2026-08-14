import csv
a = open('file.csv', 'w')
b=csv.writer(a)
b.writerow(['Name', 'Age', 'City'])
a.close()
