import csv

colunas=[
    'Nome','Idade','Classificação','Aldeia'
    ]

linhas=[
    ['Naruto Uzumaki',17,'Genin','Aldeia da Folha'],
    ['Itachi Uchiha',21,'Renegado','Aldeia da Folha'],
    ['Gaara',18,'Kazekage','Aldeia da Areia'],
    ['Deidara',19,'Renegado','Aldeia da Pedra'],
     ['Sakura',16,'Chunin','Aldeia da Folha']
    ]


with open('relatório.csv','w',newline='',
          encoding='utf-8') as arquivo_csv:
    escrita = csv.writer(arquivo_csv, delimiter=';')
    escrita.writerow(colunas)
    escrita.writerows(linhas)

