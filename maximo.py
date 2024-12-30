def encontrar_maximo(lista):
    # Caso base: quando a lista tiver apenas um elemento
    if len(lista) == 1:
        return lista[0]
    else:
        # Recursão: compara o primeiro número com o máximo do restante da lista
        max_resto = encontrar_maximo(lista[1:])
        if lista[0] > max_resto:
            return lista[0]
        else:
            return max_resto

       
print(encontrar_maximo([1,2,3,4,7])) 
