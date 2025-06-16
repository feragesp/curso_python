cad4 = bytearray(bytes(9))
print("cadena_init",cad4)

c = ord('a') # 'a'
print("c_init",c)
i = 0
print("i_init",i)
while i < 9:
    cad4[i] = c
    print("cadena_parse",cad4)
    c = c + 1
    print("c++:",c)
    i += 1
    print("i++:",i)

print("cadena_final",cad4)

for i in cad4:
    cad4[i]
print("cadena_final",cad4)
