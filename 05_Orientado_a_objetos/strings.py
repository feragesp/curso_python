"""Trabajando con Strings"""

string = "Mi texto"
string = "HOLAAAA ME HE MODIFICADO"
print(string)
# print(dir(string))

# Transformaciones

string = "mOrEnItO rEcHuLoN"

print(string.capitalize())
print(string)

print(string.lower())
print(string.swapcase())
print(string.title())
print(string.upper())

print("Fernando@gmail.com" == "fernando@gmail.com")
string = "Fernando@gmail.com"
print(string.lower() == "fernando@gmail.com")

# Buscar y Reemplazar

texto = "aoo boo coo"

print(texto.count("oo"))
print(texto.find("boo"))

texto = "aoo boo coo boo"
print(texto.rfind("boo"))


texto = "aoo boo coo boo coo boo" # 12
primer_boo = texto.find("boo") # 4
segundo_boo = texto.find("boo", primer_boo + 1)
tercer_boo = texto.find("boo", segundo_boo + 1)

print("Nº de boo", texto.count("boo"))

print("1- boo", primer_boo)
print("2- boo", segundo_boo)
print("3- boo", tercer_boo)

# Clasificaciones de caracteres

texto1 = "123abc"
texto2 = "123$abc"

print(texto2.isalnum())
print(texto1.isdigit())

print(texto1[:3])
print(texto1[:3].isdigit())

# Format

texto3 = "Hola mundo"

print('|',texto3.center(20),'|')
print(texto3.rjust(20),"|")

texto4 = "                      HOLa             m         undo                                      "
print(texto4)
print(texto4.lstrip())
print(texto4.rstrip(), "|")
print("#"+texto4.strip()+"#")

print(texto4.replace(" ",""))

texto5 = "##3 ##3HOlA   qUE    tAl###"
#Hola Que Tal#

texto6 = texto5.title()
texto6 = texto6.strip('#3')
print(texto6.split())
texto6 = ' '.join(texto6.split())
print(texto6)

texto7 = "10"
print(texto7.zfill(8))

