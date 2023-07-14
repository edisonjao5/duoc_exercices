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
departamentos = [tipo + str(i) for tipo in 'ABCD' for i in range(1, 11)]



def dpto_buy():
    os.system("cls")
    while True:
        print("=== Comprar Departamento ===")
        piso = int(input("Ingrese el piso del departamento a comprar: "))
        tipo = input("Ingrese el tipo de departamento a comprar | A | B | C | D |: ").upper()
        depto = tipo + str(piso)
        if tipo in 'ABCD' and 1 <= piso <= 10:
            if depto in departamentos:
                rut = input("Ingrese el RUT del comprador (sin dígito verificador): ")
                nombre = input("Ingrese el nombre del comprador: ").capitalize()
                if nombre.len() < 5:
                    print("Nombre no valido. Intente nuevamente..")
                    continue
                apellido = input("Ingrese el apellido del comprador: ").capitalize()
                if apellido.len() < 5:
                    print("Apellido no valido. Intente nuevamente..")
                departamentos.remove(depto)
                compradores[rut] = {
                    "nombre": nombre,
                    "apellido": apellido,
                    "depto": depto,
                }
                print(f"El Departamento ha sido comprado exitosamente por {nombre} {apellido} {validar_rut(rut)}, Felicidades.")
                break
            else:
                print("Departamento vendido. Por favor, seleccione otro.")
        else:
            print("N° de Departamento no valido. Intente nuevamente..")

def dptos_available():
    os.system("cls")
    print("=== Departamentos Disponibles ===")
    print("Piso \n  | A | B | C | D |")
    for piso in range(1, 11):
        piso = 11 - piso
        fila = [str(piso)]
        for tipo in 'ABCD':
            depto = tipo + str(piso)
            if depto in departamentos:
                fila.append('  ')
            else:
                fila.append(' X')
        print(' |'.join(fila), "|")
        

def buyers():
    os.system("cls")
    print("=== Listado de Compradores ===")
    for rut, comprador in compradores.items():
        print(f"RUT: {validar_rut(rut)}")
        print(f"Nombre: {comprador['nombre']} {comprador['apellido']}")
    if not compradores:
        print("No hay compradores registrados.")

def total_sales():
    os.system("cls")
    print("=== Ventas Totales ===")
    ventas = {tipo: 0 for tipo in 'ABCD'}
    for rut, comprador in compradores.items():
        tipo = comprador['depto'][0]
        ventas[tipo] += precios_dptos[tipo]
    print("| Tipo de Departamento  |Cantidad|  Total  |")
    ganancias = 0
    for tipo, total in ventas.items():
        cantidad = len([comprador for comprador in compradores.values() if comprador['depto'][0] == tipo])
        print(f"| Tipo {tipo} {precios_dptos[tipo]}\t\t|    {cantidad}   |  {total} UF  |")
        ganancias += total
    print(f"| TOTAL \t\t|    {len(compradores)}    |  {ganancias} UF  |")
    
def go_out():
    os.system("cls")
    print("=== Salir ===")
    nombre = input("Ingrese su nombre: ").capitalize()
    apellido = input("Ingrese su apellido: ").capitalize()
    fecha_actual = datetime.datetime.now().strftime("%d/%m/%Y")
    print(f"\nGracias por usar el sistema, {nombre} {apellido}.")
    print(f"Fecha de salida: {fecha_actual}")

while True:
    print("\n\t\t----------BIENVENIDO A LA INMOBILIARIA CASA FELIZ----------\n")
    for i in range(len(options)):
      print(f"{i + 1}. {options[i]}")

    opcion = input("Ingrese la opción que desea realizar: \n")

    if opcion == '1':
        dpto_buy()
    elif opcion == '2':
        dptos_available()
    elif opcion == '3':
        buyers()
    elif opcion == '4':
        total_sales()
    elif opcion == '5':
        go_out()
        break
    else:
        print("Ingrese una opción valida.")
