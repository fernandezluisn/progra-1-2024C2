respuesta_1 = [200, "José"]
respuesta_2 = [400]

def retornar_nombre_y_estado(respuesta_base_datos):
    
    if isinstance(respuesta_base_datos, list) and len(respuesta_base_datos) > 1:
        estado = respuesta_base_datos[0]
        nombre = respuesta_base_datos[1]
        return estado, nombre
    else:
        return 400, "Error"


def enviar_mail(respuesta_base_datos):
    estado, nombre = retornar_nombre_y_estado(respuesta_base_datos)

    if estado == 200 :
        print(f"Bienvenido {nombre} a Disney+")
    else: 
        print(f"Bienvenido a Disney+")

enviar_mail(respuesta_2)