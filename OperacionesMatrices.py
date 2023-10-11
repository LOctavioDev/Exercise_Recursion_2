class Matrix: #DECLARO LA CLASE DE MATRIX
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])

    def __str__(self):
        return "\n".join(["   ".join(map(str, row)) for row in self.data])

    def suma(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            raise ValueError("LAS MATRICES DEBEN TENER LA MISMA DIMENSION PARA LA SUMA.")
        
        resultado = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        def suma_recursiva(i, j):
            if i < self.rows:
                if j < self.cols:
                    resultado[i][j] = self.data[i][j] + matrix.data[i][j]
                    suma_recursiva(i, j + 1)
                else:
                    suma_recursiva(i + 1, 0)
        
        suma_recursiva(0, 0)

        return Matrix(resultado)
    
    
    def resta(self, matrix):
        if self.rows != matrix.rows or self.cols != matrix.cols:
            raise ValueError("LAS MATRICES DEBEN TENER LA MISMA DIMENSION PARA LA RESTA.")
        
        resultado = [[0 for _ in range(self.cols)] for _ in range(self.rows)]

        def resta_recursiva(i, j):
            if i < self.rows:
                if j < self.cols:
                    resultado[i][j] = self.data[i][j] - matrix.data[i][j]
                    resta_recursiva(i, j + 1)
                else:
                    resta_recursiva(i + 1, 0)
        
        resta_recursiva(0, 0)

        return Matrix(resultado)



    def multiplicar(self, matrix):
        if self.cols != matrix.rows:
            raise ValueError("EL NUM DE COLUMNAS DE LA MATRIZ A DEBE SER IGUAL AL NUMERO DE FILAS DE LA MATRIZ B.")

        resultado = [[0 for _ in range(matrix.cols)] for _ in range(self.rows)]

        def multiplicar_recursiva(i, j, k):
            if i < self.rows:
                if j < matrix.cols:
                    if k < self.cols:
                        resultado[i][j] += self.data[i][k] * matrix.data[k][j]
                        multiplicar_recursiva(i, j, k + 1)
                    else:
                        multiplicar_recursiva(i, j + 1, 0)
                else:
                    multiplicar_recursiva(i + 1, 0, 0)
        
        multiplicar_recursiva(0, 0, 0)

        return Matrix(resultado)


data_A =    [
            [1, 4, 5],
            [1, 6, 1]
            ]

data_B =    [
            [4, 1, 3],
            [3, 2, 2],
            [2, 3, 1],
            ]

matrix_A = Matrix(data_A)
matrix_B = Matrix(data_B)

print("Matriz A:")
print(matrix_A)

print("\nMatriz B:")
print(matrix_B)

resultado_multiplicacion = matrix_A.multiplicar(matrix_B)
print("\nResultado de la multiplicación:")
print(resultado_multiplicacion)