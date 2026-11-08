# 1) Sumar todos los elementos de una lista de números
mi_lista = [1,2,2,2,4,4,9,0,9,13]

def sumar_elementos_lista(lista):
	suma = 0
	for l in range(len(lista)):
		suma = suma + lista[l]
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
	acc = lista[0]

	for l in range(len(lista)):
		if lista[l] > acc:
			acc = lista[l]
	return acc

""" var = encontrar_num_max(mi_lista)
print(f"num_max_from_list: {var}") """

# mi_lista = [1,2,2,2,4,4,9,0,9,13]

# 5) Eliminar duplicados manteniendo el orden original
def delete_dups_nums_keep_order(lista):
	new_list = []
	for l in range(len(lista)):
		if lista[l] not in new_list:
			new_list.append(lista[l])
	
	return new_list

# var = delete_dups_nums_keep_order(mi_lista)
# print(f"lista_sin_dups_mismo_orden: {var}")

# mi_lista = [1,2,2,2,4,4,9,0,9,13]

# 6) Contar cuántas veces aparece cada elemento
def count_times_sth_appears(lista):
	numeros = []
	apariciones = []

	print(f"len: {len(lista)}")
	for l in range(len(lista)):

		print(f"pos {l} ==> num {lista[l]}")

		if lista[l] not in numeros:
			numeros.append(lista[l])
			apariciones.append(1)
		else:
			index = numeros.index(lista[l])
			apariciones[index] += 1
	
	return [numeros, apariciones]

# count_times_sth_appears(mi_lista)
# print(f"lista_de_items_repetidos_y_apariciones: {count_times_sth_appears(mi_lista)}")


#mi_list1=[1,3,5,8,9]
#mi_list2=[2,4,6,8,9]

# 7) Encontrar los elementos comunes entre dos listas
def find_common_element(first_list,second_list):
	common_elements = []
	for l in range(len(first_list)):
		if first_list[l] in second_list:
			if first_list[l] not in common_elements:
				common_elements.append(first_list[l])
	return common_elements

# find_common_element(mi_list1,mi_list2)
# print(f"find_common_element: {find_common_element(mi_list1,mi_list2)}")

mi_list = [1,2,3,4]
# 8) Calcular el producto de todos los números
def product_calculated(lista):
	prod = 1
	for l in range(len(lista)):
		prod = prod * lista[l]
	return prod

# product_calculated(mi_list)
# print(f"product_calculated: {product_calculated(mi_list)}")

my_list = [1,2,3,4]
# 9) Buscar la posición de un número (-1 si no está)
def search_position(lista, numero):
	for i in range(len(lista)):
		if lista[i] == numero:
			return i
	return -1

#search_position(my_list,4)
#search_position(my_list,9)

#print(f"YES - search_position: {search_position(my_list,4)}")
#print(f"NO - search_position: {search_position(my_list,9)}") 

mi_list1=[1,3,5,8,9]
mi_list2=[2,4,6,8,9]

# 10) Sumar dos listas de igual tamaño, elemento por elemento
def add_both_lists_by_elements(lista1,lista2):
	lista_suma = []
	for l in range(len(lista1)):
		print("lista1", lista1[l], "+" ,"lista2",lista2[l])

		add = lista1[l] + lista2[l]
		print("add: ",add)
		lista_suma.append(add)
		print("lista_suma: ", lista_suma)
	return lista_suma

print(f"add_both_lists_by_elements: {add_both_lists_by_elements(mi_list1,mi_list2)}")