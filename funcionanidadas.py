def exterior():
    def interior():
        return "hola desde la funcion interior"
    return interior()
print(exterior())