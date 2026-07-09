#comprension de lista forma corta,estructura basica => [ expresión  for  elemento  in  iterable ]
cuadrado=[numero**2 for numero in range (5)]
print(cuadrado)

 #filtra elementos usando if => [ expresión  for  elemento  in  iterable  if  condición ], if va al final

pares=[n for n in range(10) if n % 2 == 0]
print(pares)

 #tranformar elementos

nombres=["ana","maria","jose"]
mayuscula=[nombre.upper() for nombre in nombres]
print(mayuscula)

#if...else como tranformacion => [ expresión_si_cumple  if  condición  else  expresión_si_no_cumple  for  elemento  in  iterable ]

pares=["par" if n % 2 ==0 else "impar" for n in range(10)]
print(pares)