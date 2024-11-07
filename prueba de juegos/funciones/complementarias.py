def guardar_record(ruta_archivo:str, datos_del_juego: dict) -> bool:
    
    #1- Actualizar registros.
    registros = leer_registros(ruta_archivo)
    ruta = "./prueba de juegos/archivos/" + ruta_archivo    
    # paso archivo a un objeto que pueda leer python para poder manipularlo
    for usuario in registros:
        if datos_del_juego["Nombre"] == usuario["Nombre"]:
            usuario["Mejor marca"] = datos_del_juego["Puntos"]
            break
        
    print(registros)
    
    # Una vez actualizados los registros sobreescribo archivo
    with open(ruta, "w", encoding="utf-8") as archivo:  
         
         for fila in registros:
              linea = fila["Nombre"]+","+str(fila["Mejor marca"])           
    
              archivo.write(linea + "\n")
    

def leer_registros(ruta_archivo:str) -> list:
        
        """
        Devuelve un listados con nombres y mejores marcas de cada usuario.
        Recibe la ruta del archivo.
        Retorna una lista de diccionarios.
        """
        ruta = "./prueba de juegos/archivos/" + ruta_archivo

        lista_retorno = []

        with open(ruta, "r", encoding="utf-8") as archivo:    
            for linea in archivo:
                
                diccionario = {"Nombre": "Sin nombre",
                               "Mejor marca": 0}
                
                valores = linea.split(",")

                                        
                diccionario["Nombre"]= valores[0]
                    
                diccionario["Mejor marca"]= int(valores[1])
                
                lista_retorno.append(diccionario)

        return lista_retorno

