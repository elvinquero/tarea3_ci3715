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
	
	def verificarClave(self, key):
		invalidos = [1, ""]
		digitos = 0
		mayus = 0
		minus = 0
		for i in range(len(key)): 
			caracter = key[i]
			if str.isdigit(caracter):
				digitos += 1
			elif str.isalpha(caracter):
				if caracter.isupper():
					mayus += 1
				else:
					minus += 1
			else:
				invalidos.append(caracter)
		
		if digitos < 1 or mayus < 1 or minus < 1 or mayus+minus < 3:
			return [0, "Clave invalida: debe contener al menos un digito y al menos tres letras (al menos una mayuscula y una minuscula)"]
		
		elif len(invalidos) != 2:
			invalidos[0] = 0
			invalidos[1] = "Clave invalida: solo puede colocar valores alfa numericos"

		return invalidos
	
	def verificarCorreo(self, mail):
		invalidos = [1, ""]

		seccionesArroba = mail.split("@")
		if len(seccionesArroba) != 2:
			if len(seccionesArroba) < 2:
				return [0, "Correo electronico invalido: debe colocar @"]
			else:
				return [0, "Correo electronico invalido: no puede colocar mas de un @"]
		elif seccionesArroba[0] == "" or seccionesArroba[1] == "":
			return [0, "Correo electronico invalido"]
		
		seccion1 = seccionesArroba[0]
		seccionesPunto = seccionesArroba[1].split(".")
		if len(seccionesPunto) < 2 or seccionesPunto[0] == "" or seccionesPunto[1] == "":
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
		else:
			charInvalidos = self.verificarClave(clave)
			if len(charInvalidos)==2:
				if charInvalidos[0] < 1:
					validKey = 0
					mensajeKey = charInvalidos[1]	
			else:
				validKey = 0
				mensajeKey = charInvalidosMail[1]

		return [validMail, validKey, mensajeMail, mensajeKey]	
	
	def registrarUsuario(self, email, clave1, clave2):
		if (clave1 != clave2):
			return [-1, 0, "Las claves no coinciden"]
			
		verificacion = self.verificar(email, clave1)
		if verificacion[0] == 1 and verificacion[1] == 1:
			if email not in self.usuariosRegistrados: 
				self.usuariosRegistrados[email] = self.encriptar( clave1)
				return [1, 1, "Usuario registrado exitosamente"]
			else:
				return [0, -1, "El usuario ya existe"]
		
		else:
			return [verificacion[0], verificacion[1], verificacion[2] + "\n" + verificacion[3]]

	def IngresarUsuario(self, email, clave):
		verificacion = self.verificar(email, clave)
		try:
			assert(verificacion[0] == 1 and verificacion[1] == 1)
			if ( email in self.usuariosRegistrados ):
				if (self.usuariosRegistrados[email] == self.encriptar(clave) ):
					return [1, "Usuario aceptado"]
				else:
					return [0, "Clave invalida"]
			else:
				return [0, "Usuario invalido"]
		except:
			return [0, verificacion[2] + " " + verificacion[3]]