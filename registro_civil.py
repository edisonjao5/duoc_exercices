from itertools import cycle

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

opciones = ["Guardar registro", "Buscar Registro", "Imprimir Certificado", "Eliminar Registro", "Salir"]
usuarios_registrados = {}
Certificados = {
    "Nacimiento" : "El Registro Civil certifica que el usuario {nombre} {apellido} \nidentificado con rut {rut} nacio en {pais} y tiene {edad} años",
    "Matrimonio" : "El Registro Civil certifica que el usuario {nombre} {apellido} \nidentificado con rut {rut} esta casado con {conyuge} \nel dia {fecha_matrimonio} y tiene {hijos} hijos",
}
opcion = 0

print("\n\t\t----------BIENVENIDO AL TOTEM DE AYUDA DE REGISTRO CIVIL----------\n")

while opcion != 5:
    print("Por favor seleccione la opcion que desea realizar: \n")
    for i in range(len(opciones)):
        print(f"{i + 1}.) {opciones[i]}")
    opcion = int(input("Seleccione la opcion que desea realizar: "))

    if opcion == 1:
        print("\n\t\t----------GUARDAR REGISTRO----------\n")
        rut = int(input("Ingrese su rut sin puntos ni guion: "))
        nombre = input("Ingrese su nombre: ").capitalize()
        apellido = input("Ingrese su apellido: ").capitalize()
        edad = int(input("Ingrese su edad: "))
        pais = input("Ingrese su pais de origen: ").capitalize()
        if edad >= 18:
            estado_civil = input("Ingrese su estado civil: ").capitalize()
        else:
            estado_civil = None

        rut = validar_rut(rut)
        usuarios_registrados[rut] = [nombre, apellido, edad, pais, estado_civil]
        print(usuarios_registrados)
        print("\n\t\t----------REGISTRO GUARDADO CON EXITO----------\n")
        continue

    elif opcion == 2:
        print("\n\t\t----------BUSCAR REGISTRO----------\n")
        rut = int(input("Ingrese su rut sin puntos ni guion para verificar su registro: "))

        rut = validar_rut(rut)
        if rut in usuarios_registrados:
            print(f"El Rut {rut} pertenece a: \n {usuarios_registrados[rut][0]} {usuarios_registrados[rut][1]} \n Edad: {usuarios_registrados[rut][2]} \n Pais: {usuarios_registrados[rut][3]} \n Estado Civil: {usuarios_registrados[rut][4]}")
        else:
            print("El rut ingresado no se encuentra registrado")

    elif opcion == 3:
        print("\n\t\t----------IMPRIMIR CERTIFICADO----------\n")
        rut = int(input("Ingrese su rut sin puntos ni guion para solicitar el certificado: "))

        rut = validar_rut(rut)
        if rut in usuarios_registrados:
            print("Que tipo de certificado desea solicitar: ")
            for i in range(len(Certificados)):
                print(f"{i + 1}.) {list(Certificados.keys())[i]}")
            certificado = int(input("Seleccione la opción del certificado a imprimir: "))
            if certificado == 1:
                if pais == "Chile":
                    print(Certificados["Nacimiento"].format(nombre=usuarios_registrados[rut][0], apellido=usuarios_registrados[rut][1], rut=rut, pais=usuarios_registrados[rut][3], edad=usuarios_registrados[rut][2]))
                else:
                    print("El usuario no nacio en Chile, no se puede emitir el certificado")
            elif certificado == 2:
                if estado_civil != "Casado":
                    print("El usuario no esta casado, no se puede emitir el certificado")
                    continue
                conyuge = input("Ingrese el nombre de su conyuge: ").capitalize()
                apellido_conyuge = input("Ingrese el apellido de su conyuge: ").capitalize()
                conyuge = conyuge + " " + apellido_conyuge
                fecha_matrimonio = input("Ingrese la fecha de matrimonio con el formato dd/mm/aaaa: ")
                hijos = int(input("Ingrese la cantidad de hijos que tiene: "))
                print("\n\t\t----------CERTIFICADO EMITIDO CON EXITO----------\n")
                print(Certificados["Matrimonio"].format(nombre=usuarios_registrados[rut][0], apellido=usuarios_registrados[rut][1], rut=rut, conyuge=conyuge, fecha_matrimonio=fecha_matrimonio, hijos=hijos))
        else:
            print("El rut ingresado no se encuentra registrado")

    elif opcion == 4:
        print("\n\t\t----------ELIMINAR REGISTRO----------\n")
        rut = int(input("Ingrese su rut sin puntos ni guion para eliminar su registro: "))

        rut = validar_rut(rut)
        if rut in usuarios_registrados:
            usuarios_registrados.pop(rut)
            print("Registro eliminado con exito")
        else:
            print("El rut ingresado no se encuentra registrado")

    else:
        print("La opcion ingresada no es valida")
        continue

print("\n\t\t----------GRACIAS POR UTILIZAR EL TOTEM DE AYUDA DE REGISTRO CIVIL----------\n")