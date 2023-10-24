# Crear un array 2D manualmente
mi_array_2d = [
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60],
    [65, 70, 75, 80]
]

# Imprimir el array en pantalla
for fila in mi_array_2d:
    print(' '.join(map(str, fila)))