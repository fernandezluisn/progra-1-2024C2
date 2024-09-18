lista_nueva = [0] * 5

for elemento in lista_nueva:
    print(elemento)

# Podemos cargar elementos de manera distribuida
cargar ="s"

while cargar == "s":
    i = int(input("Ingrese posición de la lista: "))
    valor = input("Ingrese valor para la lista: ")
    lista_nueva[i] = valor
    cargar = input("¿Quiere cargar otro elemento? s/n :")



for elemento in lista_nueva:
    print(elemento)
