#Bifurcacion
'''
a=50
if a%2 == 0:
    print(f"El valor {a} es un numero par")
else:
    print(f"El numero {a} es impar")


if a>50:
    print(f"El valor {a} es mayor de 50")
elif a<50:
    print(f"El valor {a} es menor de 50")
else:
    print(f"El valor {a} es 50")

num= input("Introduce un valor: ")
print(f"Valor introducido: {num}") #input siempre devuelve una cadena de  caracteres

num= int(num)
a=0
while a<num:
    print(f"a: {a}")
    a+=1

    sum = 0
for a in range(10):
    sum+=a
    print(f"(a: {a} sum: {sum})")
'''
#bucle que solicite numeros al usuarios hasta que se introduzca un numero par
result = input("Introduce un numero: ")
result = int(result)

while result%2 != 0:
    result = input("Introduce otro numero: ")
    result = int(result)
print(f"Valor final: {result}")



