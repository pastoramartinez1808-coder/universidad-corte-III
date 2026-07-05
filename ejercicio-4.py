def palabra_palindromo(palabra):
    return palabra==palabra[::-1]
word= input("Ingrese una palabra: ")
if palabra_palindromo(word):
    print(f"{word} es una palabra palindromo")
else: print(f"{word} no es una palabra palindromo")