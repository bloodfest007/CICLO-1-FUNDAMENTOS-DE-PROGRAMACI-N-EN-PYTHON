print("---------")
print("Diccionarios")
print("---------")

#!DICCIONARIOS
"""nombre = input("Su nombres es: ")
apellidos = input("Su Apellidos: ")
edad = input("Su edad es: ")
correo = input("Su correo es: ")
celular = input("Su numero es: ")
direccion = input("Su dirección es: ")

datos = {"Nombres" : nombre, "Apellidos" : apellidos, "Edad" : edad, "Correo" : correo,"Celular": celular ,"Direccion": direccion}

print(datos["Nombres"], datos["Apellidos"], datos["Edad"], datos["Correo"], datos["Celular"], datos["Direccion"])
"""
mi_diccionario = {  "Nombre" : "victor", 
                    "Apellido" : "gonzalez", 
                    "edad" : "36", 
                    "genero" : "masculino"
                 }

print(mi_diccionario["Nombre"], mi_diccionario["Apellido"],mi_diccionario["edad"],mi_diccionario["genero"])
print("---------")
mi_informacion = {  "Nombre" : "victor", 
                    "Apellido" : "gonzalez", 
                    "Sobrenombre": "VG",
                    "Padres" : ["Marin Gomez", "Julian cortez"],
                    "edad" : "36", 
                    "genero" : "masculino",
                    "estado civil": "Soltero",
                    "Hijos": "0",
                    "mascotas":"perro",
                    "nombre de mascotas": ["Chato"]
                 }

print(mi_informacion["Nombre"],mi_informacion["Apellido"],mi_informacion["Sobrenombre"],mi_informacion["Padres"],mi_informacion["edad"],
     mi_informacion["genero"],mi_informacion["estado civil"],mi_informacion["Hijos"],mi_informacion["mascotas"],mi_informacion["nombre de mascotas"],)

#* Añadir campos al diccionario
mi_informacion["Celular"] = "123456789"
mi_informacion["Salario"] = "500000"
print("---------")

print(mi_informacion["Celular"])
print(mi_informacion["Salario"])
print("---------")

print(mi_informacion["Nombre"],mi_informacion["Apellido"],mi_informacion["Sobrenombre"],mi_informacion["Padres"],mi_informacion["edad"],
     mi_informacion["genero"],mi_informacion["estado civil"],mi_informacion["Hijos"],mi_informacion["mascotas"],mi_informacion["nombre de mascotas"],mi_informacion["Celular"],
     mi_informacion["Salario"])
print("---------")

#*Modificar registro existentes
mi_informacion["edad"] = 45
print(mi_informacion["edad"])
print("---------")

print(mi_informacion["Nombre"],mi_informacion["Apellido"],mi_informacion["Sobrenombre"],mi_informacion["Padres"],mi_informacion["edad"],
     mi_informacion["genero"],mi_informacion["estado civil"],mi_informacion["Hijos"],mi_informacion["mascotas"],mi_informacion["nombre de mascotas"],mi_informacion["Celular"],
     mi_informacion["Salario"])
print("---------")

#*
print(mi_informacion.get("casa", "este dato no existe"))


