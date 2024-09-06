var_1 = "hola"

#Mediante la función id observamos la 'referencia' de los objetos y los valores
print(id("hola"))
print(id(var_1))

# Al cambiar de tipo, cambia de referencia ya que int es inmutable
var_1 = 13
print(id(var_1))
