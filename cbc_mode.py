import os
from aes import AES



def bytes_xor(byte_1, byte_2):
	return bytes([a ^ b for a, b in zip(byte_1, byte_2)])

def split_blocks(message, block_size=16):
    return [message[i:i+16] for i in range(0, len(message), block_size)]


def pad(plaintext):
	padding_len = 16 - (len(plaintext) % 16)
	padding = bytes([padding_len] * padding_len)
	return plaintext + padding

def unpad(plaintext):
	padding_len = plaintext[-1]
	message = plaintext[:-padding_len]
	padding = plaintext[-padding_len:]
	return message

def cbc_encrypted(key, message, iv, file_name):
	aes_object = AES(key)
	message = pad(message)
	iv_next = iv
	with open(file_name, 'ab') as fo_enc:
		fo_enc.write(iv)
		for block in split_blocks(message):
			iv_x = bytes_xor(block, iv_next)
			cyphertext = aes_object.encrypt(iv_x)
			fo_enc.write(cyphertext)
			iv_next = cyphertext
	print("File was encrpyted succesfully by CBC MODE")

def cbc_decrypted(key, cyphertext, file_name):
	aes_object = AES(key)
	iv = cyphertext[:16]
	iv_previous = iv
	blocks_arr = split_blocks(cyphertext[16:])
	with open(file_name, 'ab') as fo_dec:
		for block in blocks_arr[:-1]:
			iv_x = aes_object.decrypt(block)
			plaintext = bytes_xor(iv_x, iv_previous)
			fo_dec.write(plaintext)
			iv_previous = block
		iv_x = aes_object.decrypt(blocks_arr[-1])
		plaintext = bytes_xor(iv_x, iv_previous)
		fo_dec.write(unpad(plaintext))
	print("File was decrypted successfully by CBC MODE")