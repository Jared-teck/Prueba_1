import random

elementos = "¿1234567890-abcdefghijklmnopqrstuvwxyz"
pass_length = int(input("introdusca la longitud del pase:"))

password = ""

for i in range(pass_length):
    password += random.choice(elementos)

print(password)