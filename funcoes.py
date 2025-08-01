
def minha_funcao(valor1, valor2, operacao,):
    if (operacao == "+"):
        return valor1 + valor2
    elif(operacao == "-"):
        return valor1 - valor2
    elif(operacao == "*"):
        return valor1 * valor2
    elif(operacao == "/"):
        return valor1 / valor2
    else:
        print("operação não aceita")

while True:
    valor1 = int(input("Valor1: "))
    valor2 = int(input("Valor2: "))
    operacao = input("Digite qual operação deseja fazer(use '+' para adição, '-' para subtração, '*' para multiplicação e '/' para divisão)")

    resposta = minha_funcao(valor1, valor2, operacao)
    print(valor1, operacao, valor2, "=", resposta)

    