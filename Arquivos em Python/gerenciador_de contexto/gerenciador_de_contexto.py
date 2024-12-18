with open('testearquivo2.txt','w') as p:
    p.write('Ja deu tudo certo\n')
    print(f'(dentro do bloco with) arquivo fechado? {p.closed}')

print(f'(fora do bloco with) arquivo fechado? {p.closed}')