#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

# El siguiente archivo realiza el que corresponde a un proceso ETL (Extracción, Transformación y Lectura),
# consistiendo específicamente en la lectura de archivos csv separados en carpetas por nombres, con el 
# objetivo de unirlos en archivos csv únicos, integrando los nombres de los usuarios originales, esto
# con propósitos de análisis.

# Este script se ejecuta dentro de la carpeta que, supuestamente, contiene únicamente las carpetas con el
# nombre y archivos correspondientes a cada cliente

# Listado de caarpetas de clientes

carpetas = next(os.walk("."))[1]

# Lectura de archivos por carpeta
print next(os.walk("."))[2]
# disk.csv
