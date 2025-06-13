# Diccionario

# Tipo de archivo "dict"
# {key:value, key2:value2, ..., keyn:valunen}

my_dic = {
    "Nombre":"Fernando",
    "Apellidos":"Aguilar Espinosa",
    "DNI":"12345678A",
    "País":"España",
    "Ciudad":"Barcelona"
}

# print(type(my_dic))
# print(my_dic)

dic2 = dict(
    Nombre="Fernando",
    Apellido="Aguilar",
    Ciudad="Barcelona"
)
# print(type(dic2))
# print(dic2)

# Acceso a un elemento []
# print(my_dic["DNI"])

my_dic_2 = {
    0:"Fernando",
    1:"Aguilar Espinosa",
    ("dos", 2):"España",
    3:"12345678A",
    "Ciudad":"Barcelona"
}
# print(my_dic_2[("dos", 2)])

my_dic_3 = {
    "Nombre":"Fernando",
    "Apellidos":"Aguilar Espinosa",
    "DNI":"12345678A",
    "País":"España",
    "Ciudad":"Barcelona"
}

# print(my_dic_3)
my_dic_3["Nombre"] = "Sergi"
my_dic_3["Apellidos"] = "Gonzalez"
# print(my_dic_3)
my_dic_3["Edad"] = 30
# print(my_dic_3)

my_dic_4 = {
    "int":10,
    "float":2.0,
    "str":"Fernandito",
    "lista":[1,2,3,4],
    "tupla":("a",2,"c"),
    "dic":{"k1":"value1", "k2":"value2"}
}
# print(my_dic_4["dic"]["k1"])

my_dic_5 = {
    "k1":10,
    "k2":30
}
# print(my_dic_5)

my_dic_6 = {
    "k1":10,
    "k2":30
}

print(my_dic_5 is my_dic_6)
print(my_dic_5 == my_dic_6)
