def limite(lista, num):
    if len(lista) == 0:
        return 0
    elif lista[0] > num:
        return 1 + limite(lista[1:], num)
    else:
        return limite(lista[1:], num)
    
resultado = limite([1,2,3,3,4,5], 2)
print(resultado)
