def sudcadena(texto,inicio):
# Toma los valores inicio hacia atras.
    resultado=texto[inicio::-1]
    return resultado
texto="HOLA MUNDO"
resultado=sudcadena(texto,8)
print(resultado)