from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
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
    new_data={web_input.get():{
        "email":email_input.get(),
        'password':password_input.get()
        }
    }
    if len(web_input.get())==0 or len(password_input.get()) ==0:
        messagebox.showinfo(title='Oops',message='Please make sure you have not left any fields empty.')
    else:
        is_ok = messagebox.askokcancel(title=web_input.get(),message=f"These are the details entered: \nEmail:{email_input.get()}\nPassword:{password_input.get()}\nIs it ok to save?")
        if is_ok:
            try:
                with open('data.json','r') as data:
                    data_j = json.load(data)
            except FileNotFoundError:
                with open('data.json', 'w') as data:
                    json.dump(new_data, data, indent=4)
            else:
                data_j.update(new_data)
                with open('data.json', 'w') as data:
                    json.dump(data_j,data,indent=4)
            finally:
                web_input.delete(0,END)
                password_input.delete(0,END)


def find_password():
    website = web_input.get()
    try:
        with open('data.json') as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message=f"No Data File Found")
    else:
        if website in data:
            email=data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website,message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showinfo(title='Error', message=f"No Details for {website} exists.")


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


web_input = Entry(width=21)
web_input.grid(row=1,column=1)
email_input = Entry(width=21)
email_input.grid(row=2,column=1)
email_input.insert(0,'daivik@gmail.com')
password_input = Entry(width=21)
password_input.grid(row=3,column=1)

search_btn = Button(text='Search',width='13',command=find_password)
search_btn.grid(row='1',column='2')
gen_pass = Button(text='Generate Password',command=generate_password)
gen_pass.grid(row=3,column=2)
add = Button(text='Add',width=36, command=save)
add.grid(row=4,column=1,columnspan=2)
window.mainloop()