def swtches():
    print('''
        ****** Bienvenidos a Pizza Master ******
        1. Pizzas
        2. Postres
        3. Ensaladas
        4. Bebidas
        5. Salir
    ''')
    opc = int(input('Ingrese la opcion: '))
    if opc == 1:
        print('***** Pizzas *****')
        print('''
            1. Pizza de peperoni
            2. Pizza de queso
            3. Pizza de jamon
            4. Pizza de pollo
            5. Pizza de carne
            6. Salir
        ''')
        opc = int(input('Ingrese la opcion: '))
        if opc == 1:
            print('Pizza de peperoni')
        elif opc == 2:
            print('Pizza de queso')
        elif opc == 3:
            print('Pizza de jamon')
        elif opc == 4:
            print('Pizza de pollo')
        elif opc == 5:
            print('Pizza de carne')
        elif opc == 6:
            print('Gracias por usar Pizza Master')
    elif opc == 2:
        print('CPostres')
    elif opc == 3:
        print('Ensaladas: ')
    elif opc == 4:
        print('Bebidas')
    elif opc == 5:
        print('Gracias por usar Pizza Master')

if  __name__ == '__main__':
    swtches()










    