import csv

with open('relatório.csv','r',newline='',
          encoding='utf-8') as arquivo_csv:
    leitor = csv.reader(arquivo_csv,delimiter=';')
    novo_relatório=[]
    for linha in leitor:
     novo_relatório.append(linha)

nova_coluna,*novo_relatório = novo_relatório
print(nova_coluna)
print('[',*novo_relatório,sep='\n',end='\n ]')

#with open('estoque.csv', 'r', newline='',
#ncoding='utf-8') as arquivo_csv:
#reader = csv.reader(arquivo_csv, delimiter=';')
#novo_estoque = list(reader)