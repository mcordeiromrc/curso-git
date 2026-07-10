# Calculadora com operações básicas, potência e raiz quadrada
import math

def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def potencia(a, b):
    return a ** b

def dividir(a, b):
    if b == 0:
        raise ValueError('Divisão por zero nao permitida')
    return a / b

def raiz_quadrada(a):
    if a < 0:
        raise ValueError('Não existe raiz quadrada de número negativo')
    return math.sqrt(a)

# TODO: Adicionar função de divisão inteira