while True:
    m,n = 0, 0
    m = int(input("INGRESA m: "))
    n = int(input("INGRESA n: "))
    

    def calcular_mcd(m, n):
        if m < n:
            m, n = n, m
        if n == 0:
            return m
        else:
            return calcular_mcd(n, m % n)
    print(calcular_mcd(m,n))