import secrets
import string

length = int(input("Password ki length batayein (e.g., 8): "))

characters = string.ascii_letters + string.digits

password = ''.join(secrets.choice(characters) for _ in range(length))

print("Generated Password:", password)