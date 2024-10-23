#DRY dont repeat yourself

def calcular_totales(matriz: list) -> list:

    lista_retorno = [0] * len(matriz)

    for i in range(len(matriz)):
                acumulador = 0
                
                for j in range(len(matriz[i])):
                    acumulador += matriz[i][j]
                
                lista_retorno[i] = acumulador
    
    return lista_retorno

def controlar_cantidad(matriz:list, lista_nombres_1:list, 
                       lista_nombres_2:list, minimo:int = 500)->None:
       
       for i in range(len(matriz)):               
                
            for j in range(len(matriz[i])):
                  if matriz[i][j] < minimo:
                      print(f"Hay que reponer {lista_nombres_2[j]} en {lista_nombres_1[i]}")

def calcular_recaudacion(matriz: list, 
                         lista_precios: list = [22, 33, 5, 77, 11, 67])->list:

      """
      Esta función calcula recaudación.
      Recibe una matriz con las ventas y una lista con precios de productos.
      Devuelve una lista con recaudación por depósito.     
      """ 
      lista_retorno = [0] * len(matriz)
      
      
      for i in range(len(matriz)):
            recaudacion = 0 
            
            for j in range(len(matriz[i])):
                recaudacion += (matriz[i][j] * lista_precios[j])
            
            lista_retorno[i] = recaudacion
                 
      return lista_retorno

