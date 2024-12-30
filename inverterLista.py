def inverter(lista):
    if len(lista) <= 1:
        return lista
    else:
        return inverter(lista[1:]) + [lista[0]]

resultado = inverter([1,2,3,4])


print(resultado)
    