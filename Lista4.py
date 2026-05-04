import random
from util import inputint, inputfloat, gerar_palavra
'''
Lista de Exercícios referentes a coleções e arquivos em python
'''
VERMELHO = '\033[31m'
VERDE = '\033[32m'
RESET = '\033[m'


#1. Faça um programa que armazene 15 números inteiros em uma lista e depois
#permita que o usuário digite um número inteiro para ser buscado na lista, se
#for encontrado o programa deve imprimir a posição desse número na lista, caso
#contrário, deve imprimir a mensagem: "Nao encontrado!".
def q1() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(15)]
    #forma extensa da linha anterior:
    #for _ in range(15):
    #    numeros.append(random.randrange(200))

    print(numeros)
    numero: int = inputint('Digite o número a ser localizado na lista: ')
    try:
        posicao: int = numeros.index(numero)
    except ValueError:
        print('Número não encontrado!')
    else:
        print(f'Número localizado na posição: {posicao}')

#2. Faça um programa que armazene 10 letras em uma lista e imprima uma listagem
#numerada. (ASCII 65-90)
def q2() -> None:
    letras: list[str] = [chr(random.randrange(65,91)) for _ in range(10)]
    # tipo enumerate cria automaticamente um contador para os elementos da lista começando em 0
    for posicao, letra in enumerate(letras):
        print(f'[{posicao}]: {letra}')

#2.1 Faça um programa que peça ao usuário para informar a qtde de caracteres
# para a geração de uma senha aleatória. Ao final o programa deve exibir a
# senha sugerida. (ASCII 40-126)
def q21() -> None:
    tamanho_senha: int = inputint('Informe a qtde de caracteres para senha (4-32): ', min=4, max=32)
    senha: list[str] = [chr(random.randrange(40,127)) for _ in range(tamanho_senha)]
    print(f'Senha gerada: {"".join(senha)}')

#3. Construa uma programa que armazene 15 números em uma lista e imprima
#uma listagem numerada contendo o número e uma das mensagens: par ou ímpar.
def q3() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(15)]
    for posicao, numero in enumerate(numeros):  
        print(f'[{str(posicao):<2}]: {str(numero):>3} ({"PAR" if numero%2==0 else "IMPAR"})')

#4. Faça um programa que armazene 8 números em uma lista e imprima todos os
#números. Ao final, imprima o total de números múltiplos de seis.
def q4() -> None:
    numeros: list[int] = [random.randrange(200) for _ in range(8)]
    print(numeros)
    multiplos6: int = sum(1 for n in numeros if n % 6 == 0)
    print(f'Qtde de números que são múltiplos de 6: {multiplos6}')

#5. Faça um programa que armazene as notas das provas 1 e 2 de 15 alunos. Calcule
#e armazene a média arredondada. Armazene também a situação do aluno: 1-
#Aprovado ou 2-Reprovado. Ao final o programa deve imprimir uma listagem
#contendo as notas, a média e a situação de cada aluno em formato tabulado.
#Utilize quantas listas forem necessárias para armazenar os dados.
def q5() -> None:
    alunos: list[dict] = []
    for c in range(1,16):
        aluno: dict = dict()
        aluno['matricula'] = c
        aluno['nome']: str = gerar_palavra(max=5)
        aluno['nota1']: float = round(random.random()*10,1)
        aluno['nota2']: float = round(random.random()*10,1)
        aluno['media']: float = round((aluno["nota1"] + aluno["nota2"])/2,1)
        aluno['situacao']: str = "Aprovado" if aluno["media"] >= 6 else "Reprovado"
        alunos.append(aluno)
        #percorrer a lista de alunos para imprimir o diário
    print("MAT\tNOME\tN1\tN2\tN2\tMD\tST")
    for aluno in alunos:
        print(f'{aluno["matricula"]}\t{aluno["nome"]}\t{aluno["nota1"]}\t{aluno["nota2"]}\t{aluno["media"]}\t{aluno["situacao"]}')


#6. Construa um programa que permita armazenar o salário de 20 pessoas. Calcular
#e armazenar o novo salário sabendo-se que o reajuste foi de 8%. Imprimir uma
#listagem numerada com o salário e o novo salário. Declare quantas listas forem
#necessárias.
def q6() -> None:
    salarios: list[float] = []
    novos_salarios: list[float] = []

    # gerar 20 salários aleatórios (ou você pode usar input)
    for _ in range(20):
        salario = round(random.uniform(1000, 5000), 2)
        salarios.append(salario)
        novo = round(salario * 1.08, 2)  # reajuste de 8%
        novos_salarios.append(novo)

    print("POS\tSALARIO\tNOVO SALARIO")
    for i, (s, n) in enumerate(zip(salarios, novos_salarios)):
        print(f'{i}\t{s:.2f}\t\t{n:.2f}')

