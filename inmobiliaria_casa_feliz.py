from itertools import cycle
import datetime
import os

def digito_verificador(rut):
    rut = str(rut)
    reversed_digits = map(int, reversed(str(rut)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    if (-s) % 11 == 10:
        return "K"
    return (-s) % 11

def validar_rut(rut):
    rut = str(rut) + "-" + str(digito_verificador(rut))
    return rut

compradores = {}
precios_dptos = {
    "A": 3800,
    "B": 3000,
    "C": 2800,
    "D": 3500,
}

options = ['Comprar departamento', 'Mostrar departamentos disponibles', 'Ver listado de compradores', 'Mostrar ganancias totales', 'Salir']
departamentos = ['A' + str(i) for i in range(1, 11)] + ['B' + str(i) for i in range(1, 11)] + ['C' + str(i) for i in range(1, 11)] + ['D' + str(i) for i in range(1, 11)]
option = 0



def dpto_buy():
    os.system("cls")
    while True:
        piso = int(input("Ingrese el piso del departamento a comprar (1-10): "))
        tipo = input("Ingrese el tipo de departamento a comprar (A, B, C, D): ").upper()
        depto = tipo + str(piso)
        if tipo in 'ABCD' and 1 <= piso <= 10:
            if depto in departamentos:
                run = input("Ingrese el RUN del comprador (sin dígito verificador): ")
                departamentos.remove(depto)
                compradores.append((run, depto))
                print("La operación se ha realizado correctamente.")
                break
            else:
                print("El departamento ya ha sido vendido. Por favor, seleccione otro.")
        else:
            print("El departamento ingresado no existe. Por favor, intente de nuevo.")

def dptos_available():
    os.system("cls")
    print("Piso \n  | A | B | C | D |")
    for piso in range(1, 11):
        fila = [str(piso)]
        for tipo in 'ABCD' or 'abcd':
            depto = tipo + str(piso)
            if depto in departamentos:
                fila.append('  ')
            else:
                fila.append(' X')
        print('  '.join(fila))

def buyers():
    os.system("cls")
    for run, depto in sorted(compradores):
        print(f'RUN: {run}, Departamento: {depto}')

def total_sales():
    os.system("cls")
    ventas = {tipo: 0 for tipo in 'ABCD'}
    for run, depto in compradores:
        ventas[depto[0]] += precios[depto[0]]
    print("Tipo de Departamento  Cantidad  Total")
    for tipo, total in ventas.items():
        cantidad = list(compradores).count(tipo)
        print(f"{tipo}  {cantidad}  {total} UF")
    total_ventas = sum(ventas.values())
    print(f"TOTAL  {len(compradores)}  {total_ventas} UF")

def go_out():
    os.system("cls")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
    print(f"\nGracias por usar el sistema, {nombre} {apellido}.")
    print(f"Fecha de salida: {fecha_actual}")

while True:
    print("\n=== Inmobiliaria Casa Feliz ===")
    for i in range(len(options)):
      print(f"{i + 1}. {options[i]}")

    opcion = input("Ingrese una opción (1-5): ")

    if opcion == '1':
        print("Usted ha seleccionado la opción 1: comprar departamento\n ")
        dpto_buy()
    elif opcion == '2':
        print("Usted ha seleccionado la opción 2: Mostrar departamentos disponibles\n ")
        dptos_available()
    elif opcion == '3':
        print("Usted ha seleccionado la opción 3: Ver listado de compradores\n ")
        buyers()
    elif opcion == '4':
        print("Usted ha seleccionado la opción 4: Mostrar ventas totales\n ")
        total_sales()
    elif opcion == '5':
        print("Usted ha seleccionado la opción 5: go_out\n ")
        go_out()
        break
    else:
        print("Opción inválida.")

