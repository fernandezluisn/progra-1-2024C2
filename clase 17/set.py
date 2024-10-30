set_a = {1, 3, 4, 555, 6, 4}
set_b = {2, 4, 77, 4, 6}

#print(set_a)

set_unido = set_a.union(set_b)

#print(set_unido)

print(f"Se encuentran en el set_a y no en el b {set_a - set_b}")
print(f"Los elementos comunes en el set_a y el b son {set_a & set_b}")
print(f"La unión de ambos sets es {set_a | set_b}")

print(f"La diferencia simetrica es {set_a.symmetric_difference(set_b)}")