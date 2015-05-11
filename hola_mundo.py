complemento = 'tu nombre es '
complemento_2 = 'tu primer apellido es '
complemento_3 = 'y tu segundo apellido es '
espacio = "     "
yes = 'yes'
no_t = 'not'
#puntos = False

usuario_1 = raw_input ('por favor ingrese su nombre ')
usuario_2 = raw_input ('por favor inrese su primer apellido ')
usuario_3 = raw_input ('por favor ingrese su segundo apellido ')

def funcion(nombre):
    nombre = "daniel"
    cuatro = " 4"
    return "Hola " + nombre + cuatro

def resultados(func=""):
        if func in globals():
                if callable(globals()[func]):
                        return globals()[func]("")
                else:
                        return "funtion no encontrer"
print resultados("funcion")
#function----------------------------------------------------------

def preguntas():
        print "vienvenido a esta primer parte, por favor responde el juego de preguntas que te haremos a continuacion."
        pregunta1 = raw_input ('cual es la capital de colombia ... ')
        if pregunta1 == "bogota" or pregunta1 == "Bogota" or pregunta1 == "BOGOTA":

                puntos = True
                if puntos == True:
                        puntos += 10
                        print puntos , "puntos"
                pregunta2()
        else:
                print "perdiste vuelve a intertar"
                puntos = False
                if puntos == False:
                        puntos = 0
                        print puntos , "puntos"
                preguntas()

def pregunta2():
        pregunta_2 = raw_input ('quien descubrio a america ... ')
        if pregunta_2 == "cristobal colon" or pregunta_2 == "Cristobal Colon" or pregunta_2 == "CRISTOBAL COLON" or pregunta_2 == "Cristobal colon":

                puntos = True
                if puntos == True:
                        puntos +=10
                        print puntos , "puntos"
        else:
                print "perdiste vuelve a intentarlo"
                puntos = False
                if puntos == False:
                        puntos -=10
                        print puntos , "puntos"
                pregunta2()


#        respuesta_1 = "bogota"
#        respuesta_2 = "cristobal colon"
#        respuesta_3 = "CRISTOBAL COLON"
#        respuesta_4 = "Cristobal colon"

def responder():
        usuario_4 = raw_input ("si esto es verdad por favor ingresa " + yes + " o " + no_t + " ")

        if usuario_4 == yes:
                print "gracias por llenar esta solicitud"
                preguntas()
        elif usuario_4 == no_t:
                print "lo lamentamos mucho por favor espera un momento...."
        else:
                        print "no me respondiste nada por favor vuelve a intentarlo"
                        responder()

def seg_apellido():
        if len(usuario_3) > 0 and usuario_3.isalpha():
                ape_2 = usuario_3.lower()
                ape_2Completo = (complemento_3 + ape_2)
                print ape_2Completo
                responder()
        else:
                print "no se ingreso ningun valor"
                seg_apellido()

def apellido():
        if len(usuario_2) > 0 and usuario_2.isalpha():
                ape = usuario_2.lower()
                apeCompleto = (complemento_2 + ape)
                print apeCompleto
                seg_apellido()

        else:
                print "no se ingreso ningun valor"


if len(usuario_1) > 0 and usuario_1.isalpha():
    nombre = usuario_1.lower()
    nombreCompleto = (complemento + nombre)
    print nombreCompleto
    apellido()

else:
    print "no se ingreso ningun valor"





