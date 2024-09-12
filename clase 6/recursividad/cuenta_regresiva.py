def contar_regresivamente(n: int) -> None:
    
    if n > 0 :
        print(n)
        contar_regresivamente(n-1)
    else:
        print("Ceroooooooo")

contar_regresivamente(3)