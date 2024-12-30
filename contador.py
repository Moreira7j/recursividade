def ocorrências(lista, num):
    if len(lista) == 0:
        return 0
    elif lista[0] == num:
        return 1 + ocorrências(lista[1:], num)
    else:
        return ocorrências(lista[1:], num)
    

resultado = ocorrências([1,2,3,3,3,3,4,5,6,6], 3)

print(resultado)