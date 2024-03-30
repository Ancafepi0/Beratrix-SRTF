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
    if (len(procesos_encontrados)>1):
        listas_ordenadas_rafagas = sorted(procesos_encontrados, key=lambda x:x[2])
        candidato = listas_ordenadas_rafagas[0]
            
                
strf ()