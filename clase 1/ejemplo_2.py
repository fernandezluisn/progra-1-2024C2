# división con programación funcional

def dividir(num_1, num_2):
    if (num_1 != 0 and num_2 != 0):
        return num_1 / num_2
    else:
        print("Los números a dividir deben ser distintos de cero")


print(f"El resultado de la división es {dividir(6, 5)}")

