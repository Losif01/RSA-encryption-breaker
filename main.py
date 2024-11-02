from RSA import RSA 

rsa = RSA(61, 53)
ciphertext = rsa.encrypt("HELLO")
decrypted_text = rsa.decrypt(ciphertext)
print("Decrypted Text:", decrypted_text)
