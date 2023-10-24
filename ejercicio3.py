import numpy as np

# Crear un array 2D manualmente con números de tipo entero de 8 bits
mi_array_2d = np.array([
    [5, 10, 15, 20],
    [25, 30, 35, 40],
    [45, 50, 55, 60],
    [65, 70, 75, 80]
], dtype=np.int8)

# Imprimir el array en pantalla
print(mi_array_2d)

# Imprimir el tipo de array
print("Tipo de array:", mi_array_2d.dtype)