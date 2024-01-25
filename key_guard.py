import customtkinter
from tkinter import *
import random
import pyperclip
from CTkMessagebox import CTkMessagebox
import json
from settings import *
from encryption import encrypt_file
from decryption import decrypt_file


# incase used on linux or mac systems, it will use system title bar color
try:
    from ctypes import windll, byref, sizeof, c_int
except:
    pass


app = customtkinter.CTk()


def generate_password():
    """generates a random password, by using all the letters, symbols and numbers available; max: 18 characters"""

    new_random_letters = random.randint(8, 10)
    new_random_numbers = random.randint(2, 4)
    new_random_symbols = random.randint(2, 4)

    password_letters = [random.choice(LETTERS)
                        for _ in range(new_random_letters)]
    password_numbers = [random.choice(NUMBERS)
                        for _ in range(new_random_numbers)]
    password_symbols = [random.choice(SYMBOLS)
                        for _ in range(new_random_symbols)]

    password_list = (password_letters + password_numbers + password_symbols)

    random.shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save_details():
    """saves the details entered in the entry boxes into a json file"""
    decrypt_file()
    website = web_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {website: {
        "email": email,
        "password": password,
    }}

    # write to json file or create if not existent
    if len(website) == 0 or len(password) == 0:
        info_message()
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
        except FileNotFoundError or FileExistsError:
            with open("data.json", "w") as data_file:
                json.dump(new_data, data_file, indent=4)
                ok_message()

        else:
            data.update(new_data)

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
                ok_message()
        finally:
            web_entry.delete(0, END)
            password_entry.delete(0, END)
            encrypt_file()


def delete_details():
    """deletes website/app information from the json file"""
    decrypt_file()
    website = web_entry.get()

    if len(website) == 0:
        info_message()
    else:
        try:
            with open("data.json", "r") as data_file:
                data = json.load(data_file)
            if website in data:
                del data[website]
                delete_message()
            else:
                error_message()

            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            web_entry.delete(0, END)
            encrypt_file()


def search_details():
    """searches for the details in the json file, if found will return a message box with details"""
    website = web_entry.get()

    if len(website) == 0:
        info_message()
    else:
        try:
            decrypt_file()
            with open("data.json", "r") as data_file:

                data = json.load(data_file)
            encrypt_file()

        except FileNotFoundError:
            error_message()
        else:
            if website in data:
                email = data[website]["email"]
                password = data[website]["password"]

                CTkMessagebox(title=f"{website} details found", message=f"email: {email} \npassword: {password}",
                              icon="imgs/message/check.png", button_color=DARK, button_hover_color=HOVER_COLOR, font=("Cascadia Code", 15, ),
                              fade_in_duration=0.1, corner_radius=20, bg_color=DARK, fg_color=DARK, text_color=WHITE)
            else:
                error_message()


def view_json_details():
    """view the json file in a new window"""
    with open("data.json", "r") as data_file:
        decrypt_file()
        data = json.load(data_file)

    NewWindow = Toplevel(app, background=DARK)
    NewWindow.title("Websites Details")
    NewWindow.iconbitmap("imgs/logo_light.ico")
    NewWindow.geometry("1000x1000")
    view_label = customtkinter.CTkTextbox(NewWindow, font=(
        "Cascadia Code", 20), width=600, height=600, wrap="word", border_spacing=5, fg_color=DARK, text_color=WHITE)
    view_label.insert("0.0", data)
    view_label.grid(row=2, column=0, pady=50,)
    view_label.configure(state="disabled")

    # making title bar consistent
    HWND = windll.user32.GetParent(NewWindow.winfo_id())
    title_bar_color = 0x00C7E8CA
    windll.dwmapi.DwmSetWindowAttribute(
        HWND, 35, byref(c_int(title_bar_color)), sizeof(c_int))
    encrypt_file()


# -----------------UI SETUP-----------------
app.title("Key Guard")
app.config(bg=DARK, padx=100, pady=50)
app.iconbitmap("imgs/logo_light.ico")
app.resizable(False, False)


# changes the title bar color by accessing windows properties.
try:
    HWND = windll.user32.GetParent(app.winfo_id())
    title_bar_color = 0x00C7E8CA
    windll.dwmapi.DwmSetWindowAttribute(
        HWND, 35, byref(c_int(title_bar_color)), sizeof(c_int))
except:
    pass
def place_logo(): 
    canvas = Canvas(width=200, height=200, highlightthickness=0, bg=DARK)
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(column=1, row=0, pady=50,)



logo_img = PhotoImage(file="imgs/logo_light.png", master=app, )
logo_label = Label(app, image=logo_img, bg=DARK,)
place_logo()


