def filtrar_numeros_pares(lista):
    pares = []
    for numeros in lista:
        if (numeros % 2) == 0:
            pares.append(numeros)
    return pares
lista=[2,3,4,5,6]
resultado=filtrar_numeros_pares(lista)
print(resultado)