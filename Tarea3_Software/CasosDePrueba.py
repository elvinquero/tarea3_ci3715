'''
Created on 16 may. 2018

@author: Angelica Acosta y Elvin Quero
'''
import unittest
from App.models import Seguridad

class TestSeguridad(unittest.TestCase):
	
	#Caso 1 frontera inferior clave
	def testClave8(self):
		email = "ana@gmail.com"
		clave= "holahola"
		seguridad = Seguridad()
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)

		assert (nuevoUsuario[0] == 2 and nuevoUsuario[1] == 2)
		
	#Caso 2 frontera superior clave
	def testClave16(self):
		email = "anita@gmail.com"
		clave= "holaholaholahola"
		seguridad = Seguridad()
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 2 and nuevoUsuario[1] == 2)