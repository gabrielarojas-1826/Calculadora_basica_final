"""
Ejercicio 1

2025-02-20

Autora: Yulied Gabriela Rojas Rojas

Este es un ejemplo de una calculadora basica

"""

###inicio de codigo
#Recopilar los operandos
operando_a = int(input("escriba un numero entero: "))
operando_b = int(input("escriba otro numero entero: "))

resultado_suma=operando_a+operando_b
resultado_resta=operando_a-operando_b
resultado_multiplicacion=operando_a*operando_b
resultado_division=operando_a/operando_b
resultado_potenciacion=operando_a**operando_b

#Mostrar el resultado en pantalla
print(f"la suma de {operando_a} y {operando_b} es {resultado_suma}")
print(f"la resta de {operando_a} y {operando_b} es {resultado_resta}")
print(f"la multiplicacion de {operando_a} y {operando_b} es {resultado_multiplicacion}")
print(f"la division de {operando_a} y {operando_b} es {resultado_division}")
print(f"la potenciacion de {operando_a} y {operando_b} es {resultado_potenciacion}")

###final de codigo
