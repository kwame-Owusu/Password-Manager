import customtkinter
from PIL import Image
from tkinter import Toplevel, Label


# Colour palette 
DARK = "#94AF9F"
WHITE = "#F4F9F9"
HOVER_COLOR = "#BBD6B8"



# Button images
delete_button_img = customtkinter.CTkImage(light_image=Image.open(
    "imgs/ios_style/delete.png"), dark_image=Image.open("imgs/ios_style/delete.png"), size=(35, 35))

save_button_img = customtkinter.CTkImage(light_image=Image.open(
    "imgs/ios_style/save.png"), dark_image=Image.open("imgs/ios_style/save.png"), size=(35, 35))

search_button_img = customtkinter.CTkImage(light_image=Image.open(
    "imgs/ios_style/search.png"), dark_image=Image.open("imgs/ios_style/search.png"), size=(30, 30))

generate_password_img = customtkinter.CTkImage(light_image=Image.open(
    "imgs/ios_style/gen_password.png"), dark_image=Image.open("imgs/ios_style/gen_password.png"), size=(50, 50))


view_json_img = customtkinter.CTkImage(light_image=Image.open(
    "imgs/ios_style/view_details.png"), dark_image=Image.open("imgs/ios_style/view_details.png"), size=(35, 35))


FONT = {
  "font": "Cascadia Code",
  "small": 15,
  "big" : 30,
  "bold": "bold"
}


# INFO MESSAGE CODES
CODES = {
  200: "OK",
  400: "Not Found",
  "info":"Info",
}


# generate password function letters and symbols
LETTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
            'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
NUMBERS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
SYMBOLS = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


#class to create window.
class NewWindow(Toplevel):
  def __init__(self, master = None):
    super().__init__(master = master)
    self.title("New Window")
    self.geometry("200x200")
    label = Label(self, text ="This is a new Window")
    label.pack()

    

