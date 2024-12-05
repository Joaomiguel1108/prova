def soma(a, b):
    print(f"A soma de {a} + {b} é igual a {a + b}")

def subtracao(a, b):
    print(f"A subtração de {a} - {b} é igual a {a - b}")

def multiplicacao(a, b):
    print(f"A multiplicação de {a} x {b} é igual a {a * b}")

def divisao(a, b):
    if b == 0:
        print("Não é possível dividir por zero.")
    else:
        print(f"A divisão de {a} por {b} é igual a {a / b}")
sair = 0

while sair >= 0:
    a = float(input("Digite um número: "))
    b = float(input("Digite outro número: "))
    conta = int(input("Escolha: \n [1] soma \n [2] subtração \n [3] multiplicação \n [4] divisão \n [5] potência \n [6] raiz \n [-1] sair\n"))

    if conta == 1:
        soma(a, b)
    elif conta == 2:
        subtracao(a, b)
    elif conta == 3:
        multiplicacao(a, b)
    elif conta == 4:
        divisao(a, b)
    elif conta == 5:
        potencia(a, b)
    elif conta == 6:
        raiz_quadrada(a, b)
    elif conta == -1:
        print("Obrigado por utilizar o nosso sistema, até mais!!!")
        break
    else:
        print("Por favor, digite uma opção válida!!!\n")
            
        sair = int(input("Posso ajudar em algo mais? \n\n [0] SIM [-1] NÃO\n"))
            
    if sair == -1:
        print("Obrigado por utilizar o nosso sistema, até mais!!!")
