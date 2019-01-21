#-*-coding:utf8;-*-
#qpy:3
#qpy:console

# Exercícios 4

nomeproduto = ''
valorproduto = ''
vlrprodutomenorvalor = 0.0
nomeprodutomenorvalor = ''
qtdprd = 0
qtdprdmaior100 = 0
somaprodutos = 0

while True:
    nomeproduto = str(input('Digite o nome do produto comprado: '))
    valorproduto = float(input('Digite o valor do produto comprado: '))
    
    if valorproduto > 100:
        qtdprdmaior100 += 1
    if vlrprodutomenorvalor == 0:
        vlrprodutomenorvalor = valorproduto
        nomeprodutomenorvalor = nomeproduto
    elif vlrprodutomenorvalor >= valorproduto:
        vlrprodutomenorvalor = valorproduto
        nomeprodutomenorvalor = nomeproduto
    qtdprd += 1
    somaprodutos += valorproduto
        
    conduser = input('Deseja continuar inserindo produtos? Responda '
                     'S para Sim ou N para Não! ')
    conduser.upper()
    if conduser == 'S':
        continue
    elif conduser == 'N':
        print('Total gasto na loja: {}\n'.format(somaprodutos))
        print('Quantidade de Produtos que custam mais que R$ 100,'
              '00: {}\n'.format(qtdprdmaior100))
        print('Nome do produto de menor valor: {}'
              .format(nomeprodutomenorvalor))
        break

