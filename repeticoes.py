notas = []

#for x in range(5):
    #codigo_aluno = input("RM: ")
    #nota = float(input("Nota: "))
    #resultado = [codigo_aluno, nota]
    #notas.append(resultado)

contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    #alternativa: contador += 1
    contador = contador + 1

print( "quantidade de notas", len(notas))

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota", nota)

