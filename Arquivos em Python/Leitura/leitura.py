#with open('arquivo.txt','r') as f:
 # print(f.tell())
 # f.seek(9)
  #print(f.tell())

#with open('arquivo.txt','r') as t:
   #texto = t.read()
   #print(texto)

#with open('arquivo.txt','r') as t:
#    linha1 = t.readline()
#    linha2 = t.readline()
#    linha3 = t.readline()
#    print(linha1,linha2,linha3)

with open('arquivo.txt','r' ) as t:
    leitura= t.readlines()
    print(leitura)