examen_P=True
identificacion=True
requisitos1= ["tener al menos 18 años","aprobar el examen teórico y práctico de conducir","una identificación válida"]
print(f"bienvenido al sistema de licencias de conducir, los requisitos son: {requisitos1}")

edad=(input("ingrese edad: "))
if edad.isdigit():
    edad=int(edad)
elif not edad.isdigit():
        print("por favor ingrese un numero valido")
        edad=(input("ingrese edad: "))
        
        while not edad.isdigit():
           print("por favor ingrese un numero valido")
           edad=(input("ingrese edad: "))
           if edad.isdigit():
            edad=int(edad)  
            break

if edad>=18:
    edad= True
    print("puedes conducir")
elif edad<18:
    edad= False
    print("no puedes conducir")
    edad= False
if edad>= 50:
    edad== True
    print("Ya que tienes mas de 50 años, debes realizar un examen medico")
elif edad>= 70:
    edad== False
    print("Ya no puedes conducir")

examen_t=True or False
examen_t=input("pasaste el examen de conducir? (si/no): ")
if examen_t==("si"):
    examen_t=True
elif examen_t==("no"):
    examen_t=False
while examen_t not in ("si","no"):
        print("respuesta invalida, por favor ingrese si o no")
        examen_t=input("pasaste el examen de conducir? (si/no): ")
        if examen_t==("si"):
            examen_t=True  
        elif examen_t==("no"):
            examen_t=False
            break
        

requisitos=[edad,examen_t,identificacion,examen_P]
if all(requisitos):
    print("felicidades, ya tienes tu licencia de conducir")
else:
    print("lo siento, no tienes tu licencia de conducir", requisitos)
