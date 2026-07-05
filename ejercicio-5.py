lista=[1,23,22,34,56,77,12,14,2,6,8]
pares=[]
#Definir la funcion.
def filtra_numeros_pares(lista):
    #Recorrer la lista
    for i in range (len(lista)):
        if (lista[i] % 2==0):
            pares.append(lista[i])
    return (pares)

resultado=filtra_numeros_pares(lista)
print(resultado)