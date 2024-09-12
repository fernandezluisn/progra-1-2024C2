# Para que haya cohesión las partes tienen que funcionar juntas
# Hace referencia a la relación entre funciones

# no es cohesiva con el main ya que repite el input
def restar1() -> None:
    
    num1 = float(input("Ingrese primer número: "))
    num2 = float(input("Ingrese segundo número: "))

    print(num1 - num2)

# es más cohesiva que la primera
def restar2(num1: float, num2: float)->float:
    '''
    Realiza una resta
    Recibe dos float
    devuelve un float
    '''
    return num1 - num2
