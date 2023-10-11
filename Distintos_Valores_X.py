def f(x):
    if x > 100:
        return x - 10
    else:
        return f(f(x + 11))
    
print(f()) 