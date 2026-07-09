tabla=[[fila*columna for columna in range (1,6)] for fila in range (1,6)]

for fila in tabla:
    print(fila)

#matriz de identidad
identidad=[[1 if fila==columna else 0 for columna in range(5)] for fila in range(5)]
for fila in identidad:
    print(fila)