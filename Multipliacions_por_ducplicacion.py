def multiplicacion_rusa_campesino(a, b):
    
    if a == 0 or b == 0:
        return 0
    
    elif a % 2 == 1:
        return b + multiplicacion_rusa_campesino(a // 2, b * 2)
    else:
        return multiplicacion_rusa_campesino(a // 2, b * 2)

print(multiplicacion_rusa_campesino(27,82))