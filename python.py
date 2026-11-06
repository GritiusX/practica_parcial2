# 1) Sumar todos los elementos de una lista de números
mi_lista = [1,2,4,4,9,0,9]

def sumar_elementos_lista(lista):
	suma = 0
	for l in range(len(lista)):
		print(int(lista[l]))
		suma = suma + int(lista[l])
	return suma

""" var = sumar_elementos_lista(mi_lista)
print(f"suma: {var}") """

# 2) Devolver una nueva lista con solo los números pares

def devolver_solo_pares(lista):
	new_list = []
	for l in range(len(lista)):
		if lista[l] % 2 == 0:
			new_list.append(lista[l])
	return new_list

""" var = devolver_solo_pares(mi_lista)
print(f"new_list: {var}") """

# 3) Invertir una lista sin usar reverse()
def invertir_lista_sin_reverse(lista):
	lista.sort(reverse=True)
	return lista

""" var = invertir_lista_sin_reverse(mi_lista)
print(f"list_inverted: {var}") """

# 4) Encontrar el número máximo en una lista de enteros
def encontrar_num_max(lista):
	acc = 0

	for l in range(len(lista)):
		if l < len(lista) and lista[l] > acc:
			acc = lista[l]
	return acc

""" var = encontrar_num_max(mi_lista)
print(f"num_max_from_list: {var}") """

# 5) Eliminar duplicados manteniendo el orden original
def delete_dups_nums_keep_order(lista):
	new_list = set(lista)
	return new_list

var = delete_dups_nums_keep_order(mi_lista)
print(f"lista_sin_dups_mismo_orden: {var}")




# 6) Contar cuántas veces aparece cada elemento
# 7) Encontrar los elementos comunes entre dos listas
# 8) Calcular el producto de todos los números
# 9) Buscar la posición de un número (-1 si no está)
# 10) Sumar dos listas de igual tamaño, elemento por elemento