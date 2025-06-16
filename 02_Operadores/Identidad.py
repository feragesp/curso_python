# IDENTIDAD: "is" => TRUE si X e Y son el mismo objeto
# IDENTIDAD: "is not" => TRUE si X e Y NO son el mismo objeto
# Hola Mundo
help(id)

text1 = input("Introduce texto ")
print("text1 ", id(text1))

text2 = input("Introduce texto ")
print("text2 ", id(text2))

print("IDENTIDAD 'is' ", text1 is text2)
print("COMPARACION", text1 == text2)
print("IDENTIDAD 'is not' ", text1 is not text2)
