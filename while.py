"""
ciclo while (mientras) 
while exp_booleana:
   instrucciones
   actualizacion de valores
"""

num = 0
while num < 10:
    print(f"hello { num }")
    num = num + 5

    # Mas operadores matematicos
    '''
    n = n + 5 == n += 5
    n = n - 5 == n -= 5
    n = n * 5 == n *= 5
    n = n / 5 == n /= 5
    '''

'''
Implementancion Do While (hacer, hasta) en Python

while True:
   instrucciones
   if exp_bool:
      break

'''
while True: 
option = input('escribe salir:')
if option == 'salir'
   break
