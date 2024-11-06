import math 
import statistics
import random

def raiz(value):
    return math.sqrt(value)

def fatorial(value):
    return math.factorial(value)

def potencia(value):
    return math.pow(value, 2)

def main():
 a = int(input("Insira o valor de A: "))
 b = int(input("Insira o valor de B: "))
 c = int(input("Insira o valor de C: "))
    
 delta = b**2-4*a*c
 if delta < 0:
    print("A equação tem raiz de valor menor que zero!")
 elif delta == 0:
    x = -b / (2*a)
    print("A equação possuí raiz única, x")
 else:
    x1= (-b + raiz(delta))/(2*a)
    x2= (-b - raiz(delta))/(2*a)
    print("As raizes da equação são:",x1," e ",x2)

main()