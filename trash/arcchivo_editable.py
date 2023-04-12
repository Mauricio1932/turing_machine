

cinta_lectura = ''
cinta_salida = []




posicion_estado = 'q0'
cabezal = 0
particion = []
simbolo = ''


def machine_parttion():
    global posicion_estado, cabezal, cinta_salida, simbolo, bandera

    while posicion_estado != 'q224':
        
        # obtenemos simbolo inicial de nuestro conjunto
        simbolo_actual = cinta_lectura[cabezal]
        
        # obtenemos la trancision que se va realizar
        
        transition = tabla_transicion.get((posicion_estado, simbolo_actual))

        # Si no existe trancicion, la maquina se termina
        if transition is None:
            break

        # obtener valor para escribir en la cinta de salida
        valor = transition[1]
        cinta_salida.append(valor)

        # Mover el cabezal DERECHA
        if transition[2] == 'R':
            cabezal += 1
            if cabezal == len(cinta_lectura):
                cinta_lectura.append('_')
        # Mover cabezal IZQUIERDA
        elif transition[2] == 'L':
            cabezal -= 1
            # if cabezal < 0:
            #     cinta_lectura.insert(0, '_')

        posicion_estado = transition[0]

        # print(cinta_salida)
        # print(simbolo_actual, posicion_estado)
        # print(transition)

    parseo = str(cinta_salida)
    lin = parseo
    lin = lin.replace("[", "")
    lin = lin.replace("]", "")
    lin = lin.replace("'", "")
    lin = lin.replace(",", "")
    lin = lin.replace("-", ",")
    lin = lin.replace(" ", "")

    # print(simbolo_actual, cabezal)
    # print("Transicion", transition, "  simbolo actual", simbolo_actual)
    # print(cinta_lectura)
    print(lin)

    if posicion_estado == 'q5 ':
        # Reconstruir la partición a partir de la cinta final
        parseo = str(cinta_salida)
        lin = parseo
        lin = lin.replace("[", "")
        lin = lin.replace("]", "")
        lin = lin.replace("'", "")
        lin = lin.replace(",", "")
        lin = lin.replace("-", ",")
        lin = lin.replace(" ", "")

        print(lin)


machine_parttion()
