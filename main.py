from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def generate_password():
    #Password Generator Project
    import random
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    # nr_letters = random.randint(8, 10)
    # nr_symbols = random.randint(2, 4)
    # nr_numbers = random.randint(2, 4)

    password_list = []
    password_list = [random.choice(letters) for _ in range(randint(8, 10))]
    password_list += [random.choice(numbers) for _ in range(randint(2, 4))]
    password_list += [random.choice(symbols) for _ in range(randint(2, 4))]
    # for char in range(nr_letters):
    #   password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #   password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #   password_list += random.choice(numbers)

    shuffle(password_list)

    password = "".join(password_list)
    # password = ""
    # for char in password_list:
    #   password += char

    input_password.delete(0,END)
    input_password.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if input_password.get() == "" or input_website.get() == "" or input_username.get() == "":
        messagebox.showinfo(title="Oops",message="Please don't leave any fields empty!")
        return
    answer = messagebox.askokcancel(title="Save Password",message=f"Will save password {input_password.get()} for website {input_website.get()} and username {input_username.get()}. Is it Ok to Save?")
    if answer:
        new_data = {
            input_website.get(): {
                "email": input_username.get(),
                "password": input_password.get()
            }
        }
#my_passwords.write(f"{input_website.get()} | {input_username.get()} | {input_password.get()}\n")
        try:
            print("loading data")
            with open("data.json", "r") as my_passwords:
                data = json.load(my_passwords)
        except FileNotFoundError as error:
            print(f"creating new data {error}")
            with open("data.json", "w") as my_passwords:
                json.dump(new_data,my_passwords,indent=4)
        else:
            print("updating data")
            data.update(new_data)
            with open("data.json","w") as my_passwords:
                json.dump(data, my_passwords, indent=4)


        input_website.delete(0,END)
        input_password.delete(0,END)
        messagebox.showinfo(title="Password Saved",message="Password Saved Successfully!")


def find_password():
    website = input_website.get()
    try:
        with open("data.json","r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError as error:
        messagebox.showinfo(title="Error",message=f"No Data File Found! {error}")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title="Error",message=f"No details for {website} exists!")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1,row=0,columnspan=3)
#columnspan

website_label = Label(anchor="e",text="WebSite:")
website_label.grid(column=0,row=1)

input_website = Entry(width=21)
input_website.focus()
input_website.grid(column=1,row=1)
search_button = Button(width=21,text="Search",command=find_password)
search_button.grid(column=2,row=1)


username_label = Label(anchor="e",text="Email/Username:")
username_label.grid(column=0,row=2)

input_username = Entry(width=47)
input_username.insert(0,"bcarvalho.osi@gmail.com")
input_username.grid(column=1,row=2,columnspan=2)

password_label = Label(anchor="e",text="Password:")
password_label.grid(column=0,row=3)

input_password = Entry(width=21)
input_password.grid(column=1,row=3)

generate_button = Button(width=21,text="Generate Password",command=generate_password)
generate_button.grid(column=2,row=3)

add_button = Button(width=40,text="Add",command=save)
add_button.grid(column=1,row=4,columnspan=2)


window.mainloop()
