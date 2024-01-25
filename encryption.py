from cryptography.fernet import Fernet

def encrypt_file():
  # read key from file
  key = ""
  with open("secret_key.key", "rb") as key_file:
    key = key_file.read()

  # read data from file
  data = ""
  with open("data.json", "rb") as data_file:
      data = data_file.read()
  
  # encrypt data
  fernet_key = Fernet(key)
  encrypted_data = fernet_key.encrypt(data)


  # save encrypted data in the file
  with open("data.json", "wb") as data_file:
    data_file.write(encrypted_data)
  

