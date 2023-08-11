import random
import string

print('Welcome to Your Password Generator')

password_characters = string.ascii_letters + string.digits + string.punctuation
exclude_characters = '<>^'

def generate_password(length):
    return ''.join(random.choice(password_characters)for _ in range(length))
    
password_length = 12
generated_password = generate_password(password_length)
print('Generated Password:', generated_password)