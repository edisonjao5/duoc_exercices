# Control de arriendo y departamentos de la inmobiliaria mi casa en un nuevo proyecto
# funcion para validar el rut del cliente
from itertools import cycle
import datetime

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

# Variables globales
compradores = {}
pisos = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
departamentos = ["F", "G", "H", "I", "J"]
status = {
    "": "Disponible",
    "V": "Vendido",
    "A": "Arrendado",
}
precio_dptos_venta = {
    "F": 3800,
    "G": 3200,
    "H": 3100,
    "I": 3000,
    "J": 3400,
}
precio_dptos_arriendo = {
    "F": 25,
    "G": 18,
    "H": 16,
    "I": 23,
    "J": 28,
}
dptos_vendidos = {}
dptos_arrendados = {}
ganancias = 0
opciones = ["Comprar o Arrendar departamento", "Mostrar departamentos disponibles", "Ver listado de compradores", "Mostrar ganancias totales", "Salir"]
opcion = 0
fecha = datetime.datetime.now()

# Funciones del Menu
def comprar_dpto(ganancias):
    print("Es usted cliente de la inmobiliaria?")
    respuesta = input("Ingrese si o no: ").lower()
    if respuesta == "si":
        print("Ingrese su rut sin puntos ni guion: ")
        rut = int(input())
        rut = validar_rut(rut)
        if rut in compradores:
            print(f"Bienvenido {compradores[rut]['nombre']} {compradores[rut]['apellido']}")
            print("Desea comprar o arrendar un departamento?")
            respuesta = int(input("Ingrese 1 para comprar o 2 para arrendar: "))
            if respuesta == 1:
                print("Departamentos disponibles para la venta: ")

                #colocar una V en los departamentos vendidos y una A en los arrendados
                for piso, departamento in zip(pisos, departamentos):
                    if departamento in dptos_vendidos:
                        print(f"Piso {piso} - Departamento {departamento} - {status['V']}")
                    elif departamento in dptos_arrendados:
                        print(f"Piso {piso} - Departamento {departamento} - {status['A']}")
                    else:
                        print(f"Piso {piso} - Departamento {departamento} - {status['']}")
                # print("|      |   TIPO  |")
                # print("| PISO |F|G|H|I|J|")
                # print("|    10| | | | | |")
                # print("|     9| | | | | |")
                # print("|     8| | | | | |")
                # print("|     7| | | | | |")
                # print("|     6| | | | | |")
                # print("|     5| | | | | |")
                # print("|     4| | | | | |")
                # print("|     3| | | | | |")
                # print("|     2| | | | | |")
                # print("|     1| | | | | |")

                # for piso, departamento in zip(pisos, departamentos):
                #     print(f"Piso {piso} - Departamento {departamento}")
                print("Ingrese el piso y el departamento que desea comprar: ")
                piso = int(input("Ingrese el piso: "))
                departamento = input("Ingrese el departamento: ").upper()
                if departamento in departamentos and piso in pisos:
                    if departamento in dptos_vendidos:
                        print("Departamento no disponible")
                    else:
                        dptos_vendidos[departamento] = {
                            "piso": piso,
                            "status": status[1],
                            "precio": precio_dptos_venta[departamento],
                        }
                        print(f"Departamento {departamento} vendido exitosamente")
                        print(f"El precio del departamento es de {precio_dptos_venta[departamento]} UF")
                        ganancias += precio_dptos_venta[departamento]
                else:
                    print("Ingrese un piso y departamento valido")
            elif respuesta == 2:
                print("Departamentos disponibles para arriendo: ")
                for piso, departamento in zip(pisos, departamentos):
                    print(f"Piso {piso} - Departamento {departamento}")
                print("Ingrese el piso y el departamento que desea arrendar: ")
                piso = int(input("Ingrese el piso: "))
                departamento = input("Ingrese el departamento: ").upper()
                if departamento in departamentos and piso in pisos:
                    if departamento in dptos_arrendados:
                        print("Departamento no disponible")
                    else:
                        dptos_arrendados[departamento] = {
                            "piso": piso,
                            "status": status[2],
                            "precio": precio_dptos_arriendo[departamento],
                        }
                        print(f"Departamento {departamento} arrendado exitosamente")
                        print(f"El precio del departamento es de {precio_dptos_arriendo[departamento]} UF")
                        ganancias += precio_dptos_arriendo[departamento]
                else:
                    print("Ingrese un piso y departamento valido")
            else:
                print("Ingrese una respuesta valida")
        else:
            print("Usted no es cliente de la inmobiliaria")
    elif respuesta == "no":
        print("Ingrese su rut sin puntos ni guion: ")
        rut = int(input())
        rut = validar_rut(rut)
        nombre = input("Ingrese su nombre: ")
        apellido = input("Ingrese su apellido: ")
        telefono = int(input("Ingrese su telefono: "))
        compradores[rut] = {
            "nombre": nombre,
            "apellido": apellido,
            "telefono": telefono,
        }
        print("Usted ha sido registrado como cliente de la inmobiliaria")
    else:
        print("Ingrese una respuesta valida")

def mostrar_dptos():
    print("Departamentos disponibles para la venta: ")
    for piso, departamento in zip(pisos, departamentos):
        print(f"Piso {piso} - Departamento {departamento}")
    print("Departamentos disponibles para arriendo: ")
    for piso, departamento in zip(pisos, departamentos):
        print(f"Piso {piso} - Departamento {departamento}")
def ver_compradores():
    for rut, comprador in compradores.items():
        print(f"Rut: {rut} - Nombre: {comprador['nombre']} {comprador['apellido']} - Telefono: {comprador['telefono']}\n")
    if len(compradores) == 0:
        print("No hay compradores registrados\n")
def ganancias_totales():
    print(f"Las ganancias totales son de {ganancias} UF")
    if ganancias == 0:
        print("No hay ganancias registradas")
def salir(rut, fecha):
    print(f"Gracias {compradores[rut]['nombre']} {compradores[rut]['apellido']} hoy {fecha} por preferirnos")
    exit()

print("\n\t\t----------BIENVENIDO A LA INMOBILIARIA MI CASA----------\n")

while opcion != 6:
    print("Por favor seleccione entre las siguientes opciones: \n")
    for i in range(len(opciones)):
        print(f"{i + 1} - {opciones[i]}")

    opcion = int(input("\nSeleccione la opción que desea realizar: \n"))
    if opcion == 1:
        comprar_dpto(ganancias)
    elif opcion == 2:
        mostrar_dptos()
    elif opcion == 3:
        ver_compradores()
    elif opcion == 4:
        ganancias_totales()
    elif opcion == 5:
        salir()
    else:
        print("Ingrese una opcion valida")

