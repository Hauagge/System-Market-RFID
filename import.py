import csv
from seed import seed


with open('produtos.csv', mode='r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['name'], row['price'], row['epc'])
        sql = 'INSERT into estoque (name,EPC , price) values (%s,%s, %s)'
        value = (row['name'], row['epc'],  float(row['price']))
        seed(sql, value)




print(row)
{'first_name': 'John', 'last_name': 'Cleese'}