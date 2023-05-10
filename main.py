import customtkinter 
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
from CTkMessagebox import CTkMessagebox

app = customtkinter.CTk()

# ---------------------------- CONSTANTS  ------------------------------- #

TEKHELET= "#3F3579ff"
PLATINUM= "#E0E0E0ff"
BLACK= "#242424"
SLATE_PINK = "#BFACE2"
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


    if len(website) == 0 or len(password) ==0:
        CTkMessagebox(title="oops", message="please complete all fields", icon="warning")
    else:
        is_ok = CTkMessagebox(title=website, message=f"these are the details entered:\nEmail: {email} \nPassword: {password} \nis it okay to save? ", icon="info")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"website: {website}  | email: {email} | password: {password}")
                file.write("\n")
                file.close()


                web_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)    

        




# ---------------------------- UI SETUP ------------------------------- #
customtkinter.set_appearance_mode("dark")  # Modes: "System" (standard), "Dark", "Light"
customtkinter.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"


app.title("Password Manager")
app.config(padx=50, pady=50,)

lock_Img = PhotoImage(file="logo.png")


canvas = Canvas(width=200, height=200, highlightthickness=0,bg=BLACK )
canvas.create_image(100, 100, image=lock_Img)
canvas.grid(column=1, row=0)

# label and entry widgets
web_label = customtkinter.CTkLabel(app,text="Website")
web_label.grid(row=1, column=0, padx=10)


web_entry = customtkinter.CTkEntry(app, width=200,)
web_entry.grid(row=1,column=1, columnspan=2,)
web_entry.focus()

email_label = customtkinter.CTkLabel(app, text="Email/Username")
email_label.grid(row=2, column=0, padx=5  )

email_entry = customtkinter.CTkEntry(app,width=200)
email_entry.grid(column=1, row=2, columnspan=2, padx=5, pady=8)
email_entry.insert(0,string="example@gmail.com")




password_label = customtkinter.CTkLabel(app, text="Password")
password_label.grid(row=3, column=0)

password_entry = customtkinter.CTkEntry(app, width=200)
password_entry.grid(row=3, column=1, padx=5)

# generate password and add button

generate_button = customtkinter.CTkButton(app,text="Generate password", hover=True, bg_color=BLACK, fg_color=SLATE_PINK,)
generate_button.configure(hover_color=(SLATE_BLUE), cursor="hand2", command=generate_password )
generate_button.grid(column=3,row=3, padx=5)

add_button = customtkinter.CTkButton(app, text="Add", hover=True,bg_color=BLACK, fg_color=SLATE_PINK, width=200)
add_button.configure( hover_color=(SLATE_BLUE), cursor="hand2", command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=10)







app.mainloop()
