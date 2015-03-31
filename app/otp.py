from random import choice
import binascii
import pprint

def encrypt(message):
	message = convert_to_binary(message)
	key = generate_random_key(message)

	cipher = ""

	for i in range(len(message)):
		if message[i] == key[i]:
			cipher += str(0)
		else:
			cipher += str(1)

	return {'cipher': cipher, 'message': message, 'key': key}

def convert_to_binary(message):
	return bin(int(binascii.hexlify(message), 16))

def generate_random_key(binary_message):
	return ''.join(choice(('0','1')) for _ in range(len(binary_message)))
