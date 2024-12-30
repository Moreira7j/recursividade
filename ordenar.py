def ordenar(lista):
    if len(lista) <= 1:
        return True
    else:
        if lista[0] > lista[1]:
            return False
        else:
            return ordenar(lista[1:])
        
resultado = ordenar([1,2,3,2])
print(resultado)