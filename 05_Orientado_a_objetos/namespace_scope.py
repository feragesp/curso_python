
# # print(dir(__builtins__))


# var = "Hola"

# var_global = 30
# print(globals())

# if 4 > 2:
#     print(var)

# def func_1():
    
#     global var_global
#     var_global += 1
#     def func_2():
#         def func_3():
#             var_local = "SOY LOCAL"
#             print(var_local)
#             # print("fun3", var)
#             if var == "Hola":
#                 print("Si soy", var)
#         func_3()
#         # print(locals())
#     func_2()

# func_1()
# print(var_global)


# i = 0
# while i < 10:
#     print(i)
#     i += 1


var_global = 30
print(var_global)

def func1():
    global var_global
    var_global *= 2
    print(var_global)
    print("-"*10)
    var_local = 3
    print(var_local)
    def fun2():
        nonlocal var_local
        var_local +=1
    fun2()
    print(var_local)
func1()
print("-"*10)
print(var_global)