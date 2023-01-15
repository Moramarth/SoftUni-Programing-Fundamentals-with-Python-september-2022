plain_text = input()

encrypted_text = ""

for char in plain_text:
    encrypted_text += chr(ord(char) + 3)

print(encrypted_text)
