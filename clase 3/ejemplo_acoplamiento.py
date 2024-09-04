respuesta_1 = [200, "José"]
respuesta_2 = [400, ]

def obtener_nombre(respuesta_base_datos) -> str:
    
    '''Obtiene un nombre de la base de datos'''

    if respuesta_base_datos[0] == 200:
        respuesta_nombre = respuesta_base_datos[1]
    else:
        respuesta_nombre = "Error"

    return respuesta_nombre

# Esta función está acoplada con la anterior
def enviar_mail(respuesta_base_datos):

    '''Esta función envía un mail al usuario de la base de datos'''
    nombre = obtener_nombre(respuesta_base_datos)
    print(f"Bienvenido {nombre} a Disney+")

enviar_mail(respuesta_1)
enviar_mail(respuesta_2)




