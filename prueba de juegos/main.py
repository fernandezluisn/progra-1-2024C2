from funciones.logica_juego import *
from funciones.complementarias import *

jugar = True

while jugar == True:

    print("Seleccione la opción que desea realizar:")
    print("1- Jugar nuevo juego")
    print("2- Salir")

    opcion = int(input("Ingrese la opción que desea realizar: "))

    match opcion:
        case 1:

            # cada vez que se inicia un juego creamos lo necesario para el inicio del
            # juego
            nom = input("Ingrese su nombre: ")
            print(f"Bienvenid@ {nom}")
            
            # controlar si el usuario ya existe
            lista_usuarios = leer_registros("registro.csv")
            #Lista usuarios contiene el record de cada usuario
            print(lista_usuarios)
            encontrado = False
            i = 0
            
            while (encontrado == False) and i < len(lista_usuarios):
                
                if lista_usuarios[i]["Nombre"] == nom:
                    maxima_puntuacion = lista_usuarios[i]["Mejor marca"]
                    print(f"Su usuario ya existe, su mejor marca es {maxima_puntuacion}")
                    encontrado = True

                i += 1

            # Este diccionario se utiliza mientras se ejecuta el juego
            datos_del_juego = {
                "Nombre" : nom,
                "Vidas": 1,
                "Puntos": 0
            }
            
            datos_del_juego = jugar_juego(datos_del_juego)
            puntaje = datos_del_juego["Puntos"]
            print(f"Felicitaciones {nom}")
            print(f"Sus puntos fueron {puntaje}")


            if encontrado:
                if puntaje > maxima_puntuacion:
                    guardar_record("registro.csv", datos_del_juego)
            


        case 2:            
            jugar = False
        case _:
            print("Debe seleccionar 1 o 2")
            sleep(3)
            pass