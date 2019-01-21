#-*-coding:utf8;-*-
#qpy:3
#qpy:console

num = 1
while True: #or use while(1):
    num += 1
    print(num)
    if num == 15:
       print('Deu por hoje!')
       break

for num in range(11,1,-1):
    print(num)


for i in range(5):
    print('Dieny')

for num in range(1,11):
    print(num)

tamanhoemmetros = float(input('Digite a altura da sua casa '))
centimetros = tamanhoemmetros*100
milimetros = centimetros*100
print('A altura da casa em metros é {:.3f}, em centimetros é {:.3f} e '
      'em milimetros é {:.3f}'.format(tamanhoemmetros, centimetros, milimetros))


nota1 = float(input('Digite a primeira nota '))
nota2 = float(input('Digite a segunda nota '))
media = (nota1 + nota2) / 2
print ('A media final é {:.2f}'.format(media))


letramusica = 'O nome dela é Jenifer'
tipodemusica = 'Ruim' if 'Jenifer' in letramusica else 'Boa'
print (tipodemusica)


numero=int(input('Digite um número '))
resultado1 = numero + numero
print(resultado1)
resultado2 = numero * 3
print (resultado2)
resultado3 = numero**0.5
print (resultado3)


numero=int(input('Digite um número '))
numero+=1
print(numero)
numero-=2
print(numero)


descobrirvariavel=input('Sua variável ')
tipodavar=type(descobrirvariavel)
print('Tipo da sua variável {}'.format(tipodavar))


#Exercicio 1
nome=input('Qual seu nome? ')
print('O nome dela é ' + nome)

#Exercicio 2
dia=input('Qual o dia do seu aniversário? ')
mes=input('Mes? ')
ano=input('Ano? ')

print(dia, '/', mes, '/', ano)

#Exercicio 3
num1=input('Primeiro número')
num2=input('Segundo número')
 
 
print('A soma dos números é: ', int(num1)+int(num2))