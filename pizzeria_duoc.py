# Sistema de pizeria de DuocUC
tipos_de_pizza = {
    'Tradicional': 12000,
    'Pepperoni': 14000,
    'All carnes': 17000
}

total_pedido = 0
pizzas_compradas = []
cantidad_pizzas_compradas = []
comprador = ''
descuento = 0
valor_descuento = 0
pedido_activo = 1


def calcular_descuento(total_pedido):
    if comprador == 'estudiante_diurno':
        return total_pedido * 0.12
    elif comprador == 'estudiante_vespertino':
        return total_pedido * 0.10
    elif comprador == 'administrativo':
        return 0


def calcular_precio_pizza(pizza, cantidad):
    return tipos_de_pizza[pizza] * cantidad


print('\n\t\t\t\tBienvenido a el menu RAPID de la Pizzeria DuocUC\n')
print('Si desea salir del programa en cualquier momento, ingrese "exit")\n')
print('Las pizzas disponibles son: \n')
for pizza in tipos_de_pizza:
    print(f'{pizza} = ${tipos_de_pizza[pizza]}')

while pedido_activo == 1:
    pizza = input('\nIngrese la pizza que desea comprar: ').capitalize()
    if pizza == 'Exit':
        print('Adios...')
        exit()
    if pizza not in tipos_de_pizza:
        print('La pizza ingresada no es valida')
        continue
    cantidad = int(input(f'\nIngrese la cantidad de pizzas {pizza} que desea comprar: '))

    try:
        if cantidad < 0:
            raise ValueError
    except ValueError:
        print('La cantidad ingresada no es valida')
        continue
    compra = calcular_precio_pizza(pizza, cantidad)
    total_pedido += compra
    pizzas_compradas.append(pizza)
    cantidad_pizzas_compradas.append(cantidad)
    otra_pizza = input('\n¿Desea agregar otra pizza? (S/N): ').lower()
    if otra_pizza == 'exit':
        print('Adios...')
        exit()
    elif otra_pizza == 's':
        continue
    elif otra_pizza == 'n':
        pedido_activo = 2
        if pedido_activo == 2:
            comprador = input(
                '\n¿Es usted estudiante diurno, estudiante vespertino o administrativo? (D/V/A): ').lower()
            if comprador == 'exit':
                print('Adios...')
                exit()
            try:
                if comprador == 'd':
                    comprador = 'estudiante_diurno'
                    descuento = calcular_descuento(total_pedido)
                    valor_descuento = 12
                    pedido_activo = 0
                elif comprador == 'v':
                    comprador = 'estudiante_vespertino'
                    descuento = calcular_descuento(total_pedido)
                    valor_descuento = 10
                    pedido_activo = 0
                elif comprador == 'a':
                    comprador = 'administrativo'
                    descuento = calcular_descuento(total_pedido)
                    valor_descuento = 0
                    pedido_activo = 0
                elif comprador != 'd' or comprador != 'v' or comprador != 'a':
                    raise ValueError
            except ValueError:
                print('La opcion ingresada no es valida')
                continue
            confirmar_pedido = input('Desea confirmar su pedido? (S/N): ').lower()
            if confirmar_pedido == 'exit':
                print('Adios...')
                exit()
            elif confirmar_pedido == 's':
                pedido_activo = 0
            elif confirmar_pedido == 'n':
                print('Su pedido ha sido cancelado')
                pedido_activo = 1
                cantidad_pizzas_compradas = []
                pizzas_compradas = []
                total_pedido = 0
                continue
            else:
                print('La opcion ingresada no es valida')
                continue
    else:
        print('La opcion ingresada no es valida')
        continue

    if pedido_activo == 0:
        print(f'\nHola {comprador.upper()}!')
        print('\nA continuacion se muestra el detalle de su pedido: ')
        print('\nPizzas Duoc\n')
        print('-------------------------------------\n')
        for valor in range(len(pizzas_compradas)):
            if cantidad_pizzas_compradas[valor] > 1:
                print(
                    f'{cantidad_pizzas_compradas[valor]} pizzas {pizzas_compradas[valor]} \t\t\t $ {tipos_de_pizza[pizzas_compradas[valor]] * cantidad_pizzas_compradas[valor]}')
            else:
                print(
                    f'{cantidad_pizzas_compradas[valor]} pizza {pizzas_compradas[valor]} \t\t $ {tipos_de_pizza[pizzas_compradas[valor]] * cantidad_pizzas_compradas[valor]}')
        print('--------------------------------------\n')
        print('Subtotal \t\t\t\t\t $', total_pedido)
        print(f'Descuento % {valor_descuento} \t\t\t\t $ {descuento}')
        print('--------------------------------------\n')
        print(f'Total a pagar \t\t\t\t $ {total_pedido - descuento}\n')
        print("¨Gracias por su compra!")
        exit()