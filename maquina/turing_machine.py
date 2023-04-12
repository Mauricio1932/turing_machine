from transiciones import transicion

cinta_salida = ['_','_']
cinta_lectura = ['_','_']


bandera = True
posicion_estado = 'q0'
cabezal = 0
cabezal_salida = 0
particion = []
simbolo = ''
lin = ""
valor_s = []


def inicio():
    global cinta_lec, cinta_salida, cabezal, cabezal_salida, posicion_estado, cinta_lectura
    
    
    cinta_lectura = ['_']
    cinta_salida = ['_']
    posicion_estado = 'q0'
    cabezal = 0
    cabezal_salida = 0

    cinta_lec = input("ingrese su conjunto: ")
    
    cinta_lec = cinta_lec.replace(" ", "_")
    
    for i in range(len(cinta_lec)):
        cinta_lectura.append(cinta_lec[i])
    cinta_lectura.append('_')
    cinta_lectura.append('_')
    
    machine_parttion(cinta_lectura)


def machine_parttion(content):
    global posicion_estado, cabezal, cinta_salida, simbolo, bandera, cabezal_salida, lin
    
    while posicion_estado != 'q5':
        # obtenemos simbolo inicial de nuestra cinta de lectura
        simbolo_actual = cinta_lectura[cabezal]
        
        # obtenemos simbolo inicial de nuestra cinta de salida
        simbolo_actual_salida = cinta_salida[cabezal_salida]

        # obtenemos la trancision a realizar
        transition = transicion(posicion_estado,simbolo_actual,simbolo_actual_salida)
        
        print(transition)
        
        
        # Si no existe trancicion, la maquina se termina
        if transition is None:
            break

        # obtener valor para escribir en la cinta de salida
        valor = transition[2]
        cinta_salida[cabezal_salida] = valor

        # mover las cintas
        # Mover el cabezal DERECHA
        if transition[3] == 'R':
            cabezal += 1
            if cabezal == len(cinta_lec):
                cinta_lectura.append('_')
        # Mover cabezal IZQUIERDA
        elif transition[3] == 'L':
            cabezal -= 1
            # if cabezal < 0:
            #     cinta_lec.insert(0, '_')

        # Mover el cabezal DERECHA de la cinta de salida
        if transition[4] == 'R':
            cabezal_salida += 1
            if cabezal_salida == len(cinta_salida):
                cinta_salida.append('_')
        # Mover cabezal IZQUIERDA
        elif transition[4] == 'L':
            cabezal_salida -= 1
            # if cabezal < 0:
            #     cinta_lec.insert(0, '_')

        posicion_estado = transition[0]
        
        print(cinta_lectura, "cita lectura")
        print (cinta_salida, "cinta salida")
    print (cinta_salida, "cinta salida")


inicio()