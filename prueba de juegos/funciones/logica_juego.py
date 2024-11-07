from time import sleep
from random import choice 

opciones = ("piedra", "papel", "tijera")

def verificar_estado_juego(datos_del_juego: dict)->bool:
    if datos_del_juego["Vidas"] == 0:
        return False
    else:
        return True
    
def restar_vidas(datos_del_juego: dict, resultado: int)-> dict:

    if resultado == (-1):
        datos_del_juego["Vidas"] += resultado
        print("Se restó una vida")
    elif resultado == 1:
        print("Se sumó un punto")
        datos_del_juego["Puntos"] += resultado

    return datos_del_juego

def comparar_elementos(elemento_1:str, elemento_2:str)-> int:     
     
     resultado = 0
     match elemento_1:
        case "piedra":
            if elemento_2 == "papel":
                        resultado = -1
            elif elemento_2 == "tijera":
                        resultado = 1            
        case "papel":
                    if elemento_2 == "tijera":
                        resultado = -1
                    elif elemento_2 == "piedra":
                        resultado = 1
                    
        case "tijera":
                    if elemento_2 == "papel":
                        resultado = 1
                    elif elemento_2 == "piedra":
                        resultado = -1
                     
        case _:
                    print("debe ingresar piedra, papel o tijera")
                    
     return resultado


def jugar_juego(datos_del_juego: dict)->dict:

    while verificar_estado_juego(datos_del_juego):
        eleccion_1 = input("Qué opcion desea elegir: piedra, papel o tijera.")
        eleccion_1 = eleccion_1.lower()
        eleccion_maquina = choice(opciones)
        print("...")
        sleep(1)
        print(f"La máquina eligió {eleccion_maquina}")    

        resultado = comparar_elementos(eleccion_1, eleccion_maquina)
        datos_del_juego = restar_vidas(datos_del_juego, resultado)
        
        puntos_acumulados = datos_del_juego["Puntos"]
        vidas_acumuladas = datos_del_juego["Vidas"]

        print(f"tiene {puntos_acumulados} puntos")
        print(f"tiene {vidas_acumuladas} vidas")


    return datos_del_juego