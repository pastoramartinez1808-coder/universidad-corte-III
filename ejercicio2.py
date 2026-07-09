lista=[1,2,3,4,5,6,7,8,9,10]
cuadrados=[n**2 for n in lista]
pares=[n for n in lista if (n % 2 ==0)]
impares=[n*10 for n in lista if (n % 2 !=0)]
print(f"la lista =>{lista} \n al elevarlo al cuadrado => {cuadrados} \n sus numeros pares => {pares} \n impares por 10 =>{impares}")