texto='Escrevendo a primeira frase 3'
linhas=['Line 1','Line 2 ' ,'Line 3','Line 4']

with open('print.txt','w') as x:
  print(texto,file= x)
  for linha in linhas:
    print(linha,file=x)