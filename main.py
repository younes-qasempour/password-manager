from tkinter import *
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

# ---------------------------- SAVE PASSWORD ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(window, width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=1)

#Labels
website_label  = Label(window, text="Website:")
website_label.grid(row=1, column=0)
email_label = Label(window, text="Email/Username:")
email_label.grid(row=2, column=0)
password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

#Enteries
website_entry = Entry(window, width=45)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()
email_entry = Entry(window, width=45)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(END, "DummyEmail@gmail.com")
password_entry = Entry(window, width=27)
password_entry.grid(row=3, column=1)

#Button
generate_password_button = Button(window, text="Generate Password", width=14)
generate_password_button.grid(row=3, column=2)
add_button = Button(window, text="Add", width=38)
add_button.grid(row=4, column=1,columnspan=2)








window.mainloop()