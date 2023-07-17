from random import choice

palabras = ['computadora', 'guitarra', 'elefante', 'bicicleta', 'television', 'mariposa', 'pescado', 'eleccion', 'cangrejo', 'cocodrilo', 'helicoptero']
letras_correctas = []
letras_incorrectas = []
vidas = 5
aciertos = 0
lista_abecedario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

def elegir_palabra (lista_palabras): 
  palabra_elegida  = choice(lista_palabras)
  return palabra_elegida.upper()

def mostrar_guiones (palabra):
    letras_ocultas = [] 
    for letra in palabra:
       letras_ocultas.append("_")
    return letras_ocultas 

def validar_letra_ingresada (letra):
   global vidas
   global aciertos
   i = 0
   for l in palabra:
      if letra == l:
         palabra_oculta[i] = l
      i += 1
   if letra_ingresada in letras_unicas:
         print (f'\n¡Felicidades! Has obtenido un acierto')
         aciertos += 1
         letras_correctas.append(letra_ingresada.upper())
         if aciertos == len(letras_unicas):
             print(f'\n¡GANASTE!')
             print (f'\nTu palabra secreta era:')           
            
   if letra_ingresada not in letras_unicas:
      vidas -= 1
      letras_incorrectas.append(letra_ingresada.upper())
      if vidas == 0:
         print (f'\n¡Has perdido!')  
         print (f'\nTu palabra secreta era: ¡{palabra}!')
      else:
         print(f'\n¡Has fallado! Vuelve a intentarlo...')   
         print(f'\nTienes {vidas} vidas restantes')

def pedir_letra(): 
   letra_ingresada = input ('\nIngrese una letra: ')
   if len (letra_ingresada) > 1:
      print ("\n¡Solo puedes ingresar una letra!")
      return pedir_letra()
   elif letra_ingresada.upper() in lista_abecedario:
      if letra_ingresada.upper() in letras_correctas or letra_ingresada.upper() in letras_incorrectas:
         print('\n¡Esta letra ya fue ingresada!')
         return pedir_letra()
      return letra_ingresada.upper()
   else:
      print("\n¡Solo puedes ingresar una letra perteneciente al abecedario!")
      return pedir_letra()
   

        
palabra = elegir_palabra(palabras)
letras_unicas = set(palabra)
palabra_oculta = mostrar_guiones(palabra)

print('\n"ADIVINA LA PALABRA"')
name = input ("\nPor favor ingrese su nombre: ")
print(f"\nBienvenida/o {name},\n\n¿Estás lista/o para jugar?")
respuesta = input ("\nResponde SI o NO: ")
if respuesta.upper() == "SI":
   print (f"\n¡QUE COMIENCE EL JUEGO!")
   print(f"\nDeberás elegir letras para adivinar la palabra oculta. Cuentas con cinco vidas, en caso de agotarlas perderás el juego ")
   print(f'\n{palabra_oculta}')
    
   while vidas >= 1 and aciertos < len(letras_unicas):
      letra_ingresada = pedir_letra ()
      validar_letra_ingresada (letra_ingresada)
      print (f'\n{palabra_oculta}')
      print (f'\nLista de letras correctas: {letras_correctas}')
      print (f'\nLista de letras incorrectas: {letras_incorrectas}')      
   
   print ('\n###################\n#¡JUEGO TERMINADO!#\n###################')
          

else: print (f"\n¡Que pena! Te esperamos pronto")


