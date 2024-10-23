from funciones.auxiliares import *
from funciones.admin_productos import *

depositos = ["PBA", "CABA", "Chubut", "Tucumán", "Mendoza"]
productos = ["autos", "muñecas", "trenes", "peluches", "spinners", "cartas"]

ejecutar = True
carga = True

matriz_ejercicio = [[13,1,13,13,1,4444], [11,1,42,13,1,2], [1,21,44,1,5551,112], 
                    [441,13,31,41,12,15], [12,31,1,12,1,2]]

while ejecutar == True:

    print("Seleccione opción que desea realizar:")
    print("1- obtener existencias")
    print("2- calcular juguetes por depósito")
    print("3- controlar juguetes a reponer")
    print("4- máxima cantidad de juguetes por tipo, mostrar provincia")
    print("5- déposito con mayor recaudación")


    print("10- salir")

    opcion = input("ingrese la opcion que desea realizar: ")
    
    
    match opcion:
        case "1":
            # Carga secuencial
            if carga == False:
                matriz_ejercicio = inicializar_matriz(len(depositos), len(productos), 0)
                #print(matriz_ejercicio)
                
                for i in range(len(depositos)):
                    for j in range(len(productos)):

                        cantidad = int(input(f"Ingrese cantidad de {productos[j]} en {depositos[i]}"))
                        matriz_ejercicio[i][j] = cantidad
                
                carga = True
            else:
                for i in range(len(matriz_ejercicio)):
                    for j in range(len(matriz_ejercicio[i])):
                        print(f"En {depositos[i]} hay {matriz_ejercicio[i][j]} {productos[j]}")
        
        case "2":
            # recorrer en matriz las filas, y recorrer 2 listas
            lista_totales = calcular_totales(matriz_ejercicio)
            for i in range(len(depositos)):
                print(f"En {depositos[i]} hay {lista_totales[i]} productos")
        
        case "3":
            controlar_cantidad(matriz_ejercicio, depositos, productos, 10)
        
        case "4":
            
            for i in range(len(productos)):
                bandera = False
                for j in range(len(depositos)):
                    if bandera == False:
                        maximo = matriz_ejercicio[j][i]
                        deposito = depositos[j]
                        bandera = True
                    elif matriz_ejercicio[j][i] > maximo:
                        maximo = matriz_ejercicio[j][i]
                        deposito = depositos[j]
                
                print(f"El deposito con más {productos[i]} es {deposito}")
                        
        case "5":
             # justifica función de carga secuenciales
            matriz_ventas = [[13,1,13,13,1,4444], 
                              [11,1,42,13,1,2], 
                              [1,21,44,1,5551,112], 
                              [441,13,31,41,12,15], 
                              [12,31,1,12,1,2]]    

            # matriz_ventas = inicializar_matriz(len(depositos), len(productos), 0)
            # matriz_ventas = cargar_secuencialmente(matriz_ventas, "ventas", 
            #                                        depositos, productos)
            
            recaudaciones = calcular_recaudacion(matriz_ventas)

            bandera_5 = False

            for i in range(len(recaudaciones)):
                
                if bandera_5 == False:
                    maximo = recaudaciones[i]
                    deposito = depositos[i]
                    bandera_5 = True
                elif recaudaciones[i] > maximo:
                    maximo = recaudaciones[i]
                    deposito = depositos[i]

            print(f"El depósito con más recaudación es {deposito}")

                        
        case "10":
            print("Se salió del ejercicio")
            ejecutar = False
            

