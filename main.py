from tkinter import *
from tkinter import messagebox
from random import randint, choice,shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    # create list comprehension new_list=[new_item for item in list]
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters+password_symbols+password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0,password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data = {
        website: {
            "email":email,
            "password": password,
        }
    }
    if len(website)==0 or len(password)==0:
        messagebox.showerror(title="Oops", message="Please fill out blank")
    else:
        is_ok= messagebox.askokcancel(title=website,message=f"There are the details entered: \nEmail:{email}\n"
                                                     f"Password:{password}\n Is it okay to save?")
        if is_ok:
            try:
                with open("data.json","r") as data_file:
                    # reading old data
                    data= json.load(data_file)
            except FileNotFoundError:
                with open("data.json","w") as data_file:
                    # saving updated data
                    json.dump(new_data,data_file,indent=4)
            else:
                #update old data with new data
                data.update(new_data)
                with open("data.json","w") as data_file:
                    # saving updated data
                    json.dump(data,data_file,indent=4)
            finally:
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)

def find_password():
    

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(pady=20,padx=20)

canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)

website_label = Label(text="Website:")
website_label.grid(row=1,column=0)
email_user_label=Label(text="Email/Username:")
email_user_label.grid(row=2,column=0)
password_label=Label(text="Password:")
password_label.grid(row=3,column=0)

# entries
website_entry = Entry(width=35)
website_entry.grid(row=1,column=1,columnspan=2)
website_entry.focus()
email_entry=Entry(width=35)
email_entry.insert(0,"xxyyzz@gmail.com")
email_entry.grid(row=2, column=1,columnspan=2)
password_entry=Entry(width=26)
password_entry.grid(row=3, column=1)

# Buttons
search_button=Button(text="Search")
search_button.grid(column=2,row=1)
generate_password_button=Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)
add_button = Button(text="Add",width=36,command=save)
add_button.grid(column=1,row=4,columnspan=2)

window.mainloop()