#7. Crie um programa que leia o preço de compra e o preço de venda de 100 mercadorias
#(utilize listas). Ao final, o programa deverá imprimir quantas mercadorias
#proporcionam:
#• lucro < 10%
#• 10% <= lucro <= 20%
#• lucro > 20%
def q7() -> None:
    compra: list[float] = []
    venda: list[float] = []

    lucro_menor_10 = 0
    lucro_entre_10_20 = 0
    lucro_maior_20 = 0

    for _ in range(100):
        pc = round(random.uniform(10, 100), 2)
        pv = round(random.uniform(10, 150), 2)

        compra.append(pc)
        venda.append(pv)

        lucro = ((pv - pc) / pc) * 100

        if lucro < 10:
            lucro_menor_10 += 1
        elif 10 <= lucro <= 20:
            lucro_entre_10_20 += 1
        else:
            lucro_maior_20 += 1

    print("RESULTADO:")
    print(f'Lucro < 10%: {lucro_menor_10}')
    print(f'Lucro entre 10% e 20%: {lucro_entre_10_20}')
    print(f'Lucro > 20%: {lucro_maior_20}')

#8. Construa um programa que armazene o código, a quantidade, o valor de compra
#e o valor de venda de 30 produtos. A listagem pode ser de todos os produtos ou
#somente de um ao se digitar o código. Utilize dicionário como estrutura de dados.
def q8() -> None:
    produtos: list[dict] = []

    # cadastro dos 30 produtos
    for c in range(1, 31):
        produto: dict = {}
        produto["codigo"] = c
        produto["quantidade"] = random.randint(1, 100)
        produto["valor_compra"] = round(random.uniform(10, 100), 2)
        produto["valor_venda"] = round(random.uniform(10, 150), 2)

        produtos.append(produto)

    print("1 - Listar todos os produtos")
    print("2 - Buscar produto por código")
    opcao = inputint("Escolha uma opção: ", min=1, max=2)

    if opcao == 1:
        print("COD\tQTD\tCOMPRA\tVENDA")
        for p in produtos:
            print(f'{p["codigo"]}\t{p["quantidade"]}\t{p["valor_compra"]:.2f}\t{p["valor_venda"]:.2f}')

    else:
        cod = inputint("Digite o código do produto: ")

        encontrado = False
        for p in produtos:
            if p["codigo"] == cod:
                print("Produto encontrado:")
                print("COD\tQTD\tCOMPRA\tVENDA")
                print(f'{p["codigo"]}\t{p["quantidade"]}\t{p["valor_compra"]:.2f}\t{p["valor_venda"]:.2f}')
                encontrado = True
                break

        if not encontrado:
            print("Produto não encontrado!")

#9. Faça um programa que leia dois conjuntos de números inteiros, tendo
#cada um 10 elementos. Ao final o programa deve listar os elementos comuns aos
#conjuntos.
def q9() -> None:
    lista1: list[int] = []
    lista2: list[int] = []

    print("Digite os 10 valores da lista 1:")
    for _ in range(10):
        lista1.append(inputint("Número: "))

    print("\nDigite os 10 valores da lista 2:")
    for _ in range(10):
        lista2.append(inputint("Número: "))

    # usando conjunto para encontrar interseção
    comuns = set(lista1) & set(lista2)

    print("\nElementos comuns:")
    if comuns:
        print(comuns)
    else:
        print("Nenhum elemento em comum.")

#10. Faça um programa que leia uma lista com 10 elementos e obtenha outra lista resultado
#cujos valores são os fatoriais da lista original.
#Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
def q10() -> None:
    lista_original: list[int] = []
    lista_fatoriais: list[int] = []
    
    print("Digite 10 números inteiros para calcular seus fatoriais:")
    
    for i in range(10):
        num = inputint(f'Digite o {i+1}º número: ')
        lista_original.append(num)
        
        fatorial = math.factorial(num)
        lista_fatoriais.append(fatorial)

    
    maior: int = lista_fatoriais[0]
    menor: int = lista_fatoriais[0]
    soma: int = 0
    pares: int = 0

    for f in lista_fatoriais:
        if f > maior:
            maior = f
        if f < menor:
            menor = f
        
        soma += f
        
        if f % 2 == 0:
            pares += 1

    media = soma / len(lista_fatoriais)
    percentual_pares = (pares / len(lista_fatoriais)) * 100

    print("\n" + "="*30)
    print(f"Lista Original: {lista_original}")
    print(f"Lista de Fatoriais: {lista_fatoriais}")
    print("-" * 30)
    print(f"Maior fatorial: {maior}")
    print(f"Menor fatorial: {menor}")
    print(f"Média dos elementos: {media:.2f}")
    print(f"Percentual de números pares: {percentual_pares:.1f}%")
    print("="*30)

