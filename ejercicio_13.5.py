#!/usr/bin/python
# -*- coding: utf-8 -*-

# hola, hola

fd = open('/etc/passwd', 'r')

lineas = fd.readlines()
fd.close()

Diccionario = {}

for linea in lineas:
    elementos = linea.split(':')
    print elementos[0], elementos[-1][:-1]
    Diccionario[elementos[0]] = elementos[-1][:-1]

print "Hay", len(lineas), "usuarios"

print "\n"

try:
	print Diccionario["root"]
	print Diccionario["imaginario"]
except KeyError:
	print "El usuario no existe"