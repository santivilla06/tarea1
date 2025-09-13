print("--------BIENVENIDO A ELSECRETO DEL TEMPLO OLVIDADO--------\n")
print("Introduccion:\n")
print("Te encuentras en la entrada de un antiguo y misterioso templo en medio de la jungla amazónica, un lugar que los mapas no muestran y del que solo hablan las leyendas. Has buscado este lugar durante años, siguiendo los rastros de un explorador perdido que hablaba de un tesoro invaluable en su interior. Una pesada puerta de piedra, cubierta de enredaderas, bloquea tu paso. A un lado, hay una pequeña abertura en la pared, lo suficientemente grande como para que una persona se deslice.\n")

print("La jungla a tus espaldas parece oscurecerse y los sonidos de criaturas desconocidas se hacen más fuertes. Debes tomar una decisión rápida.")

decision_1 = input("Te encuentras en la entrada. ¿Qué harás?:\n1.EMPUJAR la pesada puerta de piedra.\n2.INVESTIGAR los alrededores en busca de otra entrada.\n¿Elige una opcion: ").upper()
if decision_1 == "EMPUJAR" or decision_1 == "1" :
    print("Con un esfuerzo sobrehumano, logras mover la puerta. Al entrar, escuchas un clic bajo tu pie. ¡Una trampa! Unos pinchos caen del techo justo delante de ti. ¿Qué haces?\n")
    decision_1_1 = input("1.SALTAR hacia atrás para salir del templo.\n2.CORRER hacia adelante para esquivar la trampa.\nElige una opcion: ").upper()
    if decision_1_1 == "SALTAR" or decision_1_1 == "1":
        print("\n\nSaltas hacia atrás justo a tiempo. Los pinchos se estrellan contra el suelo y el estruendo provoca que la pesada puerta de piedra se cierre con un golpe sordo, sellando la entrada principal. Estás fuera, pero tu camino original ha desaparecido.\nEl ruido de la trampa ha despertado a la jungla.Escuchas el rujido de de ramas y un gruñido bajo muy cerca.Debes actuar ya.\nEl reuido de la trampra a despertado a la jungla.Escuchas el crujido de ramas y un gruñido bajo muy cerca.Debes actuar ya \n") 
        decision_1_1_2 = input("¿Que haces?\n1.DESLIZARTE por pequeña abertura lateral.\n2.RODEAR el templo en busca de una entrada trasera.\n3.ESCONDERTE entre la densa maleza  y esperar a que pase el peligro.").upper() 
        if decision_1_1_2 == "DESLIZARTE" or decision_1_1_2 == "1" :
            print("Te deslizas a una cámara y encuentras tres objetos en un pedestal: una GEMA roja que pulsa con luz, un CÁLIZ de oro y un antiguo LIBRO. Solo puedes tomar uno. ¿Cuál eliges?.") 
            decision_1_1_2_1 = input("\n1.GEMA\n2.CALIZ\n3.LIBRO.\n ¿cual eliges?: ").upper()
            if decision_1_1_2_1 == "GEMA" or decision_1_1_2_1 == "1" : 
                print("Una puerta secreta se abre a un pasillo lleno de serpiente.La luz de la gema las mantiene a raya.Al final hay una puerta co un hueco en forma de sol.") 
                decision_1_1_2_1_2 = input("\n1.INSERTAR la gema.\n2.BUSCAR otro mecanismo ¿quye haces?: ").upper()
                if decision_1_1_2_1_2 == "INSERTAR" or decision_1_1_2_1_2 == "1" :
                    print("\n\nLa puerta se abre a la salida. La gema queda atras, pero eres libre.\n\n¡HAS ESCAPADO!") 
                elif decision_1_1_2_1_2 == "BUSCAR" or decision_1_1_2_1_2 == "2" : 
                    print("activa una trampa.\n\nFIN DEL JUEGO") 
                else : 
                    print("eligue una opcion valida") 
            elif decision_1_1_2_1 == "CALIZ" or decision_1_1_2_1 == "2" :
                print("Se revela una sala con una fuente de liquido plateado.Dos canales, marcados con un SOL y una LUNA, salen de ella.")
                decision_2 = input("cual eliges verter SOL o LUNA: \n").upper() 
                if decision_2 == "SOL" : 
                    print("el liquido hierve violentamente al tocar el simbolo del sol.Un gas espeso y de olor amrgo brota del canal,llenando la sala en segundos.No hay donde correr.\nLa trampa fue acctivada.\n\nFIN EL JUEGO") 
                elif decision_2 =="LUNA" : 
                    print("el liquido pateado fluye suavemente por el canal. Escuchas un chasquido y una seccion de la pared se desliza, revelando un pequeño cofre con monedas de plata antiguas y un mapa que muestra la salida segura de la jungla.\n\n¡HAS ENCONTRADO UN TESORO Y ESCAPADO!\n\n FIN") 
                else : 
                    print("eligue una opcion valida")  
            elif  decision_1_1_2_1 == "LIBRO" or decision_1_1_2_1 == "3" :
                print("lees un acertijo:hablo sin boca y oigo sin oidos...¿Que soy?")
                decision_1_1_2_1_3 = input("\nEn la pared hay tres grabados:\nVIENTO\nOTRA OPCION\n¿Cual escoges?:  ").upper() 
                if decision_1_1_2_1_3 == "VIENTO" :
                    print("Resuelves el acertijo (la respuesta es el eco).La pared se abre,revelando el tesoro principal del templo.\n\n¡HAS GANADO!") 
                elif decision_1_1_2_1_3 == "OTRA OPCION" :
                    print("activaste una trampa.\n\nFIN DEL JUEGO") 
                else :
                    print("elige una opcion valida ")
            else : 
                print ("elige una opcion valida ") 
        elif decision_1_1_2 == "RODEAR"  or decision_1_1_2 == "2" :
            print("Rodeas el templo y encuentras una cueva oculta tras una cascada. Dentro, un río subterráneo fluye hacia la oscuridad. Es tu única entrada.") 
            decision_3 = input("\nNADAR.\nCONSTRUIR.\nAVANZAR.\n").upper()
            if decision_3 == "NADAR" :
                print("El agua está helada. Más adelante, la corriente te arrastra hacia una bifurcación. El túnel de la IZQUIERDA tiene una débil luz y corriente suave. El de la DERECHA es oscuro y la corriente es violenta.")
                decision_3_1 = input("IZQUIERDA.\nDERECHA\n¿cual eligues?: ").upper() 
                if decision_3_1 == "IZQUIERDA" :
                    print(" Llegas a una gruta iluminada por hongos. En el centro, una estatua de serpiente se traga el agua. Escalas la estatua y encuentras un túnel seco que te lleva a una sala del tesoro olvidada y una salida.\n\n¡HAS ENCONTRADO EL TESORO OCULTO! Tu instinto te ha guiado bien. FIN.")
                elif decision_3_1 == "DERECHA" :   
                    print("La corriente violenta te arrastra hacia la oscuridad total. El rugido del agua es ensordecedor y sientes que pierdes el control. En la penumbra, apenas distingues una RAÍZ gruesa que cuelga de la pared y sientes ROCAS afiladas cerca de la superficie.")
                    decision_3_1_1 = input("\nAFERRARTE.\nSUMERGIRTE.\n¿Que haces?:  ").upper() 
                    if decision_3_1_1 == "AFERRARTE" :
                        print(" Con un esfuerzo sobrehumano, logras sujetar la raíz resbaladiza justo cuando la corriente iba a estrellarte contra las rocas. Consigues salir del agua y descubres que la raíz te lleva a una grieta en el techo. Escalas por ella y llegas a la superficie, en medio de la jungla. Estás magullado y sin tesoros, pero vivo.\n\n¡SOBREVIVISTE POR POCO! Has escapado del templo. FIN.")
                    elif decision_3_1_1 == "SUMERGIRTE" :
                        print("Te sumerges para esquivar el peligro, pero la corriente es demasiado poderosa. Eres arrastrado sin control hacia un remolino subterráneo del que es imposible escapar. La oscuridad te consume.\n\nLA CORRIENTE TE HA VENCIDO. Has perecido en las profundidades. FIN DEL JUEGO.")
                    else :
                        print("elige una opcion valida")
                else :
                    print("elige una opcion valida")
            elif decision_3 == "COSNTRUIR" :
                print("Tu balsa flota bien, pero pronto llegas a unos rápidos peligrosos llenos de rocas afiladas.") 
                decision_3_1_1_2 = input("\nMANIOBRAR.\nAFERRATE\n.¿Que haces?: ").upper() 
                if decision_3_1_1_2 == "MANIOBRAR" :
                    print("Con gran habilidad, logras pasar los rápidos y llegas a una pequeña playa dentro de la cueva. Un antiguo túnel ceremonial te conduce fuera del templo.\n\n¡SOBREVIVISTE A LOS RÁPIDOS! Has encontrado una salida segura. FIN.")
                elif decision_3_1_1_2 == "AFERRARTE" :
                    print("eligues aferrarte,la corriente es demasiado fuerte,caes al agua y mueres.\n'n FIN DEL JUEGO")
                else : 
                    print("eligue una opvion valida") 
            elif decision_3 == "AVANZAR" :
                print("por la orilla: El camino es estrecho y resbaladizo. Llegas a una enorme telaraña que bloquea el paso, tejida por arañas gigantes.") 
                decision_3_1_1_2_2 = input("\nQUEMAR telarañas. \nCORTAR telarañas. \n¿Que eliges?: ").upper()  
                if decision_3_1_1_2_2 == "QUEMAR" : 
                    print("El fuego ahuyenta a las arañas y revela un mapa grabado en la pared. Siguiéndolo, evitas las trampas y encuentras una armería llena de armas antiguas de incalculable valor.\n\nHAS DESCUBIERTO UNA RELIQUIA! Tu audacia te ha recompensado. FIN.")   
                elif decision_3_1_1_2_2 == "CORTAR" :
                    print("cortas la telaraña he intentas avanzar, pero una araña te atrapa, y te vuelves su cena.\n\nFIN DEL JUEGO") 
                else : 
                    print("eligue una opcion valida")
            else : 
                print("eligue una opcion valida")                 
        elif decision_1_1_2 == "ESCONDERSE" : 
            print("te olcultas tras unos helechos gigantes.Segundos despues, una enorme pantera negra aparece, olfateando justo donde estabas. se detiene frente a la puerta sellada ") 
            decision3_3 = input("PERMANECER INMOVIL.\nLANZAR UN PIEDRA.\n¿que haras?: ").upper()
            if decision3_3 == "INMOVIL" : 
                print("la pantera no te detecta.Despues de unos momentos de frustracion al no encontrar presas, se aleja y se pierde en la espesura, el area esta despejada. ") 
                decision3_3_1 = input("INVESTIGAR el lugar.\nINTENTAR forzar la puerta principal.\n ¿que eliges") 
                if decision3_3_1 == "INVESTIGAR" : 
                    print("En el suelo semioculto por el musgo, en cuentras unas marcas extrañas al rededor de la losa que no parecen naturales.Al empujarla.,revelas una trampilla,de madera con un anillo de hierro.\n\n¡HAS ENCONTRADO UNA ENTRADA SECRETA!.")
 
                elif decision3_3_1 == "INTENTAR" or decision3_3_1 == "2":
                  print("La puerta está sellada mágicamente. Pierdes demasiado tiempo y la pantera regresa.\n\nFIN DEL JUEGO")
                else:
                   print("Elige una opción válida.")
            elif decision3_3 == "LANZAR" or decision3_3 == "2":
                print("La pantera corre hacia el sonido. Es tu oportunidad.")
                decision3_3_2 = input("1. APROVECHAR para rodear el templo.\n2. EXAMINAR la puerta mientras no está.\n¿Qué eliges?: ").upper()
                if decision3_3_2 == "APROVECHAR" or decision3_3_2 == "1":
                    print("Te mueves rápido y encuentras la entrada a un río subterráneo.\n\n¡HAS ENCONTRADO UN CAMINO ALTERNATIVO! La aventura continúa.")
                elif decision3_3_2 == "EXAMINAR" or decision3_3_2 == "2":
                    print("La puerta no cede. La pantera es más rápida de lo que pensabas y regresa.\n\nFIN DEL JUEGO")
                else:
                    print("Elige una opción válida.")
            else:
               print("Elige una opción válida.")
        else:
          print("Elige una opción válida.")
    elif decision_1_1 == "CORRER" or decision_1_1 == "2":
        print("\n\nCorres esquivando los pinchos y te adentras en un gran salón con dos caminos.")
        decision_1_1_3 = input("1. Un PUENTE de cuerda inestable a la izquierda.\n2. Unas ESCALERAS oscuras a la derecha.\n¿Qué camino tomas?: ").upper()
        if decision_1_1_3 == "PUENTE" or decision_1_1_3 == "1":
            print("A mitad del puente, te atacan unos murciélagos gigantes. El puente se balancea.")
            decision_puente = input("1. AGITAR los brazos para espantarlos.\n2. CORRER hacia el otro lado.\n¿Qué haces?: ").upper()
            if decision_puente == "AGITAR" or decision_puente == "1":
                print("Ahuyentas a los murciélagos, pero el puente se rompe. Quedas colgando de una soga.")
                decision_soga = input("1. TREPAR con tus últimas fuerzas.\n2. BALANCEARTE para llegar al otro lado.\n¿Qué haces?: ").upper()
                if decision_soga == "TREPAR" or decision_soga == "1":
                  print("Llegas al otro lado justo a tiempo y encuentras un cofre.\n\n¡HAS CONQUISTADO EL ABISMO Y ENCONTRADO EL TESORO!")
                else:
                  print("La soga se rompe y caes al abismo.\n\nFIN DEL JUEGO")
            else:
                print("Los murciélagos te hacen perder el equilibrio y caes.\n\nFIN DEL JUEGO")
        elif decision_1_1_3 == "ESCALERAS" or decision_1_1_3 == "2":
            print("Bajas a una cámara inundada. En el centro hay una palanca.")
            decision_agua = input("1. NADAR hacia la palanca.\n2. AVANZAR lento hacia una puerta al fondo.\n¿Qué haces?: ").upper()
            if decision_agua == "NADAR" or decision_agua == "1":
                print("Al tirar de la palanca, el agua baja pero dos gólems de piedra se activan.")
                decision_golem = input("1. SALTAR a un pasadizo secreto que se abrió a tus pies.\n2. ENFRENTAR a los gólems.\n¿Qué haces?: ").upper()
                if decision_golem == "SALTAR" or decision_golem == "1":
                    print("Caes por un túnel que te lleva fuera de la montaña.\n\n¡HAS LOGRADO ESCAPAR CON VIDA!")
                else :
                    print("\nPresionas los botones en el orden incorrecto. Del cuenco de la estatua sale un dardo envenenado que te alcanza en el cuello. Caes al suelo, paralizado.\n\nUNA MALA DECISIÓN TE HA COSTADO LA VIDA. FIN DEL JUEGO.")
            else : 
                print("\nDecides que la estatua no es importante y continúas tu búsqueda. Das un mal paso en el suelo blando y caes en un foso con estacas afiladas que estaba oculto por la maleza.\n\nLA IMPACIENCIA ES TU PEOR ENEMIGO. FIN DEL JUEGO.")    
        else :
            print("elige una opcion valida")
    else :
        print("elige una opcion valida")            
        