#11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
#média dos elementos da lista.
# 11. Imprimir o maior e o menor, sem ordenar, o percentual de números pares e a
# média dos elementos da lista.
def q11() -> None:
    # Definindo uma lista de 10 elementos (ou a quantidade que preferir)
    numeros: list[int] = []
    
    print("Digite 10 números inteiros para análise:")
    for i in range(10):
        numeros.append(inputint(f'Digite o {i+1}º número: '))

    # Inicializamos as variáveis de controle
    # Usamos o primeiro elemento da lista para evitar problemas com valores nulos
    maior: int = numeros[0]
    menor: int = numeros[0]
    soma: int = 0
    contagem_pares: int = 0
    total_elementos: int = len(numeros)

    for n in numeros:
        # Lógica para Maior e Menor (sem usar sort/sorted)
        if n > maior:
            maior = n
        if n < menor:
            menor = n
        
        # Acúmulo para a média
        soma += n
        
        # Verificação de pares
        if n % 2 == 0:
            contagem_pares += 1

    # Cálculos finais
    media = soma / total_elementos
    percentual_pares = (contagem_pares / total_elementos) * 100

    # Saída formatada
    print("\n" + "="*40)
    print(f"LISTA ANALISADA: {numeros}")
    print("-" * 40)
    print(f"Maior valor encontrado: {maior}")
    print(f"Menor valor encontrado: {menor}")
    print(f"Média dos elementos:    {media:.2f}")
    print(f"Percentual de pares:    {percentual_pares:.1f}%")
    print("="*40)

#12. Crie um programa para gerenciar um sistema de reservas de mesas em uma casa
#de espetáculo. A casa possui 30 mesas de 5 lugares cada. O programa deverá
#permitir que o usuário escolha o código de uma mesa (1 a 30) e forneça a
#quantidade de lugares desejados. O programa deverá informar se foi possível
#realizar a reserva e atualizar a reserva. Se não for possível, o programa deverá
#emitir uma mensagem. O programa deve terminar quando o usuário digitar
#o código 0 (zero) para uma mesa ou quando todos os 150 lugares estiverem
#ocupados.

#13. Construa um programa que realize as reservas de passagens áreas de uma companhia.
#O programa deve permitir cadastrar o número de 10 voos e definir a
#quantidade de lugares disponíveis para cada um. Após o cadastro, leia vários
#pedidos de reserva, constituídos do número da carteira de identidade do cliente e
#do número do voo desejado. Para cada cliente, verificar se há possibilidade no
#voo desejado. Em caso afirmativo, imprimir o número da identidade do cliente e
#o número do voo, atualizando o número de lugares disponíveis. Caso contrário,
#avisar ao cliente a inexistência de lugares. A leitura do número 0 (zero) para o voo
#desejado indica o término da leitura de reservas.

#14. Faça um programa que armazene 50 números inteiros em uma lista. O programa
#deve gerar e imprimir uma segunda lista em que cada elemento é o quadrado do
#elemento da primeira lista.

#15. Faça um programa que leia e armazene vários números, até digitar o número
#0. Imprimir quantos números iguais ao último número foram lidos. O limite de
#números é 100.

#16. Crie um programa para ler um conjunto de 100 números reais e informe:
#• quantos números lidos são iguais a 30
#• quantos são maior que a média
#• quantos são iguais a média

#17. Faça um programa que leia um conjunto de 30 valores inteiros, armazene-os em
#uma lista e os imprima ao contrário da ordem de leitura.

#18. Faça um programa que permita entrar com 20 valores numéricos,
# em que podem existir vários elementos repetidos. Gere
#uma lista ordenada que terá apenas os elementos não repetidos.

#19. Suponha uma estrutura de 30 elementos contendo: código e telefone. Faça
#um programa que permita buscar pelo código e imprimir o telefone.

#20. Faça um programa que leia a matrícula e a média de 100 alunos. Ordene da maior
#para a menor nota e imprima uma relação contendo todas as matrículas e médias.

questao = int(input('Questão a ser executada: '))
eval(f'q{questao}()')