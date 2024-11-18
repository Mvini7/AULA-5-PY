def media(lista):
    return sum(lista) / len(lista)

notas = []

while True:
    menu = str(input("""
    1 - Adicionar nota
    2 - Calcular média
    0 - Sair

    """))

    match menu:
        case "1":
            nota = float(input("Digite uma nota: "))
            notas.append(nota)
            print('Nota adicionada com sucesso!')
        
        case "2":
            if len(notas) == 0:
                print("Lista vazia!")

            else:
                print(f"A média das notas é de: {media(lista=notas):.2f}")
        
        case "0":
            print("Programa encerrado!")
            break
        
        case _:
            print("Opção inválida! Por favor, selecione uma opção válida!")
