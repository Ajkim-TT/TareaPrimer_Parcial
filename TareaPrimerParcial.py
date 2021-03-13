import os 
#import sys
from io import open
import psycopg2
import time
ruta = 'TareaPrimerParcial.txt'
textfile = open(ruta,'a+')
textfile.write('Tarea Primer Parcial')
conexion1 = psycopg2.connect("dbname=PrimerParcial user=postgres password=ajkimtepaz")
cursor1=conexion1.cursor()
while 1:
    try:
        print('\n______________________')
        print('Seleccione un programa\n')
        print('1.COMPARACIÓN DE 3 NUMEROS\n2.DIVISORES DE UN NUMERO\n3.CONTADOR DE VOCALES\n4.SUMA DESDE 0 HASTA UN NUMERO')
        print('5.LISTA DE NUMEROS DE 2 EN 2\n6.LISTA DE NUMEROS DEL MAYOR AL MENOR\n7.BUSCADOR DE CADA VOCAL\n8.NUMEROS IMPARES DEL 1 AL 100')
        print('9.TRES LADOS DEL TRIANGULO\n10.FACTORIAL DE NUMERO DIVISIBLE ENTRE 7\n11.CALCULAR AREA DE FIGURAS GEOMÉTRICAS')
        print('12.PROMEDIO DE NOTAS\n13.DETERMINAR SI EL AÑO FUE BICIESTO\nOtro - Salir')
        programa = input()
        programa = int(programa)
        if programa == 1:
            flag = 1
            while flag:
                print('\nCOMPARACIÓN DE 3 NUMEROS')
                textfile.write('\nCOMPARACION DE 3 NUMEROS')
                sql="insert into comparar_tres(primer_numero, segundo_numero, tercer_numero, comparacion, resultado) values (%s,%s,%s,%s,%s)"
                try:
                    print('Ingrese el primer número')
                    primer_numero = input()
                    primer_numero = float(primer_numero)
                    print('Ingrese el segundo número')
                    segundo_numero = input()
                    tercer_numero = float(tercer_numero)
                    print('Ingrese el tercer número')
                    tercer_numero = input()
                    segundo_numero = float(segundo_numero)
                    
                    if (primer_numero>segundo_numero) and (primer_numero>tercer_numero) and segundo_numero != tercer_numero:
                        primero_mayor = primer_numero+segundo_numero+tercer_numero
                        print('El primer numero es el mayor, la suma de los 3 es '+str(primero_mayor))
                        textfile.write('\nEl primer numero es el mayor, la suma de los 3 es '+str(primero_mayor))
                        datos=(str(primer_numero),str(segundo_numero),str(tercer_numero),'Primero Mayor',str(primero_mayor))
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    elif (segundo_numero>primer_numero) and (segundo_numero>tercer_numero) and primer_numero != tercer_numero:
                        segundo_mayor = primer_numero*segundo_numero*tercer_numero
                        print('El segundo numero es el mayor, la multiplicación de los 3 es '+str(segundo_mayor))
                        textfile.write('\nEl segundo numero es el mayor, la multiplicación de los 3 es '+str(segundo_mayor))
                        datos=(str(primer_numero),str(segundo_numero),str(tercer_numero),'Segundo Mayor',str(segundo_mayor))
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    elif (tercer_numero>primer_numero) and (tercer_numero>segundo_numero) and primer_numero != segundo_numero:
                        primer_numero=primer_numero//1
                        primer_numero=int(primer_numero)
                        segundo_numero=segundo_numero//1
                        segundo_numero=int(segundo_numero)
                        tercer_numero=tercer_numero//1
                        tercer_numero=int(tercer_numero)
                        concatenacion = str(primer_numero)+str(segundo_numero)+str(tercer_numero)
                        print('El tercer numero es el mayor, la concatenacion de los 3 es '+concatenacion)
                        textfile.write('\nEl tercer numero es el mayor, la concatenacion de los 3 es '+concatenacion)
                        datos=(str(primer_numero),str(segundo_numero),str(tercer_numero),'Tercero Mayor',concatenacion)
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    elif primer_numero == segundo_numero and primer_numero != tercer_numero:
                        print('El numero diferente es el tercero y es '+str(tercer_numero))
                        textfile.write('\nEl numero diferente es el tercero y es '+str(tercer_numero))
                        datos=(str(primer_numero),str(segundo_numero),str(tercer_numero),'Tercero Diferente',str(tercer_numero))
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    elif primer_numero == tercer_numero and primer_numero != segundo_numero:
                        print('El numero diferente es el segundo y es '+str(segundo_numero))
                        textfile.write('\nEl numero diferente es el segundo y es '+str(segundo_numero))
                        datos=(str(primer_numero),str(segundo_numero),str(tercer_numero),'Segundo Diferente',str(segundo_numero))
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    elif tercer_numero == segundo_numero and tercer_numero != primer_numero:
                        print('El numero diferente es el primero y es '+str(primer_numero))
                        textfile.write('\nEl numero diferente es el primero y es '+str(primer_numero))
                        datos=(str(primer_numero),str(segundo_numero),str(tercer_numero),'Primero Diferente',str(primer_numero))
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    else:
                        primer_numero=primer_numero//1
                        primer_numero=int(primer_numero)
                        segundo_numero=segundo_numero//1
                        segundo_numero=int(segundo_numero)
                        tercer_numero=tercer_numero//1
                        tercer_numero=int(tercer_numero)
                        concatenacion = str(primer_numero)+str(segundo_numero)+str(tercer_numero)
                        print(concatenacion+'  los numeros son iguales')
                        textfile.write('\n'+str(primer_numero)+' '+str(segundo_numero)+' '+str(tercer_numero)+' Todos los numeros son iguales')
                        datos=(str(primer_numero),str(segundo_numero),str(tercer_numero),'Todos Iguales','')
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                except:
                    print('\n_____________________ERROR_______________________________')
                    print('Uno o varios de los caracteres ingresados no es un numero')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==2:
            flag = 1
            while flag:
                #system('cls')
                print('DIVISORES DE UN NUMERO')
                textfile.write('\nDIVISORES DE UN NUMERO')
                sql="insert into tabladivisores(numero,divisores) values (%s,%s)"
                try:
                    print('Ingrese un número')
                    numero = input()
                    numero = int(numero)
                    if numero < 0:
                        print('El numero ingresado no debe ser negativo')
                    else:
                        i = 1
                        divisores = ''
                        for i in range(1 , numero+1):
                            residuo = numero % i
                            if residuo == 0:
                                divisores = divisores +' '+ str(i)
                        print('El numero es '+str(numero)+' y sus divisores son '+divisores)
                        textfile.write('\nEl numero es '+str(numero)+' y sus divisores son '+divisores)
                        datos=(str(numero),divisores)
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                except:
                    print('\n_________ERROR_____________')
                    print('El caracter no es un número')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa == 3:
            flag = 1
            while flag:
                print('CONTADOR DE VOCALES')
                textfile.write('\nCONTADOR DE VOCALES')
                sql="insert into cuentavocales(palabra,vocales) values (%s,%s)"
                print('Ingrese una palabra')
                palabra = input()
                palabra = str(palabra)
                voc = 0
                for i in range(0,len(palabra)):
                    if palabra[i]=='a' or palabra[i]=='e' or palabra[i]=='i' or palabra[i]=='o' or palabra[i]=='u':
                        voc=voc+1
                    if palabra[i]=='A' or palabra[i]=='E' or palabra[i]=='I' or palabra[i]=='O' or palabra[i]=='U':
                        voc=voc+1
                print('La cantidad de vocales en la palabra '+palabra+' es '+str(voc))
                textfile.write('\nLa cantidad de vocales en la palabra '+palabra+' es '+str(voc))
                datos=(palabra,str(voc))
                cursor1.execute(sql, datos)
                conexion1.commit()

                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==4:
            flag = 1
            while flag:
                print('SUMA DESDE 0 HASTA UN NUMERO')
                textfile.write('\nSUMA DESDE 0 HASTA UN NUMERO')
                sql="insert into sumahastanumero(numero,suma) values (%s,%s)"
                try:
                    print('Ingrese un numero, el programa lo redondeará al entero más cercano')
                    numero = input()
                    numero = float(numero)
                    numero = numero//1
                    numero = int(numero)
                    suma = 0
                    for i in range(1,numero+1):
                        suma = suma + i
                    print('La sumatoria de los numeros hasta '+str(numero)+' es ' + str(suma))
                    textfile.write('\nLa sumatoria de los numeros hasta '+str(numero)+' es ' + str(suma))
                    datos=(str(numero),str(suma))
                    cursor1.execute(sql, datos)
                    conexion1.commit()
                except:
                    print('\n______________ERROR_________________')
                    print('El caracter ingresado no es un número')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==5:
            flag = 1
            while flag:
                print('LISTA DE NUMEROS DE 2 EN 2')
                textfile.write('\nLISTA DE NUMEROS DE 2 EN 2')
                sql="insert into listadosendos(numero1,numero2,lista) values (%s,%s,%s)"
                try:
                    print('Ingrese dos números enteros')
                    print('Primer Número:')
                    numero1 = input()
                    numero1 = int(numero1)
                    print('Segundo Número:')
                    numero2 = input()
                    numero2 = int(numero2)

                    if numero1>numero2:
                        i=1
                        lista = ' '
                        for i in range(0,1+(numero1-numero2)//2):
                            lista = lista + ' ' + str(numero2 + 2*i)
                        print('La lista de numeros desde '+str(numero2)+' hasta '+str(numero1)+' es '+lista)
                        textfile.write('\nLa lista de numeros desde '+str(numero2)+' hasta '+str(numero1)+' es '+lista)
                        datos=(str(numero1),str(numero2),lista)
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    elif numero1<numero2:
                        i=1
                        lista = ' '
                        for i in range(0,1+(numero2-numero1)//2):
                            lista = lista + ' ' + str(numero1 + 2*i)
                        print('La lista de numeros desde '+str(numero1)+' hasta '+str(numero2)+' es '+lista)
                        textfile.write('\nLa lista de numeros desde '+str(numero1)+' hasta '+str(numero2)+' es '+lista)
                        datos=(str(numero1),str(numero2),lista)
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    else:
                        print('Los números son iguales')
                        textfile.write('\nLos números son iguales')
                        datos=(str(numero1),str(numero2),'Los numeros son iguales')
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                except:
                    print('\n____________ERROR____________')
                    print('Debe ingresar numeros enteros')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==6:
            flag = 1
            while flag:
                print('LISTA DE NUMEROS DEL MAYOR AL MENOR')
                textfile.write('\nLISTA DE NUMEROS DEL MAYOR AL MENOR')
                sql="insert into listamayoramenor(numero1,numero2,lista) values (%s,%s,%s)"
                try:
                    print('Ingrese dos números enteros')
                    print('Primer Número:')
                    numero1 = input()
                    numero1 = int(numero1)
                    print('Segundo Número:')
                    numero2 = input()
                    numero2 = int(numero2)

                    if numero1>numero2:
                        i=1
                        lista = ' '
                        for i in range(0,1+numero1-numero2):
                            lista = lista + ' ' + str(numero1 - i)
                        print('La lista de numeros desde '+str(numero1)+' hasta '+str(numero2)+' es '+lista)
                        textfile.write('\nLa lista de numeros desde '+str(numero1)+' hasta '+str(numero2)+' es '+lista)
                        datos=(str(numero1),str(numero2),lista)
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    elif numero1<numero2:
                        i=1
                        lista = ' '
                        for i in range(0,1+numero2-numero1):
                            lista = lista + ' ' + str(numero2 - i)
                        print('La lista de numeros desde '+str(numero2)+' hasta '+str(numero1)+' es '+lista)
                        textfile.write('\nLa lista de numeros desde '+str(numero2)+' hasta '+str(numero1)+' es '+lista)
                        datos=(str(numero1),str(numero2),lista)
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                    else:
                        print('Los números son iguales')
                        textfile.write('\nLos números son iguales')
                        datos=(str(numero1),str(numero2),'Los numeros son iguales')
                        cursor1.execute(sql, datos)
                        conexion1.commit()
                except:
                    print('\n_____________ERROR___________')
                    print('Debe ingresar numeros enteros')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==7:
            flag = 1
            while flag:
                print('BUSCADOR DE CADA VOCAL')
                textfile.write('\nBUSCADOR DE CADA VOCAL')
                sql="insert into cada_vocal(palabra,vocal_a,vocal_e,vocal_i,vocal_o,vocal_u) values (%s,%s,%s,%s,%s,%s)"
                print('Ingrese una palabra')
                palabra = input()
                palabra = str(palabra)
                vocal_a = 0
                vocal_e = 0
                vocal_i = 0
                vocal_o = 0
                vocal_u = 0
                for i in range(0,len(palabra)):
                    if palabra[i]=='a' or palabra[i]=='A' or palabra[i]=='á' or palabra[i]=='Á':
                        vocal_a=vocal_a+1
                    if palabra[i]=='e' or palabra[i]=='E' or palabra[i]=='é' or palabra[i]=='É':
                        vocal_e=vocal_e+1
                    if palabra[i]=='i' or palabra[i]=='I' or palabra[i]=='í' or palabra[i]=='Í':
                        vocal_i=vocal_i+1
                    if palabra[i]=='o' or palabra[i]=='O' or palabra[i]=='ó' or palabra[i]=='Ó':
                        vocal_o=vocal_o+1
                    if palabra[i]=='u' or palabra[i]=='U' or palabra[i]=='ú' or palabra[i]=='Ú' or palabra[i]=='ü' or palabra[i]=='Ü':
                        vocal_u=vocal_u+1
                print('En la palabra '+palabra)
                print('La vocal A aparece '+str(vocal_a)+' veces')
                print('La vocal E aparece '+str(vocal_e)+' veces')
                print('La vocal I aparece '+str(vocal_i)+' veces')
                print('La vocal O aparece '+str(vocal_o)+' veces')
                print('La vocal U aparece '+str(vocal_u)+' veces')
                textfile.write('En la palabra '+palabra)
                textfile.write('\nLa vocal A aparece '+str(vocal_a)+' veces')
                textfile.write('\nLa vocal E aparece '+str(vocal_e)+' veces')
                textfile.write('\nLa vocal I aparece '+str(vocal_i)+' veces')
                textfile.write('\nLa vocal O aparece '+str(vocal_o)+' veces')
                textfile.write('\nLa vocal U aparece '+str(vocal_u)+' veces')
                datos=(palabra,str(vocal_a),str(vocal_e),str(vocal_i),str(vocal_o),str(vocal_u))
                cursor1.execute(sql,datos)
                conexion1.commit()
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa == 8:
            flag = 1
            while flag:
                print('NUMERO PARES O IMPARES DEL 1 AL 100')
                print('¿Qué desea hacer?\n1.(I)ngresar Datos\n2.Ver (H)istorial\n')
                eleccion = input()
                eleccion = str(eleccion)
                if eleccion == 'I' or eleccion == 'i' or eleccion == '1':
                    try:
                        textfile.write('\nNUMERO PARES O IMPARES DEL 1 AL 100')
                        sql="insert into lista_paridad(paridad,cantidad,lista) values (%s,%s,%s)"
                        print('Desea visualizar los numeros (P,p)pares o (I,i)impares')
                        parity = input()
                        parity = str(parity)

                        if parity == 'p' or parity == 'P':
                            npares = 0
                            pares = ''
                            for i in range(1,100+1):
                                paridad = i%2
                                if paridad == 0:
                                    npares = npares + 1
                                    pares = pares + ' ' + str(i)
                            print('La cantidad de numeros pares del 1 al 100 es '+str(npares)+' y son '+pares)
                            textfile.write('\nLa cantidad de numeros pares del 1 al 100 es '+str(npares)+' y son '+pares)
                            datos=('Pares',str(npares),str(pares))
                            cursor1.execute(sql,datos)
                            conexion1.commit()
                        elif parity == 'i' or parity == 'I':
                            nimpares = 0
                            impares = ''
                            for i in range(1,100):
                                paridad = i%2
                                if paridad != 0:
                                    nimpares = nimpares + 1
                                    impares = impares + ' ' + str(i)
                            print('La cantidad de numeros impares del 1 al 100 es '+str(nimpares)+' y son'+impares)
                            textfile.write('\nLa cantidad de numeros impares del 1 al 100 es '+str(nimpares)+' y son'+impares)
                            datos=('Imares',str(nimpares),str(impares))
                            cursor1.execute(sql,datos)
                            conexion1.commit()
                        else:
                            print('Debe seleccionar una opción válida')
                    except:
                        print('Error: Caracter ingresado incorreto')
                elif eleccion == 'H' or eleccion == 'h' or eleccion == '2':
                    cursor1.execute("select * from lista_paridad")
                    for fila in cursor1:
                        print(fila)
                    conexion1.close()
                else:
                    print('Opcion No Válida')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==9:
            flag = 1
            while flag:
                print('TRES LADOS DEL TRIANGULO')
                print('¿Qué desea hacer?\n1.(I)ngresar Datos\n2.Ver (H)istorial\n')
                eleccion = input()
                eleccion = str(eleccion)
                if eleccion == 'I' or eleccion == 'i' or eleccion == '1':
                    textfile.write('\nTRES LADOS DEL TRIANGULO')
                    sql="insert into triangulos(lado1,lado2,lado3,triangulo) values (%s,%s,%s,%s)"
                    try:
                        print('Ingrese tres numeros corresponientes a 3 lados de un triángulo')
                        print('Lado 1')
                        lado1 = input()
                        lado1 = float(lado1)
                        print('Lado 2')
                        lado2 = input()
                        lado2 = float(lado2)
                        print('Lado 3')
                        lado3 = input()
                        lado3 = float(lado3)
                        if lado1 < 0 or lado2 < 0 or lado3 < 0:
                            print('Todos los numeros deben ser positivos')
                        else:
                            if lado1 == lado2 and lado1 == lado3:
                                print('El triángulo es EQUILATERO')
                                textfile.write('\nEl triángulo es EQUILATERO')
                                datos=(str(lado1),str(lado2),str(lado3),'EQUILATERO')
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                            else:
                                if lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
                                    print('El triángulo es ISÓSELES')
                                    textfile.write('\nEl triángulo es ISÓSELES')
                                    datos=(str(lado1),str(lado2),str(lado3),'ISOSELES')
                                    cursor1.execute(sql,datos)
                                    conexion1.commit()
                                else:
                                    print('El triángulo es ESCALENO')
                                    textfile.write('\nEl triángulo es ESCALENO')
                                    datos=(str(lado1),str(lado2),str(lado3),'ESCALENO')
                                    cursor1.execute(sql,datos)
                                    conexion1.commit()
                    except:
                        print('\n______________ERROR_______________')
                        print('Caracter ingresado no es un número')
                elif eleccion == 'H' or eleccion == 'h' or eleccion == '2':
                    cursor1.execute("select * from triangulos")
                    for fila in cursor1:
                        print(fila)
                    conexion1.close()
                else:
                    print('Opcion No Válida')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==10:
            flag = 1
            while flag:
                print('FACTORIAL DE NUMERO DIVISIBLE ENTRE 7')
                print('¿Qué desea hacer?\n1.(I)ngresar Datos\n2.Ver (H)istorial\n')
                eleccion = input()
                eleccion = str(eleccion)
                if eleccion == 'I' or eleccion == 'i' or eleccion == '1':
                    textfile.write('\nFACTORIAL DE NUMERO DIVISIBLE ENTRE 7')
                    sql="insert into fact_multiplos_7(multiplo,resultado) values (%s,%s)"
                    try:
                        print('Ingrese un múltiplo de 7 para obtener su factorial')
                        factor = input()
                        factor = int(factor)
                        if factor < 0:
                            print('Debe ingresar un número positivo')
                        else:
                            if factor%7 == 0:
                                factorial = 1
                                for i in range(1,factor+1):
                                    factorial = factorial*i
                                print('El factorial de '+str(factor)+' es '+str(factorial))
                                textfile.write('\nEl factorial de '+str(factor)+' es '+str(factorial))
                                datos=(str(factor),str(factorial))
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                            else:
                                print('El numero '+str(factor)+' no es un múltiplo de 7')
                                textfile.write('\nEl numero '+str(factor)+' no es un múltiplo de 7')
                                datos=(str(factor),'No es multiplo de 7')
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                    except:
                        print('\n_____________ERROR____________')
                        print('Debe ingresar un numero entero')
                elif eleccion == 'H' or eleccion == 'h' or eleccion == '2':
                    cursor1.execute("select * from fact_multiplos_7")
                    for fila in cursor1:
                        print(fila)
                    conexion1.close()
                else:
                    print('Opcion No Válida')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==11:
            flag = 1
            while flag:
                print('CALCULAR AREA DE FIGURAS GEOMÉTRICAS')
                print('¿Qué desea hacer?\n1.(I)ngresar Datos\n2.Ver (H)istorial\n')
                eleccion = input()
                eleccion = str(eleccion)
                if eleccion == 'I' or eleccion == 'i' or eleccion == '1':
                    textfile.write('\nCALCULAR AREA DE FIGURAS GEOMÉTRICAS')
                    sql="insert into areas_geo(figura,dimension1,dimension2,area) values (%s,%s,%s,%s)"
                    try:
                        print('Seleccione la figura cuya area se calculará')
                        print('(Ci)rculto\n(T)riángulo\n(Cu)adrado\n(R)ectángulo')
                        figura = input()
                        figura = str(figura)
                        if figura == 'Ci':
                            print('Ingrese el radio del círculo.')
                            radio = input()
                            radio = float(radio)
                            if radio < 0:
                                print('El radio debe ser un número positivo')
                            else:
                                area = 3.14159265 * radio * radio
                                print('El área del círculo de radio '+str(radio)+' es '+str(area))
                                textfile.write('\nEl área del círculo de radio '+str(radio)+' es '+str(area))
                                datos=('Circulo',str(radio),'',str(area))
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                        if figura == 'T':
                            print('Ingrese la base del triángulo')
                            base = input()
                            base = float(base)
                            print('Ingrese la altura del triángulo')
                            altura = input()
                            altura = float(altura)
                            if base < 0 or altura < 0:
                                print('Las dimensiones del triángulo deben ser positivas')
                            else:
                                area = 0.5 * base * altura
                                print('El área del triángulo de base '+str(base)+' y altura '+str(altura)+' es '+str(area))
                                textfile.write('\nEl área del triángulo de base '+str(base)+' y altura '+str(altura)+' es '+str(area))
                                datos=('Triangulo',str(base),str(altura),str(area))
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                        if figura == 'Cu':
                            print('Ingrese el lado del cuadrado')
                            lado = input()
                            lado = float(lado)
                            if lado < 0:
                                print('El lado debe ser un número positivo')
                            else:
                                area = lado*lado
                                print('El area del cuadrado de lado '+str(lado)+' es '+str(area))
                                textfile.write('\nEl area del cuadrado de lado '+str(lado)+' es '+str(area))
                                datos=('Cuadraro',str(lado),'',str(area))
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                        if figura == 'R':
                            print('Ingrese la base del rectángulo')
                            base = input()
                            base = float(base)
                            print('Ingrese la altura del rectángulo')
                            altura = input()
                            altura = float(altura)
                            if base < 0 or altura < 0:
                                print('Las dimensiones del rectángulo deben ser positivas')
                            else:
                                area = base * altura
                                print('El área del rectángulo de base '+str(base)+' y altura '+str(altura)+' es '+str(area))
                                textfile.write('\nEl área del rectángulo de base '+str(base)+' y altura '+str(altura)+' es '+str(area))
                                datos=('Rectangulo',str(base),str(altura),str(area))
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                        else:
                            print('Debe ingresar una opción valida')
                    except:
                        print('\n________________ERROR________________')
                        print('El caracter ingresado no es un número')
                elif eleccion == 'H' or eleccion == 'h' or eleccion == '2':
                    cursor1.execute("select * from areas_geo")
                    for fila in cursor1:
                        print(fila)
                    conexion1.close()
                else:
                    print('Opcion No Válida')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==12:
            flag = 1
            while flag:
                print('PROMEDIO DE NOTAS')
                print('¿Qué desea hacer?\n1.(I)ngresar Datos\2.Ver (H)istorial\n')
                eleccion = input()
                eleccion = str(eleccion)
                if eleccion == 'I' or eleccion == 'i' or eleccion == '1':
                    textfile.write('\nPROMEDIO DE NOTAS')
                    sql="insert into promedio_notas(nota1,nota2,nota3,estado,promedio) values (%s,%s,%s,%s,%s)"
                    try:
                        print('Ingrese las 3 notas del alumno')
                        print('Primera Nota')
                        nota1 = input()
                        nota1 = int(nota1)
                        print('Segunda Nota')
                        nota2 = input()
                        nota2 = int(nota2)
                        print('Tercera Nota')
                        nota3 = input()
                        nota3 = int(nota3)

                        if nota1<0 or nota2<0 or nota3<0:
                            print('No deben haber notas negativas, useted es un mal catedrático')
                        else:
                            promedio = (nota1+nota2+nota3)/3
                            if promedio >= 60:
                                print('El alumno fue APROBADO con promedio de '+str(promedio))
                                textfile.write('\nEl alumno fue APROBADO con promedio de '+str(promedio))
                                datos=(str(nota1),str(nota2),str(nota3),'APROBADO',str(promedio))
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                            else:
                                print('El alumno fue REPOROBADO con promedio de '+str(promedio))
                                textfile.write('\nEl alumno fue REPOROBADO con promedio de '+str(promedio))
                                datos=(str(nota1),str(nota2),str(nota3),'REPROBADO',str(promedio))
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                    except:
                        print('\n___________________ERROR______________________')
                        print('El caracter ingresado debe ser un NUMERO ENTERO')
                    print('______________________')
                    print('| VOLER AL MENU (S/N)|')
                    print('______________________')
                elif eleccion == 'H' or eleccion == 'h' or eleccion == '2':
                    cursor1.execute("select * from promedio_notas")
                    for fila in cursor1:
                        print(fila)
                    conexion1.close()
                else:
                    print('Opcion No Válida')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        elif programa ==13:
            flag = 1
            while flag:
                print('DETERMINAR SI EL AÑO FUE BICIESTO')
                print('¿Qué desea hacer?\n1.(I)ngresar Datos\2.Ver (H)istorial\n')
                eleccion = input()
                eleccion = str(eleccion)
                if eleccion == 'I' or eleccion == 'i' or eleccion == '1':
                    textfile.write('\nDETERMINAR SI EL AÑO FUE BICIESTO')
                    sql="insert into aaño_bisiesto(aaño,biciestud ) values (%s,%s)"
                    try:
                        print('Ingrese el año')
                        año = input()
                        año = int(año)
                        if año <0:
                            print('Las fechas anteriores a Cristo son inciertas')
                        else:
                            biciestud = año%4
                            if biciestud == 0:
                                biciestud = año%100
                                if biciestud == 0:
                                    biciestud = año%400
                                    if biciestud == 0:
                                        print('El año '+str(año)+' fue biciesto')
                                        textfile.write('\nEl año '+str(año)+' fue biciesto')
                                        datos=(str(año),'FUE BICIESTO')
                                        cursor1.execute(sql,datos)
                                        conexion1.commit()
                                    else:
                                        print('El año '+str(año)+' NO fue biciesto')
                                        textfile.write('\nEl año '+str(año)+' NO fue biciesto')
                                        datos=(str(año),'NO FUE BICIESTO')
                                        cursor1.execute(sql,datos)
                                        conexion1.commit()
                                else:
                                    print('El año '+str(año)+' fue biciesto')
                                    textfile.write('\nEl año '+str(año)+' fue biciesto')
                                    datos=(str(año),'FUE BICIESTO')
                                    cursor1.execute(sql,datos)
                                    conexion1.commit()
                            else:
                                print('El año '+str(año)+' NO fue biciesto')
                                textfile.write('\nEl año '+str(año)+' NO fue biciesto')
                                datos=(str(año),'NO FUE BICIESTO')
                                cursor1.execute(sql,datos)
                                conexion1.commit()
                    except:
                        print('\n_________ERROR________')
                        print('Debe ingresar un número')
                elif eleccion == 'H' or eleccion == 'h' or eleccion == '2':
                    cursor1.execute("select * from aaño_bisiesto")
                    for fila in cursor1:
                        print(fila)
                    conexion1.close()
                else:
                    print('Opcion No Válida')
                print('______________________')
                print('| VOLER AL MENU (S/N)|')
                print('______________________')
                bandera = input()
                bandera = str(bandera)
                if bandera == 'S' or bandera == 's':
                    flag = 0
                elif bandera == 'N' or bandera == 'n':
                    flag = 1
                else:
                    flag = 1
        else:
            textfile.close()
            conexion1.close()
            print('Gracias por usar nuestro programa')
            #exit()
            #pkill -f TareaPrimerParcial
            #sys.exit()
            #raise SystemExit
            os._exit(0)
    except:
        print('\n_________ERROR_________')
        print('Debe ingresar un número')
        print('!!!!!!!!!!!!!!!!!!!!!!!\n')
