from cryptography.fernet import Fernet

f_key = Fernet.generate_key()
print("KEY: " + str(f_key))
f_enc = Fernet(f_key)

enc_string = f_enc.encrypt(b"Password_2_be_kept_secret_!")

print("ENCRYPTED PASSWORD: " + str(enc_string))
print("DECRYPTED PASSWORD: " + str(f_enc.decrypt(enc_string)))
f
