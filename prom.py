nota1=int(input("Ingresar nota 1"))
nota2=int(input("Ingresar nota 2"))
nota3=int(input("Ingresar nota 3"))
promedio=(nota1+nota2+nota3)/3
if(nota1 <1) or(nota1 >10)or(nota2 <1) or (nota2 >10)or (nota3 <1) or (nota3 >10):
    print ("Error")
if promedio >= 1 and promedio <6:
    print ("EP")
elif promedio >=6 and promedio<=8:
    print ("S")
elif promedio>=8 and promedio<10:
    print ("A")
else:
    print("No Error")
