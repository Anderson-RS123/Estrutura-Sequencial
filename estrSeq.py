# python Brasil: estrutura sequencial
# https://wiki.python.org.br/EstruturaSequencial

def option(opcao_escolhida):
    mostrar_opcoes()
    while opcao_escolhida != 0:
        opcao_escolhida = int(input("Escolha uma opção para resolução ou digite 0 para sair do programa: "))
        match opcao_escolhida:
                case 0:
                    break
                case 1:
                    opcao1()
                case 2: 
                    pedir_numero()
                case 3:
                    soma_dois_numeros()
                case 4:
                    media_bimestre()
                case 5:
                    metros_para_cm()
                case 6:
                    area_do_circulo()
                case 7:
                    dobro_area_do_quadrado()
                case 8:
                    salario_mes()
                case 9:
                    fahrenheit_para_celsius()
                case 10:
                    celsius_para_fahrenheit()
                case 11:
                    nums_int_e_Real()
                case 12:
                    peso_ideal()
                case 13:
                    peso_ideal_HM()
                case 14:
                    peixe_multa()
                case 15:
                    salario_liquido()
                case 16:
                    latas_de_tinta()
                case 17:
                    latas_de_tinta2()
                case 18:
                    tempo_download()
        print("******************************")
        print("******************************")

def mostrar_opcoes():
    print("1- Mostrar Hello Word na tela")
    print("******************************")
    print("2- Pedir um número e mostrar na tela")
    print("******************************")
    print("3- Faça um Programa que peça dois números e imprima a soma")
    print("******************************")
    print("4- Faça um Programa que peça as 4 notas bimestrais e mostre a média")
    print("******************************")
    print("5- Faça um Programa que converta metros para centímetros")
    print("******************************")
    print("6- Faça um Programa que peça o raio de um círculo, calcule e mostre sua área") 
    print("******************************")
    print("7- Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário")
    print("******************************")
    print("8- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês")
    print("******************************")
    print("9- Faça um Programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).")
    print("******************************")
    print("10- Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit")
    print("******************************")
    print("11- Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:  a.  o produto do dobro do primeiro com metade do segundo. b. a soma do triplo do primeiro com o terceiro.  c. o terceiro elevado ao cubo.")
    print("******************************")
    print("12- Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58")
    print("******************************")
    print("13- Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:Para homens: (72.7*h) - 58     Para mulheres: (62.1*h) - 44.7")
    print("******************************")
    print("14- João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso. Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. Imprima os dados do programa com as mensagens adequadas.")
    print("******************************")
    print("15- Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:   salário bruto.     quanto pagou ao INSS.       quanto pagou ao sindicato.     o salário líquido.")
    print("******************************")
    print("16- Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.")
    print("******************************")
    print("17- Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.   Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:   comprar apenas latas de 18 litros;   comprar apenas galões de 3,6 litros;    misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.")
    print("******************************")
    print("18- Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).")
    print("******************************")

def opcao1():
    return print("Hello Word")

def pedir_numero():
    numero_pedido = int(input("Digite um número: "))
    return print(f"O numero digitado é: {numero_pedido}")
 
def soma_dois_numeros():
    num1 = int(input("Digite um numero:"))
    num2 = int(input("Digite outro numero:"))
    return print(f"A soma dos numeros {num1} e {num2} é: {num1 + num2}")

def media_bimestre():
    notas_bimestre = []
    for num_nota in range(1,5):
        notas_bimestre.append(float(input(f"Informe a nota {num_nota} do aluno:")))
    return print(f"A média das quatro notas do bimestre é: {sum(notas_bimestre) / len(notas_bimestre)}")

def metros_para_cm():
    return print(f"{float(input("Digite o valor em Metros: ")) * 100} é a medida desse valor em centímetros.")

def area_do_circulo():
    area_C = float(input("Digite o raio do circulo: "))
    return print(f"A área do circulo é: {3.14 * (area_C* area_C)}.")

def dobro_area_do_quadrado():
    area_Q = float(input("Digite o valor de um lado do quadrado: "))
    return print(f"O dobro da área deste quadrado é: {(area_Q * area_Q) * 2 }")

def salario_mes():
    salario_hora = float(input("Qual o seu salário por hora: "))
    dias_trabalhados = int(input("Quantas horas trabalhou neste mes: "))
    return print(f"O seu salário neste mês é de R${salario_hora * dias_trabalhados}.")

