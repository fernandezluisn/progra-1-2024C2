cadena_de_caracteres = "Soy una cadena alfanumerica"

listado = []
inicio = 0
print(len(cadena_de_caracteres))
for i in range(0, len(cadena_de_caracteres)):
    
    if cadena_de_caracteres[i] == " ":
        print(cadena_de_caracteres[inicio: i])               
        listado += [cadena_de_caracteres[inicio: i]]
        inicio = i+1
    elif i == len(cadena_de_caracteres) - 1:
        listado += [cadena_de_caracteres[inicio: i + 1]]

    
     

print(listado[1: 3])
    