import random
caracteres ="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
lon = int(input("introdusce la longitud de la contraseña"))
contraseña = ""
for i in range(lon):
    caracter = random.choice(caracteres)
    contraseña += caracter
print(contraseña)