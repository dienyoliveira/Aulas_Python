#-*-coding:utf8;-*-
#qpy:3
#qpy:console

#Exercicio 3

resultado = 0
qtd = 0

while True:
    num = int(input('Digite o primeiro número: '))

    if num == 999:
        print('Foram digitados {} números, e a soma deles foi {}!'.format
              (qtd, resultado))
        break
    else:
        resultado += num
        qtd += 1
