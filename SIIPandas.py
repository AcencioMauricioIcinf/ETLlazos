#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, pandas
from sys import getsizeof
from time import time

# PRUEBAS Y MEDIDAS:
# Refiérase a los siguientes 2 parámetros para realizar mediciones en la ejecución de este archivo

# Si desea medir y y mostrar el tiempo de ejecución del procesado de datos, cambie el siguiente valor a True:
medirTiempo = False

# Si desea visualizar el espacio en bytes ocupado por los datos procesados y la estructura interna utilizada
# para ello, cambie el siguiente valor a True:
# NOTA: Esta medición puede afectar el tiempo de ejecución del proceso considerablemente, por lo que se recomienda
# medir ambas variables por separado.
medirMemoria = False

# INSTRUCCIONES:
# El siguiente archivo realiza el que corresponde a un proceso ETL (Extracción, Transformación y Lectura),
# consistiendo específicamente en la lectura de archivos csv separados en carpetas por nombres, con el
# objetivo de unirlos en archivos csv únicos, integrando los nombres de los usuarios originales, esto
# con propósitos de análisis.

# Este script se ejecuta dentro de la carpeta que, supuestamente, contiene únicamente las carpetas con el
# nombre y archivos correspondientes a cada cliente

# Listado de carpetas de clientes
nombres_carpetas = next(os.walk("."))[1]

# Nombres de archivos por carpeta
# (Extrae los nombres de los archivos pedidos desde una de las carpetas, esto suponiendo que los nombres
# son todos consistentes y los mismos en cada carpeta)
nombres_archivos = next(os.walk(nombres_carpetas[0]))[2]


# Definición de función para la extracción de datos
# Remoción de la primera línea, más líneas sin contenido
def lectura(ruta):
    with open(ruta, 'r') as archivo:
        # Remoción de carácteres vacíos
        revise1 = [line.replace('\0', '').replace('\r', '').replace('\n', '') for line in archivo]
        # Remoción de líneas sin contenido, junto a la 1ºa línea, que contiene carácteres especiales
        revise = [line.split(',') for line in revise1[1:] if line.strip()]
    return revise


# Agregar columna de nombres a la cabecera de la estructura de datos
def nombres(datoSN, nombre):
    for dato in datoSN:
        dato.insert(0, nombre)
    return datoSN


# Extraer los datos por cada archivo
if medirTiempo:
    start = time()
if medirMemoria:
    print "Memoria en bytes:"
    print "Lista principal; Suma de listas;  Suma de textos"
for archivo in nombres_archivos:
    first = True
    datos = []
    cabecera = ""
    for nombre in nombres_carpetas:
        ruta = nombre + '/' + archivo
        datoSN = lectura(ruta)
        # Extrae la cabecera del csv en la primera pasada
        if first:
            cabecera = datoSN[0]
            cabecera.insert(0, "Cliente")
            first = False
        # Remueve la cabecera
        datoSN.remove(datoSN[0])
        # Agrega los nombres
        datoSN = nombres(datoSN, nombre)
        datos.extend(datoSN)
    if medirMemoria:
        print '%-16s %-16s %s' % (getsizeof(datos), sum(getsizeof(dato) for dato in datos),
                                  sum(sum(getsizeof(dato1) for dato1 in dato) for dato in datos))
    with open('PND_' + archivo, 'w') as destino:
        df = pandas.DataFrame(datos, columns=cabecera)
        df.to_csv(destino, index=False)
if medirTiempo:
    stop = time()
    print 'Tiempo transcurrido: %f ms' % ((stop - start) * 1000)
