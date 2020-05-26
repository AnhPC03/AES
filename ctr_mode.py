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



def ctr_encrypted(key, message, iv, file_name):
	aes_object = AES(key)
	message = pad(message)
	count = 0;
	with open(file_name, 'ab') as fo_enc:
		fo_enc.write(iv)
		for block in split_blocks(message):
			iv_count = bytes_xor(iv, count.to_bytes(16, 'big'))
			iv_x = aes_object.encrypt(iv_count)
			cyphertext = bytes_xor(iv_x, block)
			fo_enc.write(cyphertext)
			count += 1
	print("File was encrypted successfully by CTR MODE")

def ctr_decrypted(key, cyphertext, file_name):
	aes_object = AES(key)
	iv = cyphertext[:16]
	count = 0
	blocks_arr = split_blocks(cyphertext[16:])
	with open(file_name, 'ab') as fo_dec:
		for block in blocks_arr[:-1]:
			iv_count = bytes_xor(iv, count.to_bytes(16, 'big'))
			iv_x = aes_object.encrypt(iv_count)
			plaintext = bytes_xor(iv_x, block)
			fo_dec.write(plaintext)
			count += 1
		iv_count =bytes_xor(iv, count.to_bytes(16, 'big'))
		iv_x = aes_object.encrypt(iv_count)
		plaintext = bytes_xor(iv_x, blocks_arr[-1])
		fo_dec.write(unpad(plaintext))
	print("File was decrypted successfully by CTR MODE")