num = int(input("Digite o numero para ser fatorado: "))

def fatorial(num):
    if num == 0:
        return 1
    else:
        return num * fatorial(num-1)


resultado = fatorial(num)
print(resultado)