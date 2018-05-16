from django.db import models

# Create your models here.

class Seguridad:
	def __init__(self):
		self.usuariosRegistrados = {}
	
	def encriptar(self, key):
		firstKey = key[::-1]
		newKey = ""
		for i in range(len(key)):
			asciiLetter = ord(firstKey[i]) + 3
			newKey += chr(asciiLetter)
		return newKey
	
	def registrarUsuario(self, email, clave1, clave2):
		if (clave1 != clave2):
			return [0, 0, "Las claves no coinciden"]
			
		self.usuariosRegistrados[email] = self.encriptar(clave1)
		return [1, 1, "Usuario registrado exitosamente"]
		