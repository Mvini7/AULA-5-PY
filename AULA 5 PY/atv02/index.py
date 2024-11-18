comprimento = float(input("Digite o comprimento do retangulo: "))
altura = float(input("Digite a altura do retangulo: "))

def area_do_retangulo():

    resultado = comprimento * altura
    return resultado


print(f"A area do retangulo é {area_do_retangulo()}")