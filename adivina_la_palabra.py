from random import choice

palabras = ['computadora', 'guitarra', 'elefante', 'bicicleta', 'television', 'mariposa', 'pescado', 'eleccion', 'cangrejo', 'cocodrilo', 'helicoptero']
letras_correctas = []
letras_incorrectas = []
vidas = 5
lista_abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
aciertos = []

def elegir_palabra (lista_palabras): 
  palabra_elegida  = choice(lista_palabras)
  return palabra_elegida.upper()

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
      
def pedir_letra(): 
   letra_ingresada = input ('Ingrese una letra: ')
   if len (letra_ingresada) > 1:
      print ("¡Solo puedes ingresar una letra!")
      return pedir_letra()
   elif letra_ingresada.upper() in lista_abecedario:
         return letra_ingresada.upper()
   else:
         print("¡Solo puedes ingresar una letra perteneciente al abecedario!")
         return pedir_letra()

     
    

palabra = elegir_palabra(palabras)
palabra_oculta = mostrar_guiones(palabra)



print('"ADIVINA LA PALABRA"')
name = input ("Por favor ingrese su nombre: ")
print(f"Bienvenida/o {name},\n¿Estás lista/o para jugar?")
respuesta = input ("Responde SI o NO: ")
if respuesta.upper() == "SI":
   print (f"¡QUE COMIENCE EL JUEGO!")
   print(f"Deberás elegir letras para adivinar la palabra oculta. Cuentas con cinco vidas, en caso de agotarlas perderás el juego ")
   print (palabra)
   print(palabra_oculta)
    
   while vidas >= 1:
      letras_unicas = set(palabra)
      letra_ingresada = pedir_letra () 
      validar_letra_ingresada (letra_ingresada)
      print (palabra_oculta)
       
      if letra_ingresada in letras_unicas:
         print (f'¡Felicidades! Has obtenido un acierto')
         letras_correctas.append(letra_ingresada)
          
      if letra_ingresada not in letras_unicas:
         vidas -= 1
         letras_incorrectas.append(letra_ingresada)
         

         if vidas == 0:
            print (f'¡Has perdido!')  
            print (f'Tu palabra secreta era: ¡{palabra}!')
         else:
            print(f'¡Has fallado! Vuelve a intentarlo...')   
            print(f'Tienes {vidas} vidas restantes')
     
       
   print (f'Lista de letras correctas: {letras_correctas}')
   print (f'Lista de letras incorrectas: {letras_incorrectas}')
          

else: print (f"¡Que pena! Te esperamos pronto")


