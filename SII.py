#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, csv

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
        revise = [line for line in revise1[1:] if line.strip()]
    return revise


# Agregar columna de nombres a la cabecera de la estructura de datos
def nombres(datoSN, nombre):
    return ["%s,%s" % (nombre, dato) for dato in datoSN]


# Extraer los datos por cada archivo
for archivo in nombres_archivos:
    first = True
    datos = []
    cabecera = ""
    for nombre in nombres_carpetas:
        ruta = nombre + '/' + archivo
        datoSN = lectura(ruta)
        # Extrae la cabecera del csv en la primera pasada
        if first:
            cabecera = "%s,%s" % ("Cliente", datoSN[0])
            first = False
        # Remueve la cabecera
        datoSN.remove(datoSN[0])
        # Agrega los nombres
        datoSN = nombres(datoSN, nombre)
        datos.extend(datoSN)
    with open("test_" + archivo, 'w') as destino:
        escritor = csv.writer(destino, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # Agrega la cabecera al inicio
        escritor.writerow(cabecera.split(","))
        for dato in datos:
            escritor.writerow(dato.split(","))
