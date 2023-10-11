class MatrixCalculator:
    def __init__(self):
        self.matrices = {}  # Un diccionario para almacenar matrices por nombre

    def parse_expression(self, expression):
        # DIVIENDO LA EXPRESION EN OPERADORES
        elements = expression.split()
        result = None
        operator = None

        for element in elements:
            if element in "+-*/":
                operator = element
            elif element in self.matrices:
                matrix = self.matrices[element]
                if result is None:
                    result = matrix
                else:
                    if operator == '+':
                        result = result.suma(matrix)
                    elif operator == '-':
                        result = result.resta(matrix)
                    elif operator == '*':
                        result = result.multiplicar(matrix)
                    elif operator == '/':
                        raise ValueError("LA DIVISION DE MATRICES NO ESTA DEFINIDA")
            else:
                raise ValueError(f"ESTE ELEMENTO ES DESCONOCIDO: {element}")

        return result

    def register_matrix(self, name, matrix):
        self.matrices[name] = matrix

class Matrix:
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



data_A = [
        [0, 0, 0],
        [0, 0, 0]
]

data_B = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
         ]

data_C = [
        [2, 3, 2],
        [2, 3, 2]
         ]

data_D = [
        [1, 4, 5],
        [1, 6, 1]
         ]

data_E = [
        [4, 1, 3],
        [3, 2, 2],
        [2, 3, 1],
         ]


calculator = MatrixCalculator()

matrix_A = Matrix(data_A)
matrix_B = Matrix(data_B)
matrix_C = Matrix(data_C)
matrix_D = Matrix(data_D)
matrix_E = Matrix(data_E)

calculator.register_matrix("A", matrix_A)
calculator.register_matrix("B", matrix_B)
calculator.register_matrix("C", matrix_C)
calculator.register_matrix("D", matrix_D)
calculator.register_matrix("E", matrix_E)


expression = "A * B + C"
result = calculator.parse_expression(expression)

print(result)