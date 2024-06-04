# Leer dos números enteros y si la diferencia entre los dos números es par mostrar en pantalla la suma de los dígitos de los números, si dicha diferencia es un número primo menor que 10 entonces mostrar en pantalla el producto de los dos números y si la diferencia entre ellos terminar en 4 mostrar en pantalla todos los dígitos por separado.

def suma_numeros(num):
    return sum(int(digit) for digit in str(num))
def es_primo(num):
    if num < 2:
        return False
    def es_primo(num):
        if num < 2:
            return False
        return all(num % i != 0 for i in range(2, int(num**0.5) + 1))
num1 = int(input("Ingrese un número: "))
num2 = int(input("Ingrese otro número: "))
diferencia = abs(num1 - num2)
condiciones_cumplidas = False
if diferencia % 2 == 0:
    suma_total_digitos = suma_numeros(num1) + suma_numeros(num2)
    print(f"La suma de los dígitos de {num1} y {num2} es: {suma_total_digitos}")
    condiciones_cumplidas = True
if diferencia < 10 and es_primo(diferencia):
    producto = num1 * num2
    print(f"El producto de {num1} y {num2} es: {producto}")
    condiciones_cumplidas = True
if str(diferencia)[-1] == '4':
    print(f"Los dígitos de {num1} son: ", end="")
    for digit in str(num1):
        print(digit, end=" ")
    print(f"\nLos dígitos de {num2} son: ", end="")
    for digit in str(num2):
        print(digit, end=" ")
    condiciones_cumplidas = True
if not condiciones_cumplidas:
    print("No se cumple ninguna de las condiciones")
