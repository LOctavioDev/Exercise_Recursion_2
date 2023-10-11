# def multiplicar_matrices(A, B):
    
#     if len(A[0]) != len(B):
#         raise ValueError("Las matrices no son multiplicables. El número de columnas de la matriz A debe ser igual al número de filas de la matriz B.")
    
    
#     filas_A = len(A)
#     columnas_A = len(A[0])
#     columnas_B = len(B[0])

#     resultado = [[0 for _ in range(columnas_B)] for _ in range(filas_A)]

    
#     def multiplicar(fila_A, columna_B, k):
#         if fila_A < filas_A:
#             if columna_B < columnas_B:
#                 if k < columnas_A:
#                     resultado[fila_A][columna_B] += A[fila_A][k] * B[k][columna_B]
#                     multiplicar(fila_A, columna_B, k + 1)
#                 else:
#                     multiplicar(fila_A, columna_B + 1, 0)
#             else:
#                 multiplicar(fila_A + 1, 0, 0)
    
    
#     multiplicar(0, 0, 0)

#     return resultado


# matriz_A = [
#         [1, 2, 1, 2], 
#         [3, 1, 2, 1],
#         [4, 2, 1, 1]
#            ]

# matriz_B = [
#         [2, 1], 
#         [3, 2], 
#         [1, 2],
#         [1, 1]
#            ]

# resultado_multiplicacion = multiplicar_matrices(matriz_A, matriz_B)

# print("Resultado de la multiplicación:")
# for fila in resultado_multiplicacion:
#     print(fila)
    
    
    
# print([[0 for _ in range(2)]])

data_A =    [
            [1, 2],
            [3, 1],
            ]

print("\n".join(["  ".join(map(str, row)) for row in data_A]))