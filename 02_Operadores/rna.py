def relu(x):
    return max(0, x)

print(relu(10000))

from math import e

def sigmoid(x):
    return 1 / (1 + e**(-x))

print(e)
print(sigmoid(-2.5))

def sinh(x):
    return (e**x - e**(-x)) / 2

def cosh(x):
    return (e**x + e**(-x)) / 2

def tanh(x):
    return sinh(x) / cosh(x)

print(tanh(1))