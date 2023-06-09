import customtkinter 
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
from CTkMessagebox import CTkMessagebox
import json
from PIL import Image



app = customtkinter.CTk()

# ---------------------------- COLOR  CONSTANTS  ------------------------------- #
WHITE = "#EEEEEE"
TEKHELET= "#3F3579ff"
PLATINUM= "#E0E0E0ff"
BLACK= "#242424"
SLATE_PINK = "#BFACE2"
PINK = "#F5C6EC"
SLATE_BLUE ="#6767FF"
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for _ in range(nr_numbers)]
    
    password_list = password_letters + password_symbols + password_numbers

    
    # I used list comprehensions, which made the same thing in less lines of code
    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))

    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)

    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, password)
    # python module that copies  strings to the clipboard, in this case the generated password
    pyperclip.copy(password)
    
        
    




# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = web_entry.get()
    email= email_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "email": email,
        "password": password,
    }}

    if len(website) == 0 or len(password) == 0:
        CTkMessagebox(title="oops", message ="please complete all fields", icon="warning", button_color=SLATE_PINK, button_hover_color=SLATE_BLUE, font=("Fixedsys",15, ))
    else:
        try:
             with open("data.json", "r") as data_file:
             #    reading old data
                data = json.load(data_file)
           
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent= 4)
        else:
            # updating old data with new data
            data.update(new_data)
       
    
            with open("data.json", "w") as data_file:
                # saving updated data
                json.dump(data, data_file, indent=4)
        finally:
                web_entry.delete(0, END)
                password_entry.delete(0, END)    

# ---------------------------- SEARCH FUNCTIONALITY ------------------------------- #
# search for details of a website,
def search():
    website = web_entry.get()
    try:
    
        with open("data.json", "r") as data_file:
        
            data = json.load(data_file)
# catches the error so the app does not crash
    except FileNotFoundError:
            CTkMessagebox(title="Error", message="No Data File Found", icon="warning", button_color=SLATE_PINK, button_hover_color=SLATE_BLUE, font=("Fixedsys",15, ))
# gets the details associated with the website, else shows error if website is not found in json file 
    else:
        if website in data:
                email = data[website]["email"]
                password = data[website]["password"]

                CTkMessagebox(title=f"{website} details found", message=f"email: {email} \npassword: {password}", icon="check", button_color=SLATE_PINK, button_hover_color=SLATE_BLUE, font=("Fixedsys",15, ))
        else:
             CTkMessagebox(title="error", message=f"No details for {website} found", icon="warning", button_color=SLATE_PINK, button_hover_color=SLATE_BLUE, font=("Fixedsys",15, ))




# ---------------------------- UI SETUP ------------------------------- #
customtkinter.set_appearance_mode("dark")  
app.title("Password Manager")
app.config(padx=50, pady=50)
app.iconbitmap("imgs/logo.ico")
app.resizable(False, False)
lock_Img = PhotoImage(file="imgs/logo.png")


canvas = Canvas(width=200, height=200, highlightthickness=0,bg=BLACK )
canvas.create_image(100, 100, image=lock_Img)
canvas.grid(column=1, row=0)

# label and entry widgets
web_label = customtkinter.CTkLabel(app,text="Website")
web_label.grid(row=1, column=0, padx=10)


web_entry = customtkinter.CTkEntry(app, width=200,height=30)
web_entry.grid(row=1,column=1, columnspan=2,)


email_label = customtkinter.CTkLabel(app, text="Email/Username")
email_label.grid(row=2, column=0, padx=5  )

email_entry = customtkinter.CTkEntry(app,width=200, height=30)
email_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=8,)
email_entry.insert(0,string="example@gmail.com")

# images
search_img = customtkinter.CTkImage(light_image=Image.open("imgs/search.png"), dark_image=Image.open("imgs/search.png"), size=(30,30))
add_img = customtkinter.CTkImage(light_image=Image.open("imgs/add.png"), dark_image=Image.open("imgs/add.png"), size=(30,30))
generate_img = customtkinter.CTkImage(light_image=Image.open("imgs/generate.png"), dark_image=Image.open("imgs/generate.png"), size=(35,35))




password_label = customtkinter.CTkLabel(app, text="Password")
password_label.grid(row=3, column=0)

password_entry = customtkinter.CTkEntry(app, width=200, height=30)
password_entry.grid(row=3, column=1, padx=5)
# generate password and add button

generate_button = customtkinter.CTkButton(app,text="", hover=True, bg_color=BLACK, fg_color=BLACK, image=generate_img)
generate_button.configure(hover_color=PINK,command=generate_password )
generate_button.grid(column=3,row=3, padx=5)

add_button = customtkinter.CTkButton(app, text="", hover=True,bg_color=BLACK, fg_color=BLACK, image=add_img )
add_button.configure( hover_color=PINK, command=save)
add_button.grid(column=1, row=4, pady=10)




search_button = customtkinter.CTkButton(app,image=search_img, bg_color=BLACK, fg_color=BLACK)
search_button.configure(text=None,command=search, hover_color=PINK, )
search_button.grid(column=3, row=1)





if __name__ == "__main__":
    app.mainloop()
