matriz2x2 = [
	[1,2],
	[4,5]
]

matriz = [
	[2,2],
	[2,2]
]

matriz0 = [
	[0,0],
	[0,0]
]

matriz_transponded2x3 = [
	[1,2,3],
	[4,5,6]
]

matriz_simetrica3x3 = [
	[1,2,0],
	[2,2,0],
	[0,0,0]
]

matriz_no_simetrica = [
	[1,3,0],
	[2,2,0],
	[0,0,0]
]

# 1) Sumar todos los elementos de una matriz de enteros
def add_all_elements_of_matrix(matriz):
	suma = 0
	for fila in matriz:
		for n in fila:
			suma = suma + n
	return suma

# 2) Verificar si una matriz cuadrada es la identidad
def is_identidad_matrix(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			if (i == j and matriz[i][j] != 1) or (i != j and matriz[i][j] != 0):
				return False
	return True

# 3) Sumar dos matrices del mismo tamaño
def add_two_equal_matrix(matriz1,matriz2):
	new_matrix= []
	for i in range(len(matriz1)):
		new_matrix_fila= []
		for j in range(len(matriz1[0])):
			a = matriz1[i][j]
			b = matriz2[i][j]
			new_matrix_fila.append(a + b)
		new_matrix.append(new_matrix_fila)
	return new_matrix

# 4) Multiplicar todos los elementos por un escalar
def multply_matrix_by_number(matriz, escalar):
	multiplied_matrix=[]
	for fila in matriz:
		new_fila=[]
		for columna in fila:
			columna = columna * escalar
			new_fila.append(columna)
		multiplied_matrix.append(new_fila)
	return multiplied_matrix

# 5) Calcular la transpuesta (m×n a n×m)
def transponded_matrix(matriz):
	new_matrix_transponded=[]
	for j in range(len(matriz[0])): # se toma el len de la primer fila de matriz para las columnas por eso el matriz[0]
		new_fila=[]
		for i in range(len(matriz)): #se toma el len de la matriz padre para las filas
			new_fila.append(matriz[i][j])
		new_matrix_transponded.append(new_fila)
	return new_matrix_transponded

# (0,0)  (0,1)  (0,2)		(0,0) (1,0)
# (1,0)  (1,1)  (1,2) ==>   (0,1) (1,1)
#							(0,2) (1,2)

# 6) Verificar si una matriz cuadrada es simétrica
def simetric_matrix(matriz):
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			if i != j and matriz[i][j] != matriz[j][i]:
				return False
	return True

# 6) ========= tengo que chequear que matriz[i][j] == matriz[j][i] pero que i != j =======

# (0,0) (1,1) (2,2) no importa en 3x3/2x2 ===

# (0,1) con (1,0)
# (0,2) con (2,0)
# (1,2) con (2,1)

# ========================================================================================
# 7) Calcular el producto de dos matrices MxN x NxZ
def multiply_two_matrix(matriz1, matriz2):
    new_matrix = []
    if len(matriz1[0]) == len(matriz2):
        for i in range(len(matriz1)):            # fila del resultado
            fila = []
            for j in range(len(matriz2[0])):     # columna del resultado
                suma = 0                         # arranca en 0 en cada celda
                for k in range(len(matriz2)):    # recorre los pares
                    suma += matriz1[i][k] * matriz2[k][j]
                fila.append(suma)
            new_matrix.append(fila)
        return new_matrix
    else:
        return -1

# 8) Buscar un elemento y devolver su posición (fila, columna)
def search_element_and_give_position(matriz,elemento):
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if elemento == matriz[i][j]:
				return i,j
	return None

# 9) Contar cuántos ceros hay
def count_many_0(matriz):
	zeros = 0
	for i in range(len(matriz)):
		for j in range(len(matriz[0])):
			if matriz[i][j] == 0:
				zeros += 1
	return zeros

# 10) Rotar una matriz cuadrada 90° en sentido horario
def rotate_matrix(matriz):
	rotated_matrix = []
	for i in range(len(matriz)):
		for j in range(len(matriz)):
			