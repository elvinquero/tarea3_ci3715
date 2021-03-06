'''
Created on 16 may. 2018

@author: Angelica Acosta y Elvin Quero
'''
import unittest
from App.models import Seguridad

class TestSeguridad(unittest.TestCase):
		
	#Caso 1 frontera inferior clave registro
	#La primera vez que se ejecuto fallo
	def testClave8(self):
		seguridad = Seguridad()
		email = "ana@gmail.com"
		clave= "Hola1234"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)

		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 1)
		
	#Caso 2 frontera superior clave registro
	#La primera vez que se ejecuto fallo
	def testClave16(self):
		seguridad = Seguridad()
		email = "anita@gmail.com"
		clave= "HolaHolaHola1234"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 1)


	#Caso 3 esquina superior clave
	#La primera vez que se ejecuto fallo
	def testClaveMas16(self):
		seguridad = Seguridad()
		email = "anitaaaa@gmail.com"
		clave= "holaholaholaholA1"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 0)
		
	#Caso 4 esquina inferior clave registro
	#La primera vez que se ejecuto fallo
	def testClaveMenos8(self):
		seguridad = Seguridad()
		email = "jose@gmail.com"
		clave= "holahol"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 0)
		
	#Caso 5 frontera registro
	#La primera vez que se ejecuto no fallo
	def testRegistroValido(self):
		seguridad = Seguridad()
		email = "angey@gmail.com"
		clave= "Hola1234"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 1)
	
	#Caso 6 esquina inferior correo registro
	#La primera vez que se ejecuto fallo
	def testCorreoSinArrob(self):
		seguridad = Seguridad()
		email = "gmail.com"
		clave= "holA1ola"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 1)
		
	#Caso 7 esquina superior correo registro
	#La primera vez que se ejecuto fallo
	def testCorreoMasArrob(self):
		seguridad = Seguridad()
		email = "lucia@hotmail@gmail.com"
		clave= "holaho1A"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 1)
	
	#Caso 8 esquina inferior correo registro
	#La primera vez que se ejecuto fallo
	def testCorreoSinPunto(self):
		seguridad = Seguridad()
		email = "paty@gmailcom"
		clave= "h01aHola"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 1)

	#Caso 9 esquina inferior correo registro
	#La primera vez que se ejecuto fallo
	def testCorreoCaracteresEspeciales(self):
		seguridad = Seguridad()
		email = "sofia#97@gmail.com"
		clave= "hoLah0la"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 1)
	
	#Caso 10 esquinas superiores registro
	#La primera vez que se ejecuto fallo
	def testCorreoYClaveInvalida(self):
		seguridad = Seguridad()
		email = "aura@@gmail.com"
		clave= "Holahola123456789"
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 0)
		
	#Caso 11 esquinas inferiores registro
	#La primera vez que se ejecuto fallo
	def testClaveCaractesEsp(self):
		seguridad = Seguridad()
		email = "aura,@gmail.com"
		clave= "holametu."
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)

		assert (nuevoUsuario[0] == 0 and nuevoUsuario[1] == 0)
	
	#Caso 12 esquina inferior clave registro
	#La primera vez que se ejecuto no fallo
	def testClaveSinDig(self):
		seguridad = Seguridad()
		email = "aura@gmail.com"
		clave= "HOLAhola"	
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 0)

	#Caso 13 esquina inferior clave registro
	#La primera vez que se ejecuto no fallo
	def testClaveSinMayus(self):
		seguridad = Seguridad()
		email = "aura@gmail.com"
		clave= "hola12hola"
		
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 0)
		
	#Caso 14 esquina inferior clave registro
	#La primera vez que se ejecuto no fallo
	def testClaveSinMinus(self):
		seguridad = Seguridad()
		email = "juan123@gmail.com"
		clave= "HOLA1234"
		
		nuevoUsuario = seguridad.registrarUsuario(email, clave, clave)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 0)
		
	#Caso 15 malicioso registro
	#La primera vez que se ejecuto no fallo
	def testCorreoRepetido(self):
		seguridad = Seguridad()
		email = "elvin@gmail.com"
		clave1 = "ho1aCOMOesta"
		clave2 = "0traCosa"
		nuevoUsuario1 = seguridad.registrarUsuario(email, clave1, clave1)

		nuevoUsuario2 = seguridad.registrarUsuario(email, clave2, clave2)

		assert (nuevoUsuario1[0] == 1 and nuevoUsuario1[1] == 1 and
				nuevoUsuario2[0] == 0 and nuevoUsuario2[1] == -1)

	#Caso 16 malicioso registro
	#La primera vez que se ejecuto no fallo
	def testClavesDistintas(self):
		seguridad = Seguridad()
		email = "sandra@gmail.com"
		clave1 = "prueba12A"
		clave2 = "prueba21A"
		nuevoUsuario = seguridad.registrarUsuario(email, clave1, clave2)
		
		assert (nuevoUsuario[0] == -1 and nuevoUsuario[1] == 0)
		
	#Caso 17 malicioso ingreso
	#La primera vez que se ejecuto no fallo
	def testNoRegistrado(self):
		seguridad = Seguridad()
		email = "roxanne@gmail.com"
		clave = "laClave123"

		nuevoIngreso = seguridad.IngresarUsuario(email, clave)
		
		assert (nuevoIngreso[0] == 0)
		
	#Caso 18 malicioso ingreso
	#La primera vez que se ejecuto no fallo
	def testIngresoClaveIncorrecta(self):
		seguridad = Seguridad()
		email = "alex@gmail.com"
		clave1 = "hola120LA"
		clave2 = "holA12345"
		
		nuevoUsuario = seguridad.registrarUsuario(email, clave1, clave1)
		nuevoIngreso = seguridad.IngresarUsuario(email, clave2)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 1 and
				nuevoIngreso[0] == 0)
		
	#Caso 18 esquina superior de clave ingreso
	#La primera vez que se ejecuto no fallo
	def testIngresoClaveInvalida(self):
		seguridad = Seguridad()
		email = "alex@gmail.com"
		clave1 = "hola120LA"
		clave2 = "holA-345"
		
		nuevoUsuario = seguridad.registrarUsuario(email, clave1, clave1)
		nuevoIngreso = seguridad.IngresarUsuario(email, clave2)
		
		assert (nuevoUsuario[0] == 1 and nuevoUsuario[1] == 1 and
				nuevoIngreso[0] == 0)
		
	#Caso 20 esquina superior ingreso
	#La primera vez que se ejecuto no fallo
	def testIngresoCorreoYClaveCaractesEsp(self):
		seguridad = Seguridad()
		email = "aur%a@hotmailcom"
		clave = "hola-hola"
		nuevoIngreso = seguridad.IngresarUsuario(email, clave)
		
		assert (nuevoIngreso[0] == 0)	

if __name__ == "__main__":  
	unittest.main()   