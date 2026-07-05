lista=[2,3,4,3,45,33]
def numero_veces(lista,num):
    veces=0
    for i in range (0,len(lista)):
        if lista[i]==num:
            veces+=1
    return veces
print(f"el numero 3 se repite{numero_veces(lista,3)}")