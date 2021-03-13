import psycopg2
from io import open
ruta = '201630870.txt'
textfile = open(ruta,'a+')
textfile.write('\nPrimer Parcial')
flag = 1
while flag:
    textfile = open(ruta,'a+')
    conexion1 = psycopg2.connect("dbname=PrimerParcial201630870 user=postgres password=ajkimtepaz")
    cursor1=conexion1.cursor()
    print('\n\n\nIngrese el programa que desea elegir')
    try:
        print('1.Información de Población')
        print('2.Operación con los 10 primeros números naturales')
        print('3.La diferencia entre la suma de los 100 primeros numeros naturales')
        print('4.Los factores primos de 13195')
        print('5.¿Cuál es el factor primo más grande de 600851475143')
        print('6.Suseción de Fibonacci')
        print('7.Areas de un cono')
        print('Otro. Salir\n')
        eleccion = input()
        eleccion = int(eleccion)
        print('\n\n\n\n')
        if eleccion == 1:
            try:
                flag2 = 1
                while flag2:
                    try:
                        print('Información sobre la población')
                        print('Ingrese la cantidad de personas\n')
                        NN = input()
                        NN = int(NN)
                        prom_pesoG = 0
                        prom_alturaG = 0
                        promedio_pesoM = 0
                        promedio_alturaM = 0
                        promedio_pesoF = 0
                        promedio_alturaF = 0
                        NM = 0
                        NF = 0
                        i = 0
                        while i < NN:
                            i += 1
                            print('Ingrese el peso de la persona numero '+str(i)+' en libras\n')
                            peso = input()
                            peso = float(peso)
                            print('Ingrese la altura de la persona numero '+str(i)+' en metros\n')
                            altura = input()
                            altura = float(altura)
                            print('Ingrese el género de la perosna numero '+str(i)+'\n')
                            print('(M) || (m)= Masculino.')
                            print('(F) || (f)= Femenino')
                            genero = input()
                            genero = str(genero)
                            prom_pesoG = prom_pesoG + peso
                            prom_alturaG = prom_alturaG + altura
                            if genero == 'M' or genero == 'm':
                                NM = NM + 1
                                promedio_pesoM = promedio_pesoM + peso
                                promedio_alturaM = promedio_alturaM + altura
                            elif genero == 'F' or genero == 'f':
                                NF = NF + 1
                                promedio_pesoF = promedio_pesoF + peso
                                promedio_alturaF = promedio_alturaF + altura
                            else:
                                print('Género inválido\nPrograma Reiniciado')
                                prom_pesoG = 0
                                prom_alturaG = 0
                                promedio_pesoM = 0
                                promedio_alturaM = 0
                                promedio_pesoF = 0
                                promedio_alturaF = 0
                                NM = 0
                                NF = 0
                                i = 0

                        if NF != 0 and NM == 0:
                            promedio_pesoF = promedio_pesoF/NF
                            promedio_alturaF = promedio_alturaF/NF
                            print('Promedio de Peso Femenino = '+str(promedio_pesoF))
                            print('Promedio de Altura Femenino = '+str(promedio_alturaF))
                            print('Promedio de Peso General = '+str(promedio_pesoF))
                            print('Promedio de Altura General = '+str(promedio_alturaF))
                            sql="insert into Poblacion(prom_peso_General, prom_altura_General, prom_peso_Femenino, prom_altura_Femenino) values (%s,%s,%s,%s)"
                            datos=(str(promedio_pesoF),str(promedio_alturaF),str(promedio_pesoF),str(promedio_alturaF))
                            cursor1.execute(sql, datos)
                            conexion1.commit()
                            textfile.write('\nPromedio de Peso Masculino = '+str(promedio_pesoF))
                            textfile.write('\nPromedio de Altura Masculino = '+str(promedio_alturaF))
                            textfile.write('\nPromedio de Peso General = '+str(promedio_pesoF))
                            textfile.write('\nPromedio de Altura General = '+str(promedio_alturaF))
                        elif NF == 0 and NM != 0:
                            promedio_pesoM = promedio_pesoM/NM
                            promedio_alturaM = promedio_alturaM/NM
                            print('Promedio de Peso Masculino = '+str(promedio_pesoM))
                            print('Promedio de Altura Masculino = '+str(promedio_alturaM))
                            print('Promedio de Peso General = '+str(promedio_pesoM))
                            print('Promedio de Altura General = '+str(promedio_alturaM))
                            sql="insert into Poblacion(prom_peso_General, prom_altura_General, prom_peso_Masculino, prom_altura_Masculino) values (%s,%s,%s,%s)"
                            datos=(str(promedio_pesoM),str(promedio_alturaM),str(promedio_pesoM),str(promedio_alturaM))
                            cursor1.execute(sql, datos)
                            conexion1.commit()
                            textfile.write('\nPromedio de Peso Masculino = '+str(promedio_pesoM))
                            textfile.write('\nPromedio de Altura Masculino = '+str(promedio_alturaM))
                            textfile.write('\nPromedio de Peso General = '+str(promedio_pesoM))
                            textfile.write('\nPromedio de Altura General = '+str(promedio_alturaM))
                        elif NF != 0 and NM != 0:
                            promedio_pesoM = promedio_pesoM/NM
                            promedio_alturaM = promedio_alturaM/NM
                            promedio_pesoF = promedio_pesoF/NF
                            promedio_alturaF = promedio_alturaF/NF
                            prom_pesoG = prom_pesoG/NN
                            prom_alturaG = prom_alturaG/NN
                            print('Promedio de Peso Femenino = '+str(promedio_pesoF))
                            print('Promedio de Altura Femenino = '+str(promedio_alturaF))
                            print('Promedio de Peso Masculino = '+str(promedio_pesoM))
                            print('Promedio de Altura Masculino = '+str(promedio_alturaM))
                            print('Promedio de Peso General = '+str(prom_pesoG))
                            print('Promedio de Altura General = '+str(prom_alturaG))
                            sql="insert into Poblacion(prom_peso_General, prom_altura_General, prom_peso_Masculino, prom_altura_Masculino, prom_peso_Femenino, prom_altura_Femenino) values (%s,%s,%s,%s,%s,%s)"
                            datos=(str(prom_pesoG),str(prom_alturaG),str(promedio_pesoM),str(promedio_alturaM),str(promedio_pesoF),str(promedio_alturaF))
                            cursor1.execute(sql, datos)
                            conexion1.commit()
                            textfile.write('\nPromedio de Peso Femenino = '+str(promedio_pesoF))
                            textfile.write('\nPromedio de Altura Femenino = '+str(promedio_alturaF))
                            textfile.write('\nPromedio de Peso Masculino = '+str(promedio_pesoM))
                            textfile.write('\nPromedio de Altura Masculino = '+str(promedio_alturaM))
                            textfile.write('\nPromedio de Peso General = '+str(prom_pesoG))
                            textfile.write('\nPromedio de Altura General = '+str(prom_alturaG))
                        flag2 = 0;
                        conexion1.close()
                        textfile.close()
                    except:
                        print('Dato Inválido\nPrograma Reiniciado')
                        conexion1.close()
                        textfile.close()
            except:
                print('Error. Debe ingresar un número entero')
                conexion1.close()
                textfile.close()
        elif eleccion == 2:
            print('Operación con los 10 primeros números naturales')
            sumadecuadrados_int = 0
            cuadradodesumas_int = 0
            sumadecuadrados_str = ''
            cuadradodesumas_str = ''
            for i in range(1,11):
                if i<10:
                    sumadecuadrados_str = sumadecuadrados_str+' '+ str(i)+'^2 +'
                    sumadecuadrados_int = sumadecuadrados_int + (i)*(i)
                else:
                    sumadecuadrados_str = sumadecuadrados_str+' '+ str(i)+'^2'
                    sumadecuadrados_int = sumadecuadrados_int + (i)*(i)
            for i in range(1,11):
                if i<10:
                    cuadradodesumas_str = cuadradodesumas_str + ' ' + str(i)+' +'
                    cuadradodesumas_int = cuadradodesumas_int + i
                else:
                    cuadradodesumas_str = cuadradodesumas_str + ' ' + str(i)
                    cuadradodesumas_int = cuadradodesumas_int + i
            cuadradodesumas_int = cuadradodesumas_int*cuadradodesumas_int
            
            print('La suma de los cuadradrados de los primeros 10 numeros naturales es')
            print(sumadecuadrados_str +' = '+ str(sumadecuadrados_int))
            print('El cuadrado de la suma de los primeros 10 numeros naturales es')
            print('('+cuadradodesumas_str +')^2 = '+ str(cuadradodesumas_int))
            print('Por lo tanto la diferencia entre la suma de los cuadrado')
            print('de los primeros 10 numeros y el cuadrado de la suma es')
            diferencia = cuadradodesumas_int-sumadecuadrados_int
            print(str(cuadradodesumas_int)+' - '+str(sumadecuadrados_int)+' = '+str(diferencia))

            sumadecuadrados = (sumadecuadrados_str +' = '+ str(sumadecuadrados_int))
            cuadradodesumas = ('('+cuadradodesumas_str +')^2 = '+ str(cuadradodesumas_int))
            diferencia = str(diferencia)
            sql="insert into numerosnaturales(sumadecuadrados,cuadradodesumas,diferencia) values (%s,%s,%s)"
            datos=(sumadecuadrados,cuadradodesumas,diferencia)
            cursor1.execute(sql, datos)
            conexion1.commit()
            textfile.write('\nOperaciones con los Primeros 10 numeros naturales')
            textfile.write('\nLa suma de los cuadradrados de los primeros 10 numeros naturales es\n'+sumadecuadrados)
            textfile.write('\nEl cuadrado de la suma de los primeros 10 numeros naturales es\n'+cuadradodesumas)
            textfile.write('\nPor lo tanto la diferencia entre la suma de los cuadrado\nde los primeros 10 numeros y el cuadrado de la suma es\n'+diferencia)
            conexion1.close()
            textfile.close() 
        elif eleccion == 3:
            print('La diferencia entre la suma de los 100 primeros numeros naturales')
            sumadecuadrados_int = 0
            cuadradodesumas_int = 0
            sumadecuadrados_str = ''
            cuadradodesumas_str = ''
            for i in range(1,101):
                if i<100:
                    sumadecuadrados_str = sumadecuadrados_str+' '+ str(i)+'^2 +'
                    sumadecuadrados_int = sumadecuadrados_int + (i)*(i)
                else:
                    sumadecuadrados_str = sumadecuadrados_str+' '+ str(i)+'^2'
                    sumadecuadrados_int = sumadecuadrados_int + (i)*(i)
            for i in range(1,101):
                if i<100:
                    cuadradodesumas_str = cuadradodesumas_str + ' ' + str(i)+' +'
                    cuadradodesumas_int = cuadradodesumas_int + i
                else:
                    cuadradodesumas_str = cuadradodesumas_str + ' ' + str(i)
                    cuadradodesumas_int = cuadradodesumas_int + i
            cuadradodesumas_int = cuadradodesumas_int*cuadradodesumas_int
            
            print('La suma de los cuadradrados de los primeros 100 numeros naturales es')
            print(sumadecuadrados_str +' = '+ str(sumadecuadrados_int))
            print('El cuadrado de la suma de los primeros 100 numeros naturales es')
            print('('+cuadradodesumas_str +')^2 = '+ str(cuadradodesumas_int))
            print('Por lo tanto la diferencia entre la suma de los cuadrado')
            print('de los primeros 10 numeros y el cuadrado de la suma es')
            diferencia = cuadradodesumas_int-sumadecuadrados_int
            print(str(cuadradodesumas_int)+' - '+str(sumadecuadrados_int)+' = '+str(diferencia))

            sumadecuadrados = (sumadecuadrados_str +' = '+ str(sumadecuadrados_int))
            cuadradodesumas = ('('+cuadradodesumas_str +')^2 = '+ str(cuadradodesumas_int))
            diferencia = str(diferencia)
            sql="insert into ciennumerosnaturales(sumadecuadrados,cuadradodesumas,diferencia) values (%s,%s,%s)"
            datos=(sumadecuadrados,cuadradodesumas,diferencia)
            cursor1.execute(sql, datos)
            conexion1.commit()
            textfile.write('\nOperaciones con los Primeros 100 numeros naturales')
            textfile.write('\nLa suma de los cuadradrados de los primeros 100 numeros naturales es\n'+sumadecuadrados)
            textfile.write('\nEl cuadrado de la suma de los primeros 100 numeros naturales es\n'+cuadradodesumas)
            textfile.write('\nPor lo tanto la diferencia entre la suma de los cuadrado\nde los primeros 10 numeros y el cuadrado de la suma es\n'+diferencia)
            conexion1.close()
            textfile.close() 
        elif eleccion == 4:
            print('Los factores primos de 13195')
            lista = ''
            primofactor = 0
            for i in range(1,13196):
                if 13195%i == 0:
                    for j in range(1,i+1):
                        if i%j != 0:
                            lista = lista + ' ' + str(i)
            print(lista)
                
        elif eleccion == 5:
            print('¿Cuál es el factor primo más grande de 600851475143')
        
        elif eleccion == 6:
            flag3 = 1
            while flag3:
                print('Suseción de Fibonacci')
                try:
                    print('Ingrese un número entero')
                    nn = input()
                    nn = int(nn)
                    if nn < 0:
                        print('No debe ingresar números negativos')
                    else:
                        n1 = 0
                        n2 = 1
                        if nn == 0:
                            print('La suseción de Fibonacci de 0 es\n 0')
                        elif nn == 1:
                            print('La suseción de Fibonacci de 1 es\n 1')
                        else:
                            susecion = '0,1'
                            for i in range(2,nn):
                                nth = n1 + n2
                                n1 = n2
                                n2 = nth
                                susecion = susecion +','+str(nth)
                            print('La suseción de Fibonnacci hasta '+str(nn)+' es')
                            print(susecion)
                            sql="insert into fibonacci(Entero,Susecion) values (%s,%s)"
                            datos=(nn,susecion)
                            cursor1.execute(sql, datos)
                            conexion1.commit()
                            textfile.write('\nLa suseción de Fibonacci hasta '+str(nn)+' es:\n')
                            textfile.write(susecion)
                            conexion1.close()
                            textfile.close()
                            flag3 = 0
                            
                except:
                    print('Debe ingresar un número entero')
        elif eleccion == 7:
            print('Areas de un cono')
            flag4 = 1
            while flag4:
                try:
                    print('Ingrese el radio del cono')
                    radio = input()
                    radio = float(radio)
                    print('Ingrese la altura del cono')
                    altura = input()
                    altura = float(altura)
                    print('Ingrese la generatriz del cono')
                    generatriz = input()
                    generatriz = float(generatriz)
                    area_base = (radio*radio)*(3.14159265359)
                    area_lateral = 3.14159265359*radio*generatriz
                    area_total = area_base + area_lateral
                    volumen = (3.14159265359/3)*(radio*radio)*(altura)
                    print('El área de la base del cono es '+str(area_base))
                    print('El área lateral del cono es '+str(area_lateral))
                    print('El área total del cono es '+str(area_total))
                    print('El volumen del cono es '+str(volumen))
                    sql="insert into cono(area_base,area_lateral,area_total,volumen) values (%s,%s,%s,%s)"
                    datos=(area_base,area_lateral,area_total,volumen)
                    cursor1.execute(sql, datos)
                    conexion1.commit()
                    textfile.write('\nLas áreas de un cono de dimensiones')
                    textfile.write('\nRadio: '+str(radio))
                    textfile.write('\nAltura: '+str(altura))
                    textfile.write('\nGeneratriz: '+str(generatriz)+'\n son: \n')
                    textfile.write('\nÁrea de la base: '+str(area_base))
                    textfile.write('\nÁrea de lateral: '+str(area_lateral))
                    textfile.write('\nÁrea total: '+str(area_total))
                    textfile.write('\nVolumen: '+str(volumen))
                    conexion1.close()
                    textfile.close()
                    flag4 = 0
                except:
                    print('Debe ingresar un número')
        else:
            print('Gracias por usar nuestro programa')
            flag = 0
            textfile.close()
    except:
        print('Debe ingresar un numero entero')

