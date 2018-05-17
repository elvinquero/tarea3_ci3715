'''
Created on 16 may. 2018

@author: Angelica Acosta y Elvin Quero
'''
import unittest
from App.models import Seguridad

class TestSeguridad(unittest.TestCase):
		
	#Caso 1 frontera inferior clave registro
	def testClave8(self):
		seguridad = Seguridad()
		email = "ana@gmail.com"
		clave= "holahola"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)

		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 1)
		
	#Caso 2 frontera superior clave registro
	def testClave16(self):
		seguridad = Seguridad()
		email = "anita@gmail.com"
		clave= "holaholaholahola"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 1)


	#Caso 3 esquina superior clave
	def testClaveMas16(self):
		seguridad = Seguridad()
		email = "anitaaaa@gmail.com"
		clave= "holaholaholahola1"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 0)
		
	#Caso 4 esquina inferior clave registro
	def testClaveMenos8(self):
		seguridad = Seguridad()
		email = "jose@gmail.com"
		clave= "holahol"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 0)
		
	#Caso 5 valido registro
	def testRegistroValido(self):
		seguridad = Seguridad()
		email = "angey@gmail.com"
		clave= "hola1234"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 1)
	
	#Caso 6 esquina inferior correo registro
	def testCorreoSinArrob(self):
		seguridad = Seguridad()
		email = "gmail.com"
		clave= "holahola"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 1)
		
	#Caso 7 esquina superior correo registro
	def testCorreoMasArrob(self):
		seguridad = Seguridad()
		email = "lucia@hotmail@gmail.com"
		clave= "holahola"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 1)
	
	#Caso 8 esquina inferior correo registro
	def testCorreoSinPunto(self):
		seguridad = Seguridad()
		email = "paty@gmailcom"
		clave= "holahola"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 1)

	#Caso 9 esquina inferior correo registro
	def testCorreoCaracteresEspeciales(self):
		seguridad = Seguridad()
		email = "sofia#97@gmail.com"
		clave= "holahola"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 1)
	
