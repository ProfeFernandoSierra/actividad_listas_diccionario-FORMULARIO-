import os
os.system("cls")

#listas
postulantes = []
#contadores - acumuladores
vacante = 20
#banderas
acceso = True


print("=== SISTEMA DE POSTULACIÓN MAGÍSTER ===")
while acceso: 
    print("1. Registrar postulante")
    print("2. Ver postulantes registrados")
    print("3. Buscar postulante por correo")
    print("4. Ver postulantes aceptados")
    print("5. Ver estadísticas")
    print("6. Mostrar vacantes disponibles")
    print("7. Salir")
    try:
        opcion = int(input("ingrese una opcion\n"))
        if opcion == 1:
            os.system("cls")
            while True: #debemos validar que el nombre solo sean letras y no este vacio
                nombre = input("Ingrese su nombre\n").title()
                if nombre.isalpha() and len(nombre) > 0:
                    break
                else:
                    print("nombre invalido. Debe contener solo letras")
            while True: #debemos validar que el apellido solo sean letras y no este vacio
                apellido = input("Ingrese su apellido\n").title()
                if apellido.isalpha() and len(apellido) > 0:
                    break
                else:
                    print("apellido invalido. Debe contener solo letras")
            while True: #validar que edad sea un numero y este en el rango de 17 a 60
                try:
                    edad = int(input("Ingrese su edad\n"))
                    if edad >= 17 and edad <= 60:
                        break
                    else:
                        print("Edad debe estar entre 17 y 60")
                except:
                    print("edad ingresada debe ser numerica")
            while True: #validar que el correo tenga larg minimo 6 y contenga al menos un @ y un .
                correo = input("ingrese su correo\n")
                existe = False
                
                for p in postulantes:
                    if p["correo"] == correo:
                        existe = True
                
                if existe :  #correo@correo.cl
                    print("Correo ya esta registrado, intenta con otro")
                elif "@" not in correo or "." not in correo:
                    print("Correo inválido.")
                else:
                    break
                                
            while True: #validamops que la carrera tenga largo minimo 6
                carrera = input("Ingrese su carrera\n")
                if len(carrera) >= 6 :
                    break
                else:
                    print("nombre de carrera debe ser mayor a 6 caracteres")
            while True: #validamos que promedio sea un valor numerico y que este en el rango 1 a 7
                try:
                    promedio = float(input("Ingrese promedio\n"))
                    if promedio >= 1 and promedio <= 7:
                        break
                    else:
                        print("el promedio debe estar en el rango de escala chilena ")
                except:
                    print("el promedio debe ser un tipo de dato numerico")
            if edad >= 20 and promedio >= 5.5: #verificamos si la postulacion fue aceptada o rechazada segun criterios de edad y promedio
                estado = "Aceptado"
                vacante = vacante  - 1
            else:
                estado = "Rechazado"
            #creamos nuestro diccionario para almacenar los datos del postulante    
            postulante = {
                "nombre": nombre,
                "apellido": apellido,
                "edad": edad,
                "correo": correo,
                "carrera": carrera,
                "promedio": promedio,
                "estado": estado
            }
            #agregamos nuestro postulante a la lista de postulantes
            postulantes.append(postulante)
            print(f"{nombre} te has postulado con exito: postulacion {estado}")

        elif opcion == 2:
            os.system("cls")
            print("Ver postulantes")
            #validamos que existan postulante dentro de postulantes
            if len(postulantes) > 0: #imprimimos los datos de todos los postulante
                for p in postulantes:
                    print(f"Nombre completo: {p["nombre"]} {p["apellido"]}")
                    print(f"Edad: {p["edad"]}")
                    print(f"Correo: {p["correo"]}")
                    print(f"Carrera: {p["carrera"]}")
                    print(f"Promedio: {p["promedio"]}")
                    print(f"Estado: {p["estado"]}")
                    print("******************")
                
            else: #enviamos mensaje correspondiente a que no existen postulantes (aun)
                print("No existen postulantes registrados")
            
        elif opcion == 3:
            os.system("cls")
            print("Buscar postulante por correo")
            if len(postulantes) == 0:
                print("No existen postulantes para buscar")
            else:
                correo_buscar = input("ingrese correo para buscar un postulante\n")
                encontrado = False
                
                for p in postulantes:
                    if p["correo"] == correo_buscar:
                        encontrado = True
                        print(f"Nombre completo: {p["nombre"]} {p["apellido"]}")
                        print(f"Edad: {p["edad"]}")
                        print(f"Correo: {p["correo"]}")
                        print(f"Carrera: {p["carrera"]}")
                        print(f"Promedio: {p["promedio"]}")
                        print(f"Estado: {p["estado"]}")
                if encontrado == False:
                    print("Correo no existe en postulaciones")
            
                                    
        elif opcion == 4:
            os.system("cls")
            print("Ver postulantes aceptados")
            aceptado = False
            if len(postulantes) == 0:
                print("No existen postulantes")
            else:
                for p in postulantes:
                    if p["estado"] == "Aceptado":
                        aceptado = True
                        print(f"Nombre completo: {p["nombre"]} {p["apellido"]}")
                        print(f"Edad: {p["edad"]}")
                        print(f"Correo: {p["correo"]}")
                        print(f"Carrera: {p["carrera"]}")
                        print(f"Promedio: {p["promedio"]}")
                        print(f"Estado: {p["estado"]}")
                        print("******************")
                if aceptado == False:
                    print("No existen postulantes Aceptados")   
                                  
        elif opcion == 5:
            print("")
            
        elif opcion == 6:
            print("")
            
        elif opcion == 7:
            print("Hasta luego :)  ")
            acceso = False
        else:
            print("Opcion ingresada no existe")
    except:
        print("Opcion ingresada debe ser numerica")


