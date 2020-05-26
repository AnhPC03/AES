import argparse
import os, timeit

from cbc_mode import *
from ctr_mode import *


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("--type", type=str, help="encrypt or decrypt")
	parser.add_argument("--mode", type=str, help="cbc or ctr")
	parser.add_argument("--file", type=str, help="name of file want to encrypt or decrypt")

	opt = parser.parse_args()

	file_name = opt.file
	mode = opt.mode
	type_aim = opt.type

	with open('key.txt', 'rb') as fo_key:
		key = fo_key.read()
	iv = os.urandom(16)

	start = timeit.default_timer()

	if type_aim == "encrypt":
		if mode == "cbc":
			with open(file_name, 'rb') as fo_plaintext:
				message = fo_plaintext.read()
			cbc_encrypted(key, message, iv, f'{file_name}.enc')
			os.remove(file_name)
		elif mode == "ctr":
			with open(file_name, 'rb') as fo_plaintext:
				message = fo_plaintext.read()
			ctr_encrypted(key, message, iv, f'{file_name}.enc')
			os.remove(file_name)
	elif type_aim == "decrypt":
		initial_file_name = os.path.splitext(file_name)[0]
		if mode == "cbc":
			with open(file_name, 'rb') as fo_cypher_read:
				text_cypher_1 = fo_cypher_read.read()
			cbc_decrypted(key, text_cypher_1, f'{initial_file_name}')
			os.remove(file_name)
		elif mode == "ctr":
			with open(file_name, 'rb') as fo_cypher_read:
				text_cypher_1 = fo_cypher_read.read()
			ctr_decrypted(key, text_cypher_1, f'{initial_file_name}')
			os.remove(file_name)


	stop = timeit.default_timer()
	print(f'Time to {type_aim} was: {stop - start} seconds')


if __name__ == "__main__":
	main()