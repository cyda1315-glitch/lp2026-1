'''
Exercícios sobre os comandos básicos em Python
'''

#1. Faça um programa que imprima o seu nome.
def q1():
   print ('João paulo')


#2. Faça um programa que imprima o produto dos valores 30 e 27.
def q2():
    print(30*27)

#3. Faça um programa que imprima a média aritmética entre os números 5, 8, 12.
def q3():
    media = (5+8+12)/3
    print(f'(5+8+12)/3 = {media}')


#4. Faça um programa que leia e imprima um número inteiro.
def q4():
    numero = 0
    try:
        numero = int(input('Digite um número inteiro:'))
        print(f' Você digitou: {numero}')
    except ValueError:
        print('O valor digitado é inválido! Apaenas valores inteiros são aceitos. Tente novamente.')
    except:
        print('Erro desconhecido! Contrate o administrador do sistema.')


#5. Faça um programa que leia dois números reais e os imprima.
def q5():
    num1 = float(input('Digite um número real: '))
    num2 = float(input('Digite outro número real: '))
    print( f'Os números digitados foram: {num1:.f} e {num2:.f}')


#6. Faça um programa que leia um número inteiro e imprima o seu
#   antecessor e o seu sucessor.
def q6():
    numero = int(input('Digite um númerro inteiro: "))
    antecessor = numero - 1
    sucessor = numero + 1
    print("O número antecessor é: ", antecessor)
    print("O sucessor é:",sucessor)


#7. Faça um programa que leia o nome o endereço e o telefone de
#   um cliente e ao final, imprima esses dados.
def q7():
    nome = input("Digite o nome do cliente: ")
    endereco = input("Digite o endereço do cliente: ")
    telefone = input(Digite o telefone do cliente: ")
    print("Dados do cliente")
    print("Nome:", nome)
    print(Endereço:", endereco)
    print(Telefone:", telefone)


#8. Faça um programa que leia dois números inteiros e imprima a
#   subtração deles.
def q8():
    n1 = int(input("Digite o primeiro número inteiro: "))
    n2 = int(input("Digite o segundo número inteiro: "))
    subtracao = n1 - n2
    print("A subtração é:", subtracacao )


#9. Faça um programa que leia um número real e imprima ¼ deste número.
def q9():
    numero_real = float(input("Digite um número real: ")
    percentual = numero_real / 100
    print("O percentual do número é: {percentual}")


#10. Faça um programa que leia três números reais e calcule a
#    média aritmética destes números. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q10():
    n1 = float(input("Digite o 1° número real: "))
    n2 = float(input("Digite o 2° número real: "))
    n3 = float(input("Digite o 3° número real: "))
    media = (n1 + n2 + n3) / 3
    print("A média é:", media)


#11. Faça um programa que leia dois números reais e calcule as
#    quatro operações básicas entre estes dois números, adição,
#    subtração,multiplicação e divisão. Ao final, o programa
#    deve imprimir os resultados dos cálculos.
def q11():
    n1 = float(input("Digite o 1° número real: "))
    n2 = float(input("Digite o 2° número real: "))
    adicao = n1 + n2 
    subtracao = n1 - n2
    multiplicacao = n1 / n2 
    print("Adição:", adicao)
    print("Subtração:", subtracao)
    print("Multiplicação:", multiplicacao)
    print("Divisão:", divisao)

#12. Faça um programa que leia um número real e calcule o
#    quadrado deste número. Ao final, o programa deve
#    imprimir o resultado do cálculo.
def q12():
    numero = float(input("Digite um número real: "))
    quadrado = numero ** 2
    print(O quadrado do número é:", quadrado)


#13. Faça um programa que leia o saldo de uma conta poupança e
#    imprima o novo saldo, considerando um reajuste de 2%.
def q13():
    saldo = float(input("Digite o saldo da conta: "))
    reajuste = saldo * 0.02
    novo_saldo = saldo + reajuste
    print("O novo saldo é:", novo_saldo)

#14. Faça um programa que leia a base e a altura de um retângulo
#    e imprima o perímetro (base*2 + altura*2) e a área (base * altura).    
def q14():
    base = float(input("Digite a base do retângulo: "))
    altura = float(input("Digite a altura do retângulo: "))
    perimetro = (base * 2) + (altura * 2)
    area = base * altura
    print("O perimetro do retângulo é:", perimetro)
    print("A área do retângulo é:", area)
 

#15. Faça um programa que leia o valor de um produto, o percentual
#    do desconto desejado e imprima o valor do desconto e o valor
#    do produto subtraindo o desconto.
def q15():
  valor_produto = float(input("Digite o valor do produto: "))
  percentual_desconto = float(input("Digite o percentual de desconto que deseja: "))
  valor_desconto = valor_produto * (percentual_desconto / 100)
  valor_final = valor_produto - valor_desconto 
  print("O valor do desconto é:", valor_desconto)
  print("O valor final do produto é:", valor_final)
  

#16. Faça um programa que calcule o reajuste do salário de um
#    funcionário. Para isso, o programa deverá ler o salário atual
#    do funcionário e ler o percentual de reajuste. Ao final imprimir
#    o valor do novo salário.
def q16():
    salario = float(input("Digite seu salário atual: "))
    percentual_reajuste = float(inpt("Digite o percentual do reajuste: "))
    reajuste = salario * (percentual_reajuste / 100
    novo_salario = salario + reajuste
    print("Seu novo salário é:", novo_salario


#17. Faça um programa que calcule a conversão entre graus centígrados
#    e Fahrenheit. Para isso, leia o valor em centígrados e calcule
#    com base na fórmula a seguir. Após calcular o programa deve
#    imprimir o resultado da conversão.
#    F = (9 x C + 160) / 5
def q17():
    celsius = float(input("Digite a temperatura em celsius: "))
    fahrenheit = (9 * celsius + 160) / 5	
    print("A temperatura em Fahrenheit é:", fahrenheit)


#18. Faça um programa que calcule a quantidade de litros de combustível
#    consumidos em uma viagem, sabendo-se que o carro tem autonomia de
#    12 km por litro de combustível. O programa deverá ler o tempo
#    decorrido na viagem e a velocidade média e aplicar as fórmulas:
#    D = T x V       L = D / 12
#    Em que:
#    • D = Distância percorrida
#    • T = Tempo
#    • V = Velocidade média
#    • L = Litros de combustível consumidos
#    Ao final, o programa deverá imprimir a distância percorrida e a
#    quantidade de litros consumidos na viagem.
def q18():
    tempo = float(input("Digite o tempo da viagem: "))
    velocidade_media = float(input("Digite a velocidade em Km/h: "))
    distancia = tempo * velocidade_media
    litros_consumidos = distancia / 12
    print("Distância percorrida é:", distancia, "km")
    print("Litros de combustivel consumidos:", litros_consumidos, "L")


#19. Faça um programa que calcule o valor de uma prestação em atraso.
#    Para isso, o programa deve ler o valor da prestação vencida, a
#    taxa periódica de juros e o período de atraso. Ao final, o
#    programa deve imprimir o valor da prestação atrasada, o período
#    de atraso, os juros que serão cobrados pelo período de atraso, o
#    valor da prestação acrescido dos juros. Considere juros simples.
def q19():
    valor_prestacao = float(input("Digite o valor da prestação em atraso: "))
    taxa_juros = float(input("Digite a taxa de juros: "))
    periodo_atraso = float(input("Digite o período de atraso: "))
    juros_cobrados = valor_prestacao + juros_cobrados
    print(f"\njuros a serem cobrados pelo período de atraso: R$ {juros_cobrados}")
    print(f"valor da prestação com o juros: R${valor_final})


#20. Faça um programa que efetue a apresentação do valor da conversão
#    em real (R$) de um valor lido em dólar (US$). Para isso, será
#    necessário também ler o valor da cotação do dólar.
def q20():
    valor_dolar = float(input("Digite o valor do dólar: "))
    catacao_dolar = float(input("Digite a cotação do dólar para real (R$): "))
    valor_real = valor_dolar * cotacao_dolar
    print(f"O valor de US${valor_dolar:} convertendo para real é de R${valor_real})