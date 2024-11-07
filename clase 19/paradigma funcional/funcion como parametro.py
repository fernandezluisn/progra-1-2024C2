from  ejemplo_1 import sumar, restar

def operar(num_1:int, num_2:int, operacion: any) -> int:
    return operacion(num_1, num_2)

print(f"operar devuelve {operar(3, 2, sumar)}")