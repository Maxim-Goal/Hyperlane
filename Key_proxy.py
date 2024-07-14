import csv
with open('key_proxy.csv') as f:
    file = csv.reader(f, delimiter=';')
    key_proxy = [i for i in file if i[1] != 'proxy']


