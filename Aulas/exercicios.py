#-*-coding:utf8;-*-
#qpy:3
#qpy:consol

opcao = '4'
num1 = 0
num2 = 0

while True:
    frase = 'O resultado é'
    if opcao == '0':
       opcao = input ('Escolha uma opção:\n1: Somar\n2: Multiplicar\n3: Maior número\n4: Digitar os números novamente\n5: Sair\n')
       
    elif opcao == '1':
       resultado = num1 + num2
       print ('{} {}'.format(frase, resultado))
       opcao = '0'
       
    elif opcao == '2':
       resultado = num1 * num2
       print ('{} {}'.format(frase, resultado))
       opcao = '0'
       
    elif opcao == '3':
       if num1 < num2:
          print ('{} {}'.format(frase, num2))
       elif num2 < num1:
          print ('{} {}'.format(frase, num1))
       else:
          print('Os números digitados são iguais!')
       opcao = '0'
       
    elif opcao == '4':
       num1 = int(input ('Digite o primeiro número: '))
       num2 = int(input ('Digite o segundo número: '))
       opcao = '0'
       
    elif opcao == '5':
       print('Saindo do programa, obrigada!')
       break
    else:
       print('Opção invalida!')
       opcao = '0'
       
       