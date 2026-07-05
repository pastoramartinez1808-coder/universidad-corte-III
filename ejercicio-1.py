lista=[4,3,4,5,67,8]
def mayor_lista(lista):
    mayor=lista[0]
    for i in range (1,len(lista)):
        if lista[i]>mayor:
            mayor=lista[i]
    return(mayor)
print(f"el numero mayor del la lista es {mayor_lista(lista)}")
