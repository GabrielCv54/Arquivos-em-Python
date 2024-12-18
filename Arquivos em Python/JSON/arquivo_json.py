import json 

livro = {
 'Titulo':'Magnus Chase e os Deuses de Asgard',
 'Autor':'Rick riordan',
 'Ano de Publicação': 2015,
  'Série' : [
      {
      'Título':'Magnus Chase - A Espada do Verão',
      'Ano':2015,
      'Autor': 'Rick Riordan',
      },
      {
          'Título':'Magnus Chase- O Martelo de Thor',
          'Ano':2016,
          'Autor':'Rick Riordan'
      },
      {
         'Título':'Magnus Chase - O Navio dos Mortos',
          'Ano':2017,
          'Autor':'Rick Riordan'
      },

  ]

}

livro_str = json.dumps(livro,  indent=2)
print(livro_str)
with open('livro.json','w') as l:
    json.dump(livro, l, indent=2)


livro_carregado_da_string=json.loads(livro_str)
with open('livro.json','r')as lf:
    livro_carregado_do_arquivo = json.load(lf)

print(f'Comparação 1: {livro_carregado_do_arquivo == livro}')
print(f'Comparação 2: {livro_carregado_da_string == livro}  ')