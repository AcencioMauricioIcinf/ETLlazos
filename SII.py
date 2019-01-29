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
#
def lectura(ruta):
    with open(ruta, 'r') as archivo:
        revise1 = [line.replace('\0', '').replace('\r', '').replace('\n', '') for line in archivo]
        revise = [line for line in revise1[1:] if line.strip()]
    return revise


# Extraer los datos por cada archivo

for nombre in nombres_archivos:
    print nombre
    revise = []
    for carpeta in nombres_carpetas:
        ruta = carpeta + '/' + nombre
        revise.extend(lectura(ruta))
    print revise