def fahrenheit_para_celsius():
    return print(f" {round(((float(input("Digite a temperatura em fahrenheit: ")) - 32) / 9) * 5,1)}°C é a temperatura em celsius.")

def celsius_para_fahrenheit():
    return print(f"{round((float(input("Digite a temperatura em Celsius: ")) * 1.8) + 32,1)}°F é a temperatura em Fahrenheit.")

def nums_int_e_Real():
    num1 = int(input("Digite um numero inteiro: "))
    num2 = int(input("Digite outro numero inteiro: "))
    num_real = float(input("Digite qualquer tipo de numero: "))
    return print(f"Resposta A: o produto do dobro do primeiro com metade do segundo:{(num1 * 2) * (num2 / 2)},\nResposta B: a soma do triplo do primeiro com o terceiro:{(num1 * 3) + num_real},\nResposta C: o terceiro elevado ao cubo:{num_real ** 3}.")

def peso_ideal():
    return print(f"{round((float(input("Qual a sua altura em metros: ")) * 72.7) - 58,1)}\n Kg é o sue peso ideal.")

def peso_ideal_HM():
    altura = float(input("Qual a sua altura em metros: "))
    return print(f"Peso ideal para homens:{round((72.7 * altura) - 58,1)}\nPeso ideal para mulheres:{round((62.1 * altura) - 44.7,1)}.")

def peixe_multa():
    excesso = []
    peso = 1
    while peso != 0:
        peso = float(input("Qual o peso do peixe em Kg ou digite 0 para sair:"))
        excesso.append(peso - 50) if peso > 50 else print()
    return print(f"O valor da multa que vai ser preciso ser paga é de R${sum(excesso) * 4}.")

def salario_liquido():
    salario = float(input("Qual o seu salario por hora:"))
    horas = int(input("Quantas horas voce trabalhou este mes:"))
    salario_bruto = salario * horas
    ir = 11 / 100 * salario_bruto
    inss = 8 / 100 * salario_bruto
    sindicato = 5 / 100 * salario_bruto
    liquido = salario_bruto - ir - inss - sindicato
    return print(f"O seu saláiro bruto é de R${salario_bruto}\nO imposto de renda é de R${ir}\nO imposto do INSS é de R${inss}\nO imposto do sindicato é de R${sindicato}\nO seu salário liquido é de R${liquido}.")

def latas_de_tinta():
    area_pintada = float(input("Qual a area em m³ que vai ser pintado:"))
    qtd_latas = (area_pintada // (18 * 3)) + 1
    return print(f"Para pintar {area_pintada} m³ voce vai precisar de {qtd_latas} latas de tinta e vai gastar R${qtd_latas * 80}.")

def latas_de_tinta2():
    area_para_pintar = float(input("Qual a area que quer pintar:"))
    latas_grandes = ((area_para_pintar) // (18 * 6)) + 1
    latas_pequenas = ((area_para_pintar) // (3.6 * 6)) + 1
    area_para_pintar2 = area_para_pintar
    contador_lata_grande = 0
    contador_lata_pequena = 0
    while area_para_pintar >= (18 * 6):
        area_para_pintar = area_para_pintar - (18 * 6)
        contador_lata_grande = contador_lata_grande + 1
    while area_para_pintar >= (3.6 * 6):
        area_para_pintar = area_para_pintar - (3.6 * 6)
        contador_lata_pequena = contador_lata_pequena + 1
    if area_para_pintar != 0:
        contador_lata_pequena = contador_lata_pequena + 1
    return print(f"Para pintar {area_para_pintar2} m³, vai ser necessário comprar um das seguintes opções:\n1: {latas_grandes} latas de 18L gastando R${latas_grandes * 80}.\n2: {latas_pequenas} latas de 3,6L gastando R${latas_pequenas * 25}.\n3: {contador_lata_grande} latas de 18L e {contador_lata_pequena} latas de 3,6L, gastando R${(contador_lata_grande * 80) + (contador_lata_pequena * 25)}.")

def tempo_download():
    tamanho = float(input("Qual o tamanho do arquivo em Mb:"))
    velocidade = float(input("Qual a velocidade da internet em Mbps:"))
    return print(f"O tempo para baixar esse arquive é de aproximadamente {round((tamanho / velocidade) / 60, 2)} minutos.")

option(1)