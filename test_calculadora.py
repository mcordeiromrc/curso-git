from calculadora import somar, subtrair, multiplicar, dividir, potencia, raiz_quadrada

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(5, 3) == 2

def test_multiplicar():
    assert multiplicar(2, 3) == 6

def test_dividir():
    assert dividir(6, 3) == 2

def test_potencia():
    assert potencia(2, 3) == 8

def test_raiz_quadrada():
    assert raiz_quadrada(9) == 3
    assert raiz_quadrada(16) == 4
    assert raiz_quadrada(0) == 0

print('Todos os testes passaram!')