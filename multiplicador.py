

encendido = True

while encendido:
    print("                              ")
    print("Bienvenido al SuperMultiplicador")

    while True:
        print("                              ")
        a = input("ingresa el multiplicando del cual quieres ver sus productos $")
        if a.isnumeric():
            a = int(a)
            break
        else:
            print("POR FAVOR,ingresa un numero valido")

    while True:
        b = input("ingresa un multiplicador $")
        if b.isnumeric():
            b = int(b)
            break
        else:
            print("POR FAVOR,ingresa un numero valido")

    print("                              ")
    print(f'para los numeros {a} y {b} los productos son:')
    print("                              ")
    multiplicador = range((b+1))
    for X in multiplicador:
        print(f'{a } X {X } = {a*X}')
    print("                              ")

    while True:
        respuesta = input("Desea realizar otra multiplicacion S/N ")
        if respuesta.lower() == "s":
            encendido = True
            break

        elif respuesta.lower() == "n":
            print("                              ")
            print("Gracias por utilizar el SuperMultiplicador !!!")
            encendido = False
            break
        else:
            print("Por favor, ingresa una opcion valida.")
