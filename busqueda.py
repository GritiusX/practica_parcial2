# ===== Clase 11: Búsqueda =====

nombres = ["Ana", "Bruno", "Carla", "Diego", "Elena"]
numeros = [4, 8, 15, 16, 23]
lista_desordenada = [3, 1, 6, 4, 8, 2]

# 1) Implementar busqueda_secuencial y probarla con una lista de nombres (strings).
def busqueda_secuencial_y_string(lista,name):
    for elem in lista:
        if name.lower() == elem.lower():
            return elem
    return -1

# 2) Implementar busqueda_binaria y probarla con una lista de números ordenada.
def busqueda_secuencial_y_num(lista,num):
    for elem in lista:
        if int(num) == elem:
            return num
    return -1

# 3) Modificar la búsqueda secuencial para contar cuántas comparaciones realiza.
def busqueda_secuencial_con_comparaciones(lista,num):
    comparaciones=0
    for elem in lista:
        if (comparaciones < len(lista)) and (elem != int(num)):
            comparaciones += 1
        else:
            return num, comparaciones
    return -1

# 4) Dada una lista desordenada, ordenarla primero (usando sorted()) y luego aplicar búsqueda binaria.
def ordenar_lista_mas_busqueda_binaria_devuelve_posicion(lista,num):
    ordenada = []
    ordenada = sorted(lista)
    izq, der = 0, len(ordenada) -1
    while izq <= der:
        medio = (izq + der) // 2
        if ordenada[medio] == num:
            return medio
        elif ordenada[medio] < num:
            izq = medio + 1
        else:
            der = medio -1
    return -1

# 5) Probar busqueda_binaria con una lista desordenada: ¿encuentra siempre el valor? ¿Por qué?
def busqueda_binaria_con_lista_desordenada_devuelve_posicion(lista,num):
    izq, der = 0, len(lista) -1
    while izq <= der:
        medio = (izq + der) // 2
        if lista[medio] == num:
            return medio
        elif lista[medio] < num:
            izq = medio + 1
        else:
            der = medio - 1
    return -1
# la busqueda binaria ASUME SIEMPRE que la lista esta ordenada, por eso hay veces que da correcto 
# pero en otra muy probable que no por el tema de las mitades, que lo que esta a la izq es menor 
# que lo que esta a la der

# 6) Escribir una función que indique si conviene usar búsqueda secuencial o binaria
#    según el tamaño y el estado (ordenada o no) de la lista.

def esta_ordenada(lista):
    for i in range(1, len(lista)):
        if lista[i - 1] > lista[i]:   # un par al revés alcanza
            return False
    return True                        # revisó todo sin encontrar ninguno

def busqueda_binaria_o_secuencial(lista):
    if len(lista) <= 5:
        return "es chica, conviene secuencial"
    if esta_ordenada(lista):
        return "es grande y esta ordenada, conviene binaria"
    return "esta desordenada, conviene secuencial"

print(busqueda_binaria_o_secuencial(numeros))              # binaria
print(busqueda_binaria_o_secuencial(lista_desordenada))    # secuencial
print(busqueda_binaria_o_secuencial([1, 5, 2, 9, 3, 7]))   # secuencial