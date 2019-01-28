#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, pandas

# El siguiente archivo realiza el que corresponde a un proceso ETL (Extracción, Transformación y Lectura),
# consistiendo específicamente en la lectura de archivos csv separados en carpetas por nombres, con el 
# objetivo de unirlos en archivos csv únicos, integrando los nombres de los usuarios originales, esto
# con propósitos de análisis.

# Este script se ejecuta dentro de la carpeta que, supuestamente, contiene únicamente las carpetas con el
# nombre y archivos correspondientes a cada cliente

# Listado de carpetas de clientes

carpetas = next(os.walk("."))[1]

# Nombres de archivos por carpeta
# (Extrae los nombres de los archivos pedidos desde una de las carpetas, esto suponiendo que los nombres
# son todos consistentes y los mismos en cada carpeta)

archivos = next(os.walk(carpetas[0]))[2]

# Extraer los datos por cada archivo

for archivo in archivos:
    for carpeta in carpetas:
		ruta = carpeta + '/' + archivo
		print ruta
		df = pandas.read_csv(ruta, skiprows=1)
		print df

