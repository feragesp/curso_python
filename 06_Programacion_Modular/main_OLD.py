
# import mi_modulo
from mi_modulo import * 

def func(arg):
    print(arg)

"""def my_function(arg):
    print("Imprimo desde Main")
    print(arg)"""

"""dic = {
    "key1": 10,
    "key1": -8
}"""


if __name__ == "__main__":
    func("Buenos dias")
    a = int(input("Valor A:"))
    b = int(input("Valor B:"))
    mi_suma(a, b)
    #my_function("Necesito un cafe")
    #funcioncita("Necesito un cafe")
    #print(dic)
    # print(globals())
    print("NAME de main.py", __name__)