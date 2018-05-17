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
		
		seccion1 = seccionesArroba[0]
		seccionesPunto = seccionesArroba[1].split(".")
		if len(seccionesPunto) < 2:
			return [0, "Correo electronico invalido: debe colocar el dominio"]

		for i in range(len(seccion1)):
			caracter = seccion1[i]
			if ( (not str.isdigit(caracter)) and (not str.isalpha(caracter)) and (caracter != ".") and (caracter != "_") and (caracter != "-") ):
				invalidos.append(caracter)

		for i in range(len(seccionesPunto)):
			n = len(seccionesPunto[i])
			for j in range(n):
				caracter = seccionesPunto[i][j]
				if ( (not str.isdigit(caracter)) and (not str.isalpha(caracter))):
					invalidos.append(caracter)	
		
		if len(invalidos) != 2:
			invalidos[0] = -1
			invalidos[1] = "Correo electronico invalido: presenta caracteres no permitidos"
		
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
		else:
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

		