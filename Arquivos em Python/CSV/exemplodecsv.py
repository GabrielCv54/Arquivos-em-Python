import csv

with open('dados.csv','r') as csv:
    read_csv = csv.reader(csv)
    for linha in read_csv:
        print(linha)