# ===== Clase 11: Búsqueda =====

nombres = ["Ana", "Bruno", "Carla", "Diego", "Elena"]
numeros = [4, 8, 15, 16, 23, 42]

# 1) Implementar busqueda_secuencial y probarla con una lista de nombres (strings).
def busqueda_secuencial_y_string(matriz,name):
    for elem in matriz:
        if name.lower() == elem.lower():
            return elem
    return -1

# 2) Implementar busqueda_binaria y probarla con una lista de números ordenada.
def busqueda_secuencial_y_num(matriz,num):
    for elem in matriz:
        if int(num) == elem:
            return num
    return -1

print(busqueda_secuencial_y_num(numeros,4))
# 3) Modificar la búsqueda secuencial para contar cuántas comparaciones realiza.


# 4) Dada una lista desordenada, ordenarla primero (usando sorted()) y luego aplicar búsqueda binaria.


# 5) Probar busqueda_binaria con una lista desordenada: ¿encuentra siempre el valor? ¿Por qué?


# 6) Escribir una función que indique si conviene usar búsqueda secuencial o binaria
#    según el tamaño y el estado (ordenada o no) de la lista.