from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password=''
    password_input.delete(0,END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password += "".join(password_list)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    if len(web_input.get())==0 or len(password_input.get()) ==0:
        messagebox.showinfo(title='Oops',message='Please make sure you have not left any fields empty.')
    else:
        is_ok = messagebox.askokcancel(title=web_input.get(),message=f"These are the details entered: \nEmail:{email_input.get()}\nPassword:{password_input.get()}\nIs it ok to save?")
        if is_ok:
            with open('data.txt','a') as data:
                data.write(f"{web_input.get()} | {email_input.get()} | {password_input.get()}\n")
            web_input.delete(0,END)
            password_input.delete(0,END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)
canvas = Canvas(height=200,width=200)
logo_img = PhotoImage(file='logo.png')
canvas.create_image(100,100,image=logo_img)
canvas.grid(row=0,column=1)
web_label = Label(text='Website:')
web_label.grid(row=1,column=0)
email_label = Label(text='Email/Username:')
email_label.grid(row=2,column=0)
password_label = Label(text='Password:')
password_label.grid(row=3,column=0)


web_input = Entry(width=35)
web_input.grid(row=1,column=1,columnspan=2)
email_input = Entry(width=35)
email_input.grid(row=2,column=1,columnspan=2)
email_input.insert(0,'daivik@gmail.com')
password_input = Entry(width=35)
password_input.grid(row=3,column=1,columnspan=2)


gen_pass = Button(text='Generate Password',width=30,command=generate_password)
gen_pass.grid(row=4,column=1,columnspan=2)
add = Button(text='Add',width=30, command=save)
add.grid(row=5,column=1,columnspan=2)
window.mainloop()