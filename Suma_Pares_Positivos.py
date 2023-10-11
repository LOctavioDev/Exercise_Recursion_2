while True:
    N = int(input("INGRESA N: "))
    def calcular_suma(N):
            if N < 2:
                return 0  
            elif N % 2 != 0:
                return "Error: N es impar" 
            else:
                return N + calcular_suma(N - 2)

    print(calcular_suma(N))