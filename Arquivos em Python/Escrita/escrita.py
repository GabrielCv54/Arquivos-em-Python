text= 'Frase sendo escrita nessa variável'
with open('arquivo.txt','w') as escrita :
   escrita.write(text)
   

strings=['como','falar','em','inglês']
with open('Frase sendo escrita nessa variável.txt','a') as r:
    r.writelines(strings)
     
t2 = text + '\n'
strings2=[f'{linha}\n'for linha in strings]
with open('arquivo2.txt','w') as t:
      t.write (t2)
      t.writelines(strings2)


vazio=[]
for linha in strings2:
     vazio.append(f'{linha}\n')