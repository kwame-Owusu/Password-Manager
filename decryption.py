from cryptography.fernet import Fernet

def decrypt_file():
  # read the key from the file
  key = ""
  with open("secret_key.key", "rb") as key_file:
    key = key_file.read()

  # read the data from the encrypted file
  encrypted_data = ""
  with open("data.json", "rb") as data_file:
    encrypted_data = data_file.read()

  # decrypt the file 
  fernet_key = Fernet(key)
  decrypted_data = fernet_key.decrypt(encrypted_data)


  # save the decrypted file to the same file
  with open("data.json", "wb") as data_file:
    data_file.write(decrypted_data)

