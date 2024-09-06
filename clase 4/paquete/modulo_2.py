# El modulo 2 gestiona a los docentes
UNIVERSIDAD = "UTN-FRA"

def informar_materias(lista_materias, nombre_docente : str)->None:

    for materia in lista_materias:
        print(f"El docente {nombre_docente} da clases en {materia}")