#idade = int(input("digite sua idade: "))

#if idade >= 18:
    #print("liberado")
#else:
    #print("banido")

salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <= 6000:
    print("programador pleno")
elif salario > 6000 and salario <= 15000:
    print("programador senior")
else:
    print("gerente de projetos")