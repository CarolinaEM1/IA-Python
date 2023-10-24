import numpy as np

nombres = ['Python', 'C++', 'C', 'Fortran', 'Java', 'JavaScript', 'Kotlin']
print("Arreglo desordenado:")
print(nombres)

nombres_desordenados = np.random.permutation(nombres)
print("\nArreglo desordenado de manera aleatoria:")
print(nombres_desordenados)