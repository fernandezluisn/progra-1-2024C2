# División con programación orientada a objetos. Ya lo vamos a ver en profundidad
# más adelante.
class Calculadora:

    def __init__(self) -> None:
        self.resultado = 0

    def dividir(self, num_1, num_2):
        if (num_1 != 0 and num_2 != 0):
            self.resultado = num_1 / num_2
            return self.resultado
        
obj_calculadora = Calculadora() # se crea el objeto

print(f"El resultado es {obj_calculadora.resultado}") # muestro el valor por defecto de resultado


# llamo a la función y cambio resultado    
print(f"El resultado de la división con el objeto calculadora es {obj_calculadora.dividir(6,3)}") 

print(f"El resultado es {obj_calculadora.resultado}")

obj_calculadora_1 = Calculadora() # se crea un nuevo objeto

print(f"El resultado es {obj_calculadora_1.resultado}") # muestro el valor por defecto de resultado


# llamo a la función y cambio resultado    
print(f"El resultado de la división con el objeto calculadora es {obj_calculadora_1.dividir(6,2)}") 

print(f"El resultado para la calculadora uno es {obj_calculadora_1.resultado} y para la cero es {obj_calculadora.resultado}")