elif decision_1 == "INVESTIGAR" or decision_1 == "2":
    print("\nDecides ser cauteloso y examinas los alrededores de la entrada. Notas que la vegetación es extrañamente densa a la izquierda del templo, como si ocultara algo. A la derecha, escuchas el leve sonido de agua corriente.") 
    decision_4 = input("\nIZQUIERDA o DERECHA: ") .upper()
    if decision_4 == "IZQUIERDA": 
        print("\nTe abres paso a través de las lianas y hojas gigantes. Descubres una estatua de un mono de piedra casi completamente cubierta de musgo. Sus ojos parecen huecos y uno de sus brazos extendidos sostiene un cuenco vacío.")
        decision_4_1 = input("¿Qué haces?:\n. LIMPIAR la estatua para examinarla mejor.\n. IGNORAR la estatua y seguir buscando.\nElige una opción: ") .upper()
        if decision_4_1 == "LIMPIAR": 
            print("\nAl quitar el musgo, revelas una inscripción en la base: 'El sabio ve, oye y calla'. Te das cuenta de que la boca, los ojos y los oídos de la estatua son en realidad botones que se pueden presionar.")
            decision_4_1_1 = input("Recuerdas la frase. ¿En qué orden presionas los botones?:\n OJOS, OÍDOS, BOCA.\n BOCA, OJOS, OÍDOS.\nElige una opción: ").upper()
            if decision_4_1_1 == "OJOS, OIDOS, BOCA" : 
                print("\nPresionas los símbolos en el orden correcto. Escuchas un ruido sordo y la estatua se desliza hacia un lado, revelando una escalera de caracol que desciende a la oscuridad.\n\n¡HAS DESCUBIERTO UNA ENTRADA SECRETA! Tu sabiduría te ha abierto el camino.")
            elif decision_4_1_1 == "BOCA, OJOS, OIDOS":
                print("activas una trampa y queda encerrado.\n\nHAS PERDIDO") 
        elif decision_4_1 == "IGNORAR":
            print("decides ignorar la estatua y continuas tu camino pero caes en una trampa .\n\nMUERES ATRAPADO")
        else :
            print("elige una opcion valida")
    elif decision_4 == "DERECHA" :
        print("\nDecides seguir por el camino de la derecha que va a un sendero que te lleva lejos de la jungla.\nHAS ESCAPADO DE LA JUNGLA")  
    else :
        print("elige una opcion valida")
else :
    print("elige una opcion valida")                                   
                
            
           
        
                
            
    
         