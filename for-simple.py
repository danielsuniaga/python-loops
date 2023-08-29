"""Rutina que nos permite ver diferentes ejemplos de FOR"""

miEmail=input("Introduce tu dirección de email: ")

for i in ["Pildoras","Informática",3]:

    print("Hola",end=" ")

print("segunda cadena")

contador=0

for i in miEmail:

    if(i=="@" or i=="."):

        contador=contador+1

if contador==2:

    print("Email es correcto")

else:

    print("El email no es correcto")

for letra in "Python":

    if letra=="h":

        continue
    
    print("Viendo la letra: "+letra)

nombre="Pildoras Informaticas"

contador=0

for i in nombre:

    if i==" ":

        continue

    contador+=1

print(contador)