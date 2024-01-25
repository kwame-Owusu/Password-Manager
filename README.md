# Key Guard Program
it is a program written in  python, the main goal is to be able to get details from the user like website/app name, email associated with the website/app and add a password to it(can also be generated by the program) after that it is saved in a Json file where the user can either choose to view, delete or overwrite the data.


## Libraries and images credit
* [Customtkinter](https://customtkinter.tomschimansky.com/) - Modern version of tkinter with more customization but also inherits main functions from tkinter.
* [CTKmessagebox](https://github.com/Akascape/CTkMessagebox) - Modern version of message pop up for customtkinter integration and homogenous ui.
* [Cryptography(Fernet)](https://cryptography.io/en/latest/) - Library used for the encryption and decryption of the json file.
* [Pyperclip](https://pypi.org/project/pyperclip/) - Library used to copy generated password to clipboard.
* [Images credit](https://icons8.com/) - the images for the icons were taken from Icons8 website.


## UI colour palette

![Key Guard Palette](https://olympuss.ntu.ac.uk/storage/user/1587/files/d056a193-f9c2-4ce2-b3c0-d9ef6aee51b5)

## Project structure
```
$PROJECT_ROOT
│   # Images used for the icons
├── imgs
│   # Python files
├── Encryption.py
├── Decryption.py
├── Key_guard.py
├── Settings.py
│   # Key generation from Fernet
├── secret_key.key
│   # Json file
└── Data.json
```

## Video for how it works
https://olympuss.ntu.ac.uk/storage/user/1587/files/69b2fe6b-56fe-4235-840f-0ce973173d3f




## Limitations
this program is a simple program and though the encryption process is good, its serves only this purpose for such simple program, thats why i used fernet, I might package the program later.


