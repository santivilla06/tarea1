print("--------BIENVENIDO A ELSECRETO DEL TEMPLO OLVIDADO--------\n")
print("Introduccion:\n")
print("Te encuentras en la entrada de un antiguo y misterioso templo en medio de la jungla amazónica, un lugar que los mapas no muestran y del que solo hablan las leyendas. Has buscado este lugar durante años, siguiendo los rastros de un explorador perdido que hablaba de un tesoro invaluable en su interior. Una pesada puerta de piedra, cubierta de enredaderas, bloquea tu paso. A un lado, hay una pequeña abertura en la pared, lo suficientemente grande como para que una persona se deslice.\n")

print("La jungla a tus espaldas parece oscurecerse y los sonidos de criaturas desconocidas se hacen más fuertes. Debes tomar una decisión rápida.")

decision_1 = input("Te encuentras en la entrada. ¿Qué harás?:\n1.EMPUJAR la pesada puerta de piedra.\n2.DESLIZARTE por la abertura.\n3.INVESTIGAR los alrededores en busca de otra entrada.\n¿Elige una opcion: ").upper()
if decision_1 == "EMPUJAR" or decision_1 == "1" :
    print("Con un esfuerzo sobrehumano, logras mover la puerta. Al entrar, escuchas un clic bajo tu pie. ¡Una trampa! Unos pinchos caen del techo justo delante de ti. ¿Qué haces?\n")
    decision_1_1 = input("1.SALTAR hacia atrás para salir del templo.\n2.CORRER hacia adelante para esquivar la trampa.\nElige una opcion: ").upper()
    if decision_1_1 == "SALTAR" or decision_1_1 == "1":
        print("\n\nSaltas hacia atrás justo a tiempo. Los pinchos se estrellan contra el suelo y el estruendo provoca que la pesada puerta de piedra se cierre con un golpe sordo, sellando la entrada principal. Estás fuera, pero tu camino original ha desaparecido.\nEl ruido de la trampa ha despertado a la jungla.Escuchas el rujido de de ramas y un gruñido bajo muy cerca.Debes actuar ya.\nEl reuido de la trampra a despertado a la jungla.Escuchas el crujido de ramas y un gruñido bajo muy cerca.Debes actuar ya \n") 
        decision_1_1_2 = input("¿Que haces?\n1.DESLIZARTE por pequeña abertura lateral.\n2.RODEAR el templo en busca de una entrada trasera.\n3.ESCONDERTE entre la densa melaza  y esperar a que pase el peligro.").upper() 
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
                    print("el liquido pateado fluye suavemente por el canal. Escuchas un chasquido y una seccion de la pared se desliza, revelando un pequeño cofre con monedas de plata antiguas y un mapa que muestra la salida segura de la jungla.\n\N¡HAS ENCONTRADO UN TESORO Y ESCAPADO!\N\N FIN") 
                else : 
                    print("eligue una opcion valida")  
                
                
            
    
         