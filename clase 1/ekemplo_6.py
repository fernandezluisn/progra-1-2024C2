# ejemplo de match
especialidad = "psiquiatra"

match especialidad:
    case "dentista":
        print("El dentista atiende en el tercer piso, consultorio 305")
    case "clínico" | "psiquiatra":
        print("El clínico y el psiquiatra atienden en el segundo piso, consultar en ese piso")
    case "pediatra":
        print("El pediatra se encuentra en el primer piso, consultorio 103 o 104")
    case "otorrinolaringologo":
            print("El otorrinolaringologo se encuentra en el quinto piso, consultorio 505")
    case _:
          print("No hay información en el sistema, consulte en recepción.")