# labels
web_label = customtkinter.CTkLabel(
    app, text="Website", font=("Cascadia Code", 22, ), bg_color=DARK, text_color=WHITE)
web_label.grid(row=1, column=0, sticky="w")

email_label = customtkinter.CTkLabel(
    app, text="Email", font=("Cascadia Code", 22, ), bg_color=DARK, text_color=WHITE)
email_label.grid(row=2, column=0, sticky="w")

password_label = customtkinter.CTkLabel(
    app, text="Password", font=("Cascadia Code", 22, ), bg_color=DARK, text_color=WHITE)
password_label.grid(row=3, column=0, sticky="w")


# entry boxes
web_entry = customtkinter.CTkEntry(
    app, width=200, font=(FONT["font"], FONT["small"]), border_color=WHITE, fg_color=DARK, bg_color=DARK, corner_radius=12, text_color=WHITE)
web_entry.grid(row=1, column=1, columnspan=2, pady=20, padx=10)

email_entry = customtkinter.CTkEntry(
    app, width=200, font=(FONT["font"], FONT["small"]), border_color=WHITE, fg_color=DARK, bg_color=DARK, placeholder_text="example@gmail.com",
    corner_radius=12, placeholder_text_color=WHITE, text_color=WHITE)
email_entry.grid(row=2, column=1, columnspan=2, pady=20, padx=10)

password_entry = customtkinter.CTkEntry(
    app, width=200, font=(FONT["font"], FONT["small"],), border_color=WHITE, fg_color=DARK, bg_color=DARK, corner_radius=12, text_color=WHITE)
password_entry.grid(row=3, column=1, columnspan=2, pady=20, padx=15)


# error and info management ui
def info_message():

    CTkMessagebox(title=CODES["info"], message="Please check all fields are complete",
                  icon="imgs/message/warning.png", button_color=DARK, button_hover_color=HOVER_COLOR, font=("Cascadia Code", 15),
                  fade_in_duration=0.05, corner_radius=20, bg_color=DARK, fg_color=DARK, text_color=WHITE, )


def error_message():
    CTkMessagebox(title=CODES[400], message="Details not found",
                  icon="imgs/message/wrong.png", button_color=DARK, button_hover_color=HOVER_COLOR, font=("Cascadia Code", 15),
                  fade_in_duration=0.05, corner_radius=20, bg_color=DARK, fg_color=DARK, text_color=WHITE)


def ok_message():
    CTkMessagebox(title=CODES[200], message="Details added successfully",
                  icon="imgs/message/check.png", button_color=DARK, button_hover_color=HOVER_COLOR, font=("Cascadia Code", 15),
                  fade_in_duration=0.05, corner_radius=20, bg_color=DARK, fg_color=DARK, text_color=WHITE)


def delete_message():
    CTkMessagebox(title=CODES[200], message="Details deleted successfully",
                  icon="imgs/message/check.png", button_color=DARK, button_hover_color=HOVER_COLOR, font=("Cascadia Code", 15),
                  fade_in_duration=0.05, corner_radius=20, bg_color=DARK, fg_color=DARK, text_color=WHITE)



# buttons
delete_button = customtkinter.CTkButton(
    app, text="", hover=True, bg_color=DARK, fg_color=DARK, image=delete_button_img, width=80, corner_radius=10)
delete_button.configure(hover_color=HOVER_COLOR, command=delete_details)
delete_button.grid(column=0, row=4, pady=30,)

save_button = customtkinter.CTkButton(
    app, text="", hover=True, bg_color=DARK, fg_color=DARK, image=save_button_img, width=80, corner_radius=10)
save_button.configure(hover_color=HOVER_COLOR, command=save_details)
save_button.grid(column=1, row=4, pady=30)

search_button = customtkinter.CTkButton(
    app, text="", hover=True, bg_color=DARK, fg_color=DARK, image=search_button_img, width=80, corner_radius=10)
search_button.configure(hover_color=HOVER_COLOR, command=search_details)
search_button.grid(column=3, row=1,)

generate_password_button = customtkinter.CTkButton(
    app, text="", hover=True, bg_color=DARK, fg_color=DARK, image=generate_password_img, width=100, corner_radius=10)
generate_password_button.configure(
    hover_color=HOVER_COLOR, command=generate_password)
generate_password_button.grid(column=3, row=3, padx=10)

view_json = customtkinter.CTkButton(
    app, text="", hover=True, bg_color=DARK, fg_color=DARK, image=view_json_img, width=80, corner_radius=10,)
view_json.configure(hover_color=HOVER_COLOR, command=view_json_details)
view_json.grid(column=3, row=4,)




if __name__ == "__main__":
    app.mainloop()
