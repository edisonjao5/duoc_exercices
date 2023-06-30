from itertools import cycle

def digito_verificador(dni):
    dni = str(dni)
    reversed_digits = map(int, reversed(str(dni)))
    factors = cycle(range(2, 8))
    s = sum(d * f for d, f in zip(reversed_digits, factors))
    if (-s) % 11 == 10:
        return "K"
    return (-s) % 11

def validar_dni(dni):
    dni = str(dni) + "-" + str(digito_verificador(dni))
    return dni

opciones = ["Guardar registro", "Buscar Registro", "Imprimir Certificado", "Eliminar Registro", "Salir"]
usuarios_registrados = {}
Certificados = {
    "Nacimiento" : "\n\tEl Registro Civil certifica que el usuario {nombre} \n\tidentificado con dni {dni} nacio en {ciudad} - {pais} y tiene {edad} años\n",
    "Matrimonio" : "\n\tEl Registro Civil certifica que el usuario {nombre} \n\tidentificado con dni {dni} esta casado con {conyuge} \n\tel dia {fecha_matrimonio} y tiene {hijos} hijos\n",
}
opcion = 0

print("\n\t\t----------BIENVENIDO AL SISTEMA RENAPER----------\n")

while opcion != 5:
    print("Por favor seleccione la opcion que desea realizar: \n")
    for i in range(len(opciones)):
        print(f"{i + 1}.) {opciones[i]}")
    opcion = int(input("Seleccione la opcion que desea realizar: "))

    if opcion == 1:
        print("\n\t\t----------GUARDAR REGISTRO----------\n")
        dni = int(input("Ingrese su dni sin puntos ni guion: "))
        nombre = input("Ingrese su nombre y apellido: ").capitalize()
        if len(nombre) < 8:
          print("El nombre debe tener al menos 8 caracteres")
          continue
        edad = int(input("Ingrese su edad: "))
        if edad < 0:
          print("La edad debe ser mayor a 0")
          continue
        pais = input("Ingrese su pais de origen: ").capitalize()
        ciudad = input("Ingrese su ciudad de origen: ").capitalize()
        if edad >= 18:
            estado_civil = input("Ingrese su estado civil: ").capitalize()
        else:
            estado_civil = None

        dni = validar_dni(dni)
        usuarios_registrados[dni] = [nombre, edad, pais, ciudad, estado_civil]
        print(usuarios_registrados)
        print("\n\t\t----------REGISTRO GUARDADO CON EXITO----------\n")
        continue

    elif opcion == 2:
        print("\n\t\t----------BUSCAR REGISTRO----------\n")
        dni = int(input("Ingrese su dni sin puntos ni guion para verificar su registro: "))

        dni = validar_dni(dni)
        if dni in usuarios_registrados:
            print(f"El DNI {dni} pertenece a: \n {usuarios_registrados[dni][0]} \n Edad: {usuarios_registrados[dni][1]} \n Pais: {usuarios_registrados[dni][2]} \n Ciudad: {usuarios_registrados[dni][3]} \n Estado Civil: {usuarios_registrados[dni][4]}")
        else:
            print("El dni ingresado no se encuentra registrado")

    elif opcion == 3:
        print("\n\t\t----------IMPRIMIR CERTIFICADO----------\n")
        dni = int(input("Ingrese su dni sin puntos ni guion para solicitar el certificado: "))

        dni = validar_dni(dni)
        if dni in usuarios_registrados:
            print("Que tipo de certificado desea solicitar: ")
            for i in range(len(Certificados)):
                print(f"{i + 1}.) {list(Certificados.keys())[i]}")
            certificado = int(input("Seleccione la opción del certificado a imprimir: "))
            if certificado == 1:
                if pais == "Argentina":
                    print(Certificados["Nacimiento"].format(nombre=usuarios_registrados[dni][0], dni=dni, pais=usuarios_registrados[dni][2], ciudad=usuarios_registrados[dni][3], edad=usuarios_registrados[dni][1]))
                else:
                    print("El usuario no nacio en Argentina, no se puede emitir el certificado")
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
                print(Certificados["Matrimonio"].format(nombre=usuarios_registrados[dni][0], apellido=usuarios_registrados[dni][1], dni=dni, conyuge=conyuge, fecha_matrimonio=fecha_matrimonio, hijos=hijos))
        else:
            print("El dni ingresado no se encuentra registrado")

    elif opcion == 4:
        print("\n\t\t----------ELIMINAR REGISTRO----------\n")
        dni = int(input("Ingrese su dni sin puntos ni guion para eliminar su registro: "))

        dni = validar_dni(dni)
        if dni in usuarios_registrados:
            usuarios_registrados.pop(dni)
            print("Registro eliminado con exito")
        else:
            print("El dni ingresado no se encuentra registrado")

    else:
        print("La opcion ingresada no es valida")
        continue

print("\n\t\t----------GRACIAS POR UTILIZAR EL SISTEMA DE RENAPER----------\n")