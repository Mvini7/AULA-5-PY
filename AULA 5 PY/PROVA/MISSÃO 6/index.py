print("Tente sair da masmorra!")

lista = []

for i in range(10, 31):
        
    if i % 2 > 0:
        lista.append(i)

print(lista)
print("Esses são os numeros primos entre 10 e 30!")
print("Um desses numeros te liberta da masmorra!")

while True:

    numeros = int(input("Digite um numero entre 10 e 30 que seja primo para sair da masmorra: "))

    if numeros == 21:
        print("Você estar livre da masmorra!")
        break
    else:
        print("Tente Novamente!")

    if numeros in lista:
        continue
    else:
        print("Numero invalido, tente novamente (digite um numero entre 10 e 30)")
