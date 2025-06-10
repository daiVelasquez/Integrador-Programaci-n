import random
import time

# 1. Generar biblioteca de libros aleatorios
titulos = ["Búsqueda", "Ordenamientos", "Códigos", "Redes", "Datos", "Python", "AI"]
autores = ["Ana", "Lautaro", "Marta", "Carlos", "Luna"]

biblioteca = []
for _ in range(1000):
    libro = {
        "titulo": random.choice(titulos),
        "autor": random.choice(autores),
        "año": random.randint(1980, 2025)
    }
    biblioteca.append(libro)

# 2. Bubble Sort Mejorado (lento)
def bubble_sort(lista):
    arr = lista.copy()
    n = len(arr)
    for i in range(n):
        intercambiado = False
        for j in range(0, n - i - 1):
            if arr[j]["año"] > arr[j + 1]["año"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                intercambiado = True
        if not intercambiado:
            break
    return arr

# 3. Quick Sort (rápido)
def quick_sort(lista):
    if len(lista) <= 1:
        return lista
    else:
        pivote = lista[0]
        menores = [x for x in lista[1:] if x["año"] <= pivote["año"]]
        mayores = [x for x in lista[1:] if x["año"] > pivote["año"]]
        return quick_sort(menores) + [pivote] + quick_sort(mayores)

# 4. Búsqueda binaria por año
def busqueda_binaria(lista, año_objetivo):
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio]["año"] == año_objetivo:
            return lista[medio]
        elif lista[medio]["año"] < año_objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1
    return None

# 5. Ejecutar ordenamientos y medir tiempos
año_a_buscar = 2005

inicio = time.time()
orden_bubble = bubble_sort(biblioteca)
tiempo_bubble = time.time() - inicio
resultado_bubble = busqueda_binaria(orden_bubble, año_a_buscar)

inicio = time.time()
orden_quick = quick_sort(biblioteca)
tiempo_quick = time.time() - inicio
resultado_quick = busqueda_binaria(orden_quick, año_a_buscar)

# 6. Mostrar resultados
print("\n--- COMPARACIÓN DE ORDENAMIENTOS ---")
print(f"Bubble Sort tomó: {tiempo_bubble:.4f} segundos")
print(f"Quick Sort tomó : {tiempo_quick:.4f} segundos")
print(f"Diferencia     : {tiempo_bubble - tiempo_quick:.4f} segundos")

print("\n--- RESULTADOS DE BÚSQUEDA BINARIA ---")
print("Resultado en lista ordenada con Bubble Sort:", resultado_bubble)
print("Resultado en lista ordenada con Quick Sort:", resultado_quick)

# 7. Conclusión sugerida para video o informe:
# Quick Sort es mucho más eficiente que Bubble Sort en listas grandes.
# Ambas listas ordenadas permiten aplicar búsqueda binaria con buenos resultados.
