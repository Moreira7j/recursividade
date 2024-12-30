def reverter(palavra):
    if len(palavra) == 0:
        return ""
    else:
        return palavra[-1] + reverter(palavra[:-1] )
    
resultado = reverter("gustavo")
print(resultado)