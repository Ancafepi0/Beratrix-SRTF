from typing import List
#---------------------------------------------FUNCIONES PRINCIPALES DEL MENU---------------------------------------------
#FUNCION UTILIZADA PARA OBTENER Y VERIFICAR EL NUMERO DE PROCESOS A EJECUTAR
def obtener_numero_procesos ():
    #AQUI SE PIDE EL NUMERO DE PROCESOS A EJECUTAR SIN VERIFICAR
    respuesta =  input ("Por favor digite el numero de procesos a ejecutar"+"\n"+"MINIMO 6, MAXIMO 8"+ "\n")
    #METODO VERIFICAR
    while (True):
        try:
            numero_procesos = int(respuesta)
            while (int(numero_procesos) < 6 or int(numero_procesos) > 8):
                numero_procesos = input ("RESPUESTA INVALIDA"+"\n"+"Por favor digite nuevamente el numero de procesos a ejecutar"+"\n"+"MINIMO 6, MAXIMO 8"+ "\n")
            break
        except ValueError:
            respuesta =  input ("RESPUESTA NO VALIDA"+"\n"+"Por favor digite nuevamente el numero de procesos a ejecutar"+"\n"+"MINIMO 6, MAXIMO 8"+ "\n")
    #AQUI SE RETORNA EL NUMERO DE PROCESOS TRAS VERIFICARLOS
    return numero_procesos
#FUNCION UTILIZADA PARA CREAR LOS PROCESOS SI EL USUARIO DESEA AGREGARLE UN NOMBRE
def creacion_nombre():
    #AQUI SE DECLARA EL ARRAY PROCESO
    proceso=[None,0,0,0,0]
    #AQUI SE DECLARA Y SE PIDE EL NOMBRE
    nombre = input ("Por favor digite el nombre del proceso")
    #AQUI SE DECLARA Y SE PIDE TIEMPO DE LLEGADA
    tiempo_llegada_respuesta = input ("Por favor digite el tiempo de llegada del proceso:  ")
    #METODO VERIFICAR
    while (True):
        try:
            tiempo_llegada = int(tiempo_llegada_respuesta)
            while (int(tiempo_llegada) < 0):
                tiempo_llegada = input ("RESPUESTA INVALIDA"+"\n"+"Por favor digite nuevamente el tiempo de llegada del proceso"+ "\n")
            break
        except ValueError:
            tiempo_llegada_respuesta =  input ("RESPUESTA NO VALIDA"+"\n"+"Por favor digite  nuevamente el tiempo de llegada del proceso"+ "\n")
    #AQUI SE PIDE EL NUMERO DE RAFAGA
    numero_rafaga = obtener_rafaga()
    #AQUI SE AGREGAN LOS VALORES A LA LISTA LLAMADA PROCESO 1. POSICION EL NOMBRE 2. POSICIN TIEMPO LLEGADA 3. POSICION NUMERO DE RAFAGA 
    #4. TIEMPO DE ESPERA QUE AUN NO SE AGREGA Y 5. POSICION TIEMPO_TERMINACION QUE AUN NO SE AGREGA
    proceso [0]= nombre
    proceso [1]= tiempo_llegada
    proceso [2]= numero_rafaga
    #AQUI SE HACE EL RETURN DEL PROCESO TRAS HABERLO LLENADO
    return proceso

#FUNION UTILIZADA PARA CREAR LOS PROCESOS SI EL USUARIO NO QUIERE AGREGARLE EL NOMBRE
def creacion_sin_nombre(numero):
    proceso=[None,0,0,0,0]
    #AQUI SE DECLARA Y SE Asigna un nombre
    nombre = ("Proceso " + str(numero))
    #AQUI SE DECLARA Y SE PIDE TIEMPO DE LLEGADA
    tiempo_llegada_respuesta = input ("Por favor digite el tiempo de llegada del proceso:  ")
    #METODO VERIFICAR
    while (True):
        try:
            tiempo_llegada = int(tiempo_llegada_respuesta)
            while (int(tiempo_llegada) < 0):
                tiempo_llegada = input ("RESPUESTA INVALIDA"+"\n"+"Por favor digite nuevamente el tiempo de llegada del proceso"+ "\n")
            break
        except ValueError:
            tiempo_llegada_respuesta =  input ("RESPUESTA NO VALIDA"+"\n"+"Por favor digite  nuevamente el tiempo de llegada del proceso"+ "\n")
    #AQUI SE PIDE EL NUMERO DE RAFAGA
    numero_rafaga = obtener_rafaga()
    #AQUI SE AGREGAN LOS VALORES A LA LISTA LLAMADA PROCESO 1. POSICION EL NOMBRE 2. POSICIN TIEMPO LLEGADA 3. POSICION NUMERO DE RAFAGA 
    #4. TIEMPO DE ESPERA QUE AUN NO SE AGREGA Y 5. POSICION TIEMPO_TERMINACION QUE AUN NO SE AGREGA
    proceso [0]= nombre
    proceso [1]= tiempo_llegada
    proceso [2]= numero_rafaga
    #AQUI SE HACE EL RETURN DEL PROCESO TRAS HABERLO LLENADO
    return proceso#FUNCION UTILIZADA PARA OBTENER EL NUMERO DE RAFAGAS DEL PROCESO
