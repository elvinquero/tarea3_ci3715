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
	
	def verificarCorreo(self, mail):
		invalidos = [1, ""]

		seccionesArroba = mail.split("@")
		if len(seccionesArroba) != 2:
			if len(seccionesArroba) < 2:
				return [0, "Correo electronico invalido: debe colocar @"]
			else:
				return [0, "Correo electronico invalido: no puede colocar mas de un @"]
		else:
			return invalidos
	
	def verificar(self, email, clave):
		validMail = 1
		mensajeMail = ""
		validKey = 1
		mensajeKey = ""
		
		charInvalidosMail = self.verificarCorreo(email)
		if len(charInvalidosMail)==2:
			if charInvalidosMail[0] < 1:
				validMail = 0
				mensajeMail = charInvalidosMail[1]	
				
		if len(clave) < 8 or len(clave) > 16:
			validKey = 0
			mensajeKey = "Clave invalida: debe tener entre 8 y 16 caracteres"

		return [validMail, validKey, mensajeMail, mensajeKey]	
	
	def registrarUsuario(self, email, clave1, clave2):
		if (clave1 != clave2):
			return [0, 0, "Las claves no coinciden"]
			
		verificacion = self.verificar(email, clave1)
		if verificacion[0] == 1 and verificacion[1] == 1:
			self.usuariosRegistrados[email] = self.encriptar( clave1)
			return [1, 1, "Usuario registrado exitosamente"]
		
		else:
			return [verificacion[0], verificacion[1], verificacion[2] + "\n" + verificacion[3]]

		