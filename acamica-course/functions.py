from math import pow


def welcome():
    print("Welcome to working with functions")


def greeting(name):
    print("Hello, {}".format(name))


def potencia(x, y=2):
    """
    Eleva un número x a la potencia y
    :param x: base
    :param y: exponente (opcional, si no se especifica su valor por defecto es 2)
    :return: x^y
    """
    return int(pow(x, y))


def makeTuple(x, y, z):
    return (x,y,z)


def makeList(x, y, z):
    return [x,y,z]


def returnMultiple():
    return 1, 2, 3


def varSum(*args):
    try:
        return sum(args)
    except TypeError as err:
        print("Invalid data type: ", err)
        return 0


def kwVarSum(**kwargs):
    try:
        return sum(kwargs.values())
    except TypeError as err:
        print("Invalid data type: ", err)
        return 0


def testFinally(a, b):
    c = 0
    try:
        c = a / b
    except ZeroDivisionError:
        print("Cannot divide by zero")
        exit(1)
    finally:
        print("c =", str(c))


welcome()
greeting("Pipe")
print("3^2 = {}".format(str(potencia(3))))          # uso exponente por defecto (2)
print("2^3 = {}".format(str(potencia(2, 3))))       # uso de ambos parámetros
print("2^4 = {}".format(str(potencia(y=4, x=2))))   # uso de parámetros especificados en orden inverso

T = makeTuple(1,2,3)
print(str(T))
print(type(T))

L = makeList(1,2,3)
print(str(L))
print(type(L))

a, b, c = returnMultiple()
print("a ={}, b = {}, c = {}".format(a, b, c))

print(str(varSum(1, 2, 3)))
print(str(varSum(4, 5, 6, 7)))
print(str(varSum("a", "b")))

print(str(kwVarSum(a=8, b=9, c=10)))
print(str(kwVarSum(a=11, b=12, c=13, d=14)))
print(str(kwVarSum(a="a", b="b")))

testFinally(4, 0)
testFinally(4, 2)