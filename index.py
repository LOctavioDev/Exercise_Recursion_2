def mostrar_numeros(n):
    if n < 11:
        print(n)
        mostrar_numeros(n + 1)
        if n != 10:
            print(n)
         
         
print(mostrar_numeros(1))