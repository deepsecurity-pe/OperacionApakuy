import random

def generarDNI(cantidad):
	dni_true = []
	numberKeys = [6, 7, 8, 9, 0, 1, 1, 2, 3, 4, 5]

	while True:
		total = 0
		# lista dni 
		dni = [0,0,0,0,0,0,0,0]

		#lista numeros multiplicar
		num_const = [3,2,7,6,5,4,3,2]	
		
		#generando dni aleatorios
		for i in range(8):
			dni[i] = random.randrange(8)

		#haciendo la operacion multiplicar dni * numeros constantes 
		for i in range(8):
			total = total + (dni[i] * num_const[i])

		keyIndex = 11 - (total % 11)

		if keyIndex == 11:
			keyIndex = 0

		resultado = keyIndex + 1

		dni = ''.join(map(str, dni))

		if dni not in dni_true:
			dni_true.append(dni)
			if len(dni_true) >= cantidad :
				break

	return dni_true

dni_validos = generarDNI(1000)

for i in dni_validos:
	print(i)
