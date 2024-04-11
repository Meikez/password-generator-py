from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_letters = [random.choice(letters) for _ in range(nr_letters)]
    password_symbols = [random.choice(symbols) for _ in range(nr_letters)]
    password_numbers = [random.choice(numbers) for _ in range(nr_letters)]

    password_list = password_letters + password_symbols + password_numbers

    random.shuffle(password_list)

    password = "".join(password_list)
    password_input.insert(0,password)
    pyperclip.copy(password)
# password_list = []
#
# for char in range(nr_letters):
#   password_list.append(random.choice(letters))
#
# for char in range(nr_symbols):
#   password_list += random.choice(symbols)
#
# for char in range(nr_numbers):
#   password_list += random.choice(numbers)
#
# random.shuffle(password_list)

# password = ""
# for char in password_list:
#   password += char



# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_credential():
    website = website_input.get()
    username = username_input.get()
    password = password_input.get()

    new_data = {
        website: {
            "email": username,
            "password": password,

        }
    }

    if website=="" or username =="" or password=="":
        messagebox.showinfo(title="Warning", message="Please make sure you haven't left any fields empty.")
    else:
        confirmated= messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {username} \nPassword: {password} \nIs it ok to save?")

        if confirmated:
            try:
                with open('credentials.json', mode="r") as file:
                    # Reading current data
                    data = json.load(file)
                    # Updating the data
                    data.update(new_data)
            except FileNotFoundError as error:
                with open("credentials.json", "w") as file_write:
                    print(f"we are at exception {error}")
                    json.dump(new_data, file_write, indent=4)
                    # Saving the update data

            else:

                with open("credentials.json", "w") as file_update:
                    print(f"we are at else exception")
                    json.dump(data, file_update, indent=4)
            finally:
                    website_input.delete(0, END)
                    password_input.delete(0, END)


def search_password():
    try:
        with open("credentials.json", "r") as password_file:
            data = json.load(password_file)
            password_find = {}
            if website_input.get() in data:
                password_find = data[website_input.get()]
                messagebox.showinfo(title="Credentials", message=f"username: {password_find["email"]} \n password: {password_find["password"]}")
                print(password_find)
            else:
                messagebox.showinfo(title="warning", message="Website not found")

    except FileNotFoundError:
        messagebox.showinfo(title="warning", message="File not found")


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(pady=40,padx=40)

canvas = Canvas(width=200, height=200)
password_img = PhotoImage(file="lock.png", )
scale= int(250/450)

password_img = password_img.subsample(2,2)
canvas.create_image(100,100, image=password_img)
canvas.grid(column=1,row=0)

#Labels

website_label = Label(text="Website:", )
website_label.grid(column=0,row=1)
website_label.focus()

username_label = Label(text="Email/Username:",)
username_label.grid(column=0,row=2)


password_label = Label(text="Password:", )
password_label.grid(column=0,row=3)

# Inputs

website_input = Entry(width=35)
website_input.grid(column=1,row=1, columnspan=1)

username_input = Entry(width=35)
username_input.grid(column=1,row=2, columnspan=1)
username_input.insert(0,"mati.lealtech@gmail.com")

password_input = Entry(width=20, )
password_input.grid(column=1,row=3, )

generate_password_button = Button(text="Generate password", command=password_generator)
generate_password_button.grid(column=2,row=3)

add_button = Button(text="add",width=36, command=save_credential)
add_button.grid(column=1,row=4,columnspan=2)

search_button = Button(text="Search", command=search_password )
search_button.grid(column=2,row=1)

window.mainloop()