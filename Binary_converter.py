class Binary_Converter:

	def __init__(self, binary):
		self.binary = binary

	def binary_to_hex(self):

		def looping_func(string):
			decimal = 0
			idx = 0
			while idx < len(string):
				if string[idx] != '0':
					decimal = decimal + (2 **idx)
				else:
					decimal = decimal
				idx = idx + 1
			return decimal

		binary = self.binary
		lista_hex = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]

		if len(binary) < 9:
			if len(binary) < 4:
				rev_binary = ''.join(reversed(binary))
				while len(rev_binary) < 4:
					rev_binary = rev_binary + '0'

				deci_1 = looping_func(rev_binary)
				hex_final = lista_hex[deci_1]

			elif len(binary) == 4:
				final_binary = "".join(reversed(binary))

				deci_1 = looping_func(final_binary)
				hex_final = lista_hex[deci_1]

			elif len(binary) < 9:
				rev_binary = ''.join(reversed(binary))
				while len(rev_binary) < 8:
					rev_binary = rev_binary + '0'

				part_1 = rev_binary[0:4]
				part_2 = rev_binary[4:8]

				deci_1 = looping_func(part_1)
				deci_2 = looping_func(part_2)

				hex_1 = lista_hex[deci_1]
				hex_2 = lista_hex[deci_2]
				
				if hex_1 == '0':
					hex_final = hex_2
				elif hex_2 == '0':
					hex_final = hex_1
				else:
					hex_final = hex_2 + hex_1

			hex_value = "The hex value of the binary {0} is: {1}".format(binary,hex_final)

		else:
			hex_value = "You should digit a binary with maximum lenght = 8"
		return hex_value

	def binary_to_deci(self):
		binary = self.binary
		rev_binary = ''.join(reversed(binary))

		idx = 0
		decimal = 0
		while idx < len(rev_binary):
			if rev_binary[idx] != '0':
				decimal = decimal + (2**idx)
			else:
				decimal = decimal
			idx = idx + 1

		deci_value = "The decimal value of the binary {0} is: {1} ".format(binary,decimal)
		return deci_value