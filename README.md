# The second program exercise: Usage of block cyphers

## Description:

The project allows to encrypt and decrypt any type of file by AES Algorithm with CBC mode or CTR mode choices.
The file key.txt contains the key which be used for encrypting and decrypting files by AES. This file must be kept secrete.
The key size in this project has length 16 bytes (128 bits).

## The project includes 4 files:

1. aes.py contains AES class to encrypt and decrypt file by AES without any mode
2. cbc_mode.py contains functions to encrypt and decrypt file by AES with CBC mode
3. ctr_mode.py contains functions to encrypt and decrypt file by AES with CTR mode
4. main.py contains main function

## Requirement:

Python language with version 3.x

## Usage:

From terminal type following command line to run:

```  python3 main.py --type type-crypt --mode mode-to-crypt --file path/to/filename/to/crypt  ```

1. Change "type-crypt" to "encrypt" if you want to encrypt file, else "decrypt" to decrypt file.
2. Change "mode-to-crypt" to "cbc" if you want to do crypt file with mode CBC, else "ctr" is mode CTR.
3. Change "path/to/filename/to/crypt" to file name you want to do crypt

## Comparation time to excute between my project with pycrypto library:

1. My project took 165 seconds to encrypt abc.pptx file (in size 14.3 MB) by AES with CBC mode. The pycrypto library took 0.09 seconds.
2. My project took 220 seconds to decrypt the above file by AES with CBC mode. The pycrypto library took 0.084 seconds.
3. My project took 166 seconds to encrypt abc.pptx file (in size 14.3 MB) by AES with CTR mode. The pycrypto library took 0.063 seconds.
4. My project took 164 seconds to decrypt the above file by AES with CTR mode. The pycrypto library took 0.062 seconds.

==> My project excuted slower than the pycrypto library very much.

## Copyright by Nguyen Tien Anh
