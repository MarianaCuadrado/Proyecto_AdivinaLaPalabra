from random import choice

palabras = ['computadora', 'guitarra', 'elefante', 'bicicleta', 'television', 'mariposa', 'pescado', 'eleccion', 'cangrejo', 'cocodrilo', 'helicoptero']
letras_correctas = []
letras_incorrectas = []
vidas = 5

def elegir_palabra (lista_palabras): 
  palabra_elegida  = choice(lista_palabras) 
  return palabra_elegida

def mostrar_guiones (palabra):
    letras_ocultas = [] 
    for letra in palabra:
       letras_ocultas.append("_")
    return letras_ocultas 

def validar_letra_ingresada (letra):
    i = 0
    for l in palabra:
      if letra == l:
         palabra_oculta[i] = l
      i += 1
      
      
      

palabra = elegir_palabra(palabras)
palabra_oculta = mostrar_guiones(palabra)




print('"ADIVINA LA PALABRA"')
name = input ("Por favor ingrese su nombre: ")
print(f"Bienvenida/o {name},\n¿Estás lista/o para jugar?")
respuesta = input ("Responde SI o NO: ")
if respuesta.upper() == "SI":
    print (f"¡QUE COMIENCE EL JUEGO!")
    print(f"Deberás elegir letras para adivinar la palabra oculta. Cuentas con cinco vidas, en caso de agotarlas perderàs el juego ")
    print (palabra)
    print(palabra_oculta)
    
    while vidas >= 1:
       letra_ingresada = input ('Ingrese una letra: ')
       validar_letra_ingresada (letra_ingresada)
       print(palabra_oculta)

else: print (f"¡Que pena! Te esperamos pronto")