def obtener_rafaga():
    #AQUI SE PIDE EL  NUMERO DE RAGAS UTILIZADAS EN EL PROCESO SIN VERIFICAR
    respuesta = input ("Digite el numero de rafagas que utiliza el proceso: ")
    #METODO VERIFICAR
    while (True):
        try:
            numero_rafaga = int(respuesta)
            while (int(numero_rafaga) < 1 or int(numero_rafaga) > 12):
                numero_rafaga = input ("RESPUESTA INVALIDA"+"\n"+"Por favor digite nuevamente el numero de rafagas a utilizar"+"\n"+"MINIMO 1, MAXIMO 12"+ "\n")
            break
        except ValueError:
            respuesta =  input ("RESPUESTA NO VALIDA"+"\n"+"Por favor digite  nuevamente el numero de rafagas a utilizar en el proceso"+"\n"+"MINIMO 1, MAXIMO 12"+ "\n")
    #AQUI SE RETORNA EL NUMERO DE RAFAGAS YA VERIFICADAS
    return numero_rafaga
#---------------------------------------------IMPLEMENTACION DEL MENU---------------------------------------------
def menu ():
    #SE IMPORTA LIBRERIA LIST PARA PODER QUE LISTA_PROCESOS SE VUELVA UNA LISTA DE LISTAS
    lista_procesos: List[List] = []  
    #SALUDO DE PROYECTO BERATRIX
    print (" BIENVENIDO A BERATRIX "+"\n"+ " Aplicacion para la simulacion \n de sistemas de planificacion \n STRF ")
    #DECLARACION DE NUMERO DE REPETICIONES
    numero_repeticiones = obtener_numero_procesos()
    #SOLICITUD PARA SABER QUE METODO IMPLEMENTA RPARA CREAR PROCESO (CON O SIN NOMBRE)
    respuesta = input (" ¿Desea crear los procesos con un nombre especifico o desa que se generen automaticamente? " +"\n"
                + "\n DIGITE 1 PARA ASIGNAR NOMBRES"
                + "\n DIIGITE 2 PARA ASIGNAR GENERAR DE FORMA AUTOMATICA \n")
    #METODO PARA VERIFICAR LA RESPUESTA DL USUARIO
    while (True):
        try:
            respuesta_usuario = int(respuesta)
            while (int(respuesta_usuario) < 1 or int(respuesta_usuario) > 2):
                respuesta_usuario = input ("RESPUESTA INVALIDA"+"\n"+"Por favor digite nuevamente el numero de rafagas a utilizar"+"\n"+"MINIMO 1, MAXIMO 12"+ "\n")
            break
        except ValueError:
            respuesta =  input ("RESPUESTA NO VALIDA"+"\n"+"Por favor digite  nuevamente el numero de rafagas a utilizar en el proceso"+"\n"+"MINIMO 1, MAXIMO 12"+ "\n")
    #CODICIONAL PARA IMPLEMENTAR EL METODO SEGUN LA RESPUESTA DEL USUARIO
    if (respuesta_usuario==1):
        for i in range(numero_repeticiones):
            obj_proceso = creacion_nombre ()
            lista_procesos.append(obj_proceso)
    else:
        for i in range(numero_repeticiones):
            obj_proceso = creacion_sin_nombre (i+1)
            lista_procesos.append(obj_proceso)
    #RETORNO DE LA LISTA DE PROCESOS CREADA
    return lista_procesos
