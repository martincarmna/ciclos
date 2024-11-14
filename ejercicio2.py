'''
Crea una programa que pida un número y calcule su factorial (El factorial de 
un número es el producto de todos los enteros entre 1 y el propio número y se 
representa por el número seguido de un signo de exclamación. 
Por ejemplo 5! = 1x2x3x4x5=120)
'''

n = int(input("ingresa el numero:  "))
factorial = 1
if n < 0:
    print("Error el factorial no se realiza en numeros negativos")
elif n == 0:
    print(" el factorial de 0 es 1")

else:
 for i in range(1, n +1):
    factorial *= i
    print(f"El factorial de {n} es {factorial}")


          


