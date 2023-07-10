print('"ADIVINA LA PALABRA"')
name = input ("Por favor ingrese su nombre: ")
print(f"Bienvenida/o {name},\n¿Estás lista/o para jugar?")
respuesta = input ("Responde SI o NO: ")
if respuesta.upper() == "SI":
    print (f"¡QUE COMIENCE EL JUEGO!")
    print(f"Deberás elegir letras para adivinar la palabra oculta. Cuentas con cinco vidas, en caso de agotarlas perderàs el juego ")
else: print (f"¡Que pena! Te esperamos pronto")