#---------------------------------------------IMPLEMENTACION DEL STRF---------------------------------------------
#FUNCION QUE EJECUTA EL STRF 
def strf ():
    #LISTA CREADA USUARIO LLAMA A MENU PARA OBTENER LA LISA CREADA POR EL USUARIO
    lista_creada_usuario = menu()
    #LISTA ORDENADA ORDENA LA LISTA CREADA POR EL USUARIO DE MENOR A MAYOR UTILIZANDO PRIMERO EL PRIMER ARGUMENTO Y LUEGO EL SEGUNDO
    lista_ordenada = sorted(lista_creada_usuario, key=lambda x: (x[1], x[2]))
    strf_ciclo (lista_ordenada)

#FUNCION QUE EJECUTA EL CICLO STRF
def strf_ciclo(lista_ordenada): 
    proceso_en_ejecucion = [[None,0,0,0,0]] 
    lista_espera: List[List] = []
    #LISTA CON PROCESOS EN ESPERA CANDIDATOS EN PROCESOS QUE SEAN DE MENOR RAFAGAS
    lista_candidatos_espera: List[List] = []
    #LISTA CON PROCESOS EN ESPERA CANDIDATOS EN PROCESOS CON IGUAL NUMERO DE RAFAGAS
    lista_candidatos_igual: List [List] = []
    #CONTADOR ES UNA VARIABLES QUE INDICA CUANTOS CICLOS SE HAN EJECUTADO
    contador=0
    #LISTA QUE GUARDA LOS PROCESOS ENCONTRADOS
    procesos_encontrados: List[List] = []   
    #-----------------------------------------------PROCESOS DE BUSQUEDA-----------------------------------------------
    #1
    #CICLO QUE BUSCA PROCESOS QUE COINCIDA SU TIEMPO DE INICIO CON EL TIEMPO DEL CONTADOR
    for proceso_coincidir in lista_ordenada:
        if proceso_coincidir[1] == contador:
            procesos_encontrados.append(proceso_coincidir)
    #CONDICIONALES QUE DECIDEN QUE PROCESO ES CANDIDATO A EJECUTARSE
    #1.1 SI HAY MAS DE UN PROCESOS QUE PUEDE SER CANDIDATO OSEA QUE LLEGA AL MISMO TIEMPO
    if (len(procesos_encontrados)>1):
        listas_ordenadas_rafagas = sorted(procesos_encontrados, key=lambda x:x[2])
        candidato = listas_ordenadas_rafagas[0]
    #UTILIZAMOS EL SLICING PARA QUE EL FOR EMPIECE DESPUES DEL PRIMERO PUES SERAN LOS PROCESOS QUE IRAN A LISTA DE ESPERA
    # El slicing te permite seleccionar un rango específico de elementos en una lista. 
        for enviar_a_espera in listas_ordenadas_rafagas[1:]:
            lista_espera.append(enviar_a_espera)
    #1.2 SI SOLO HAY UN PROCESO CANDIDATO
    elif (len(procesos_encontrados)==1):
        candidato= procesos_encontrados [0]
    #1.3 SI NO HAY NINGUNO PROCESO CANDIDATO
    else:
        candidato= [[None,0,0,0,0]]
    #2
    #Ciclo que compara de rafaga necesitadas con el del procesos candidato
    #2.1 ACCION SI HAY UN PROCESO CANDIDATO Y UN PROCESO EN EJECUCION
    
    if (candidato[0][0] != None and proceso_en_ejecucion[0][0] != None):
        #AQUI SE COMPARA LA RAFAGA DE LOS DOS PROCESOS PARA SABER CUAL ES MENOR
        valor_candidato= candidato[2]
        valor_proceso_ejecucion = proceso_en_ejecucion [0][2]
        #ACCION SI EL NUMERO DE RAFAGAS DEL PROCESO EN EJECUCION ES MENOR QUE EL DE CANDIDATO
        if (valor_proceso_ejecucion < valor_candidato):
            lista_espera.append(candidato)
            candidato=proceso_en_ejecucion

        #ACCION SI EL NUMERO DE RAFAGAS ES IGUAL EN LOS PROCESO
        elif (valor_candidato==valor_proceso_ejecucion):
            lista_espera.append(candidato)
            candidato= proceso_en_ejecucion


        #ACCION SI EL PROCESO CANDIDATO TIENE MENOR RAFAGAS QUE EL PROCESO EN EJECUCION
        else:
            lista_espera.append(proceso_en_ejecucion)
            candidato = candidato
    #2.2 SI HAY PROCESO CANDIDATO Y NO HAY PROCESO EN EJECUCION
    if (candidato[0][0] != None and proceso_en_ejecucion[0][0] == None):
        candidato = candidato
    #2.3 SI NO HAY PROCESO CANDIDATO Y SI HAY PROCESO EN EJECUCION
    if (candidato[0][0] == None and proceso_en_ejecucion[0][0] != None):
        candidato = proceso_en_ejecucion
    #2.4 SI NO HAY CANDIDADTO Y NO HAY PROCESO EN EJECUCION
    if (candidato[0][0] == None and proceso_en_ejecucion[0][0] == None):
        candidato = candidato
    #3 BUSQUEDA EN LA LISTA DE ESPERA BUSCANDO CANDIDATO CON MENOS RAFAGAS
    #3.1 SI HAY UN PROCESO CANDIDATO BUSCARA EN LA LISTA PROCESOS QUE TENGAN MENOR RAFAGAS QUE EL
    if (candidato[0][0] != None):
        valor_rafaga_candidato = candidato [2]
        #BUSQUEDA EN LA LISTA DE ESPERA UN PROCESO CON MENOS RAFAGAS QUE EL CANDIDATO
        for proceso_espera in lista_espera:
            if (proceso_espera[2] < valor_rafaga_candidato):
                lista_candidatos_espera.append(proceso_espera)
        #SI EN LA LISTA CANDIDATOS DE ESPERA HAY MAS DE UNO SE TOMA EL QUE LLEGO PRIMERO
        if (len(lista_candidatos_espera) > 1):
            lista_ordena_candidatos_espera = sorted(lista_candidatos_espera, key=lambda x:(x[1], x[2]))
            proceso_a_ejecutar = lista_ordena_candidatos_espera[0]
            lista_espera.append(candidato)
            candidato = proceso_a_ejecutar
            for proceso_eliminar in lista_espera:
                if proceso_eliminar[0] == proceso_a_ejecutar [0]:
                    lista_espera.remove(proceso_a_ejecutar)
                    break
        #SI EN LA LISTA CANDIDATOS DE ESPERA SOLO HAY UNO ENTONCES ESE PROCESO SE TOMA COMO CANDIDATO
        elif (len(lista_candidatos_espera)== 1):
            proceso_a_ejecutar = lista_candidatos_espera
            lista_espera.append(candidato)
            candidato = proceso_a_ejecutar
            lista_espera.remove(proceso_a_ejecutar[0])
     
        #SI EN LA LISTA CANDIDATOS DE ESPERA NO HAY NINGUN PROCESO CON MENOR RAFAGAS ENTONCES CANDIDATO SE MANTIENE IGUAL
        else:
            candidato = candidato
    #3.2 SI HAY CANDIDATO SE BUSCA UN PROCESO CON IGUAL CANTIDAD DE RAFAGAS
        if (candidato[0][0] !=  None):
            refagas_candidato= candidato[2]
            for proceso_igual_espera in lista_espera:
                if (proceso_igual_espera[2] == refagas_candidato):
                    lista_candidatos_igual.append(proceso_igual_espera)
                print ("Funcione")
            if (len(lista_candidatos_igual) > 1):
                lista_ordena_candidatos_espera = sorted(lista_candidatos_igual, key=lambda x:(x[1], x[2]))
                proceso_a_ejecutar = lista_ordena_candidatos_espera[0]
                lista_espera.append(candidato)
                candidato = proceso_a_ejecutar
                for proceso_eliminar in lista_espera:
                    if proceso_eliminar[0] == proceso_a_ejecutar [0]:
                        lista_espera.remove(proceso_a_ejecutar)
                        break

            #SI EN LA LISTA CANDIDATOS DE ESPERA SOLO HAY UNO ENTONCES ESE PROCESO SE TOMA COMO CANDIDATO
            elif (len(lista_candidatos_igual)== 1):
                proceso_a_ejecutar = lista_candidatos_igual
                lista_espera.append(candidato)
                candidato = proceso_a_ejecutar
                lista_espera.remove(proceso_a_ejecutar[0])

            #SI EN LA LISTA CANDIDATOS DE ESPERA NO HAY NINGUN PROCESO CON MENOR RAFAGAS ENTONCES CANDIDATO SE MANTIENE IGUAL
            else:
                candidato = candidato
strf ()