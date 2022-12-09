"""Crear un bucle que cuente todos los números pares hasta el 100 

x = 1
while x <= 100:
    if x % 2 == 0:
        print("El numero" , x , "es par")
        
    x = x + 1 """
    

"""Dado un número, cuente el número total de dígitos de un número
Por ejemplo, el número es 75869, por lo que la salida debería ser 5.

user_input = int(input(("Ingresa un numero: ")))
user_input = abs(user_input)
print("Tu numero original es : {} ".format(user_input))

count = 0
while user_input > 0 :
     user_input //= 10
     count += 1
    
print("Los digitos de tu número son: {} ".format(count)) """


"""Imprima el siguiente patrón con el ciclo for:

 
def numpat(n):
   
    num = 5 
 
    for i in range(n, 0 ,-1):
        for j in range(1,i+1):
         print(j, end=" ")
        num = num - 1
    
        print()
 
n = 5
numpat(n)"""
