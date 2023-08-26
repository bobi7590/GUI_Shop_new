import tkinter as tk
from tkinter import messagebox



from service import register_users, login
from products_service import get_prod


def handler():
   messagebox.showerror("Warning", "Username already registered. Try another one.")

def destroy_widgets(window: tk.Tk):
    for widgets in window.winfo_children():
        widgets.destroy()

def clear_text(*text: tk.Entry):
    for box in text:
        box.delete(0,"end")

def render_main_screen(window):
    login_button = tk.Button(
        window,
        text = 'Login',
        bg = 'green',
        width = '20',
        heigh = '3',
        fg = 'white',
        command = lambda: render_login_screen(window)
    ).place(x=250, y=500)

    register_button = tk.Button(
        window,
        text='Register',
        bg='black',
        width='20',
        heigh='3',
        fg='white',
        command =lambda: render_register_screen(window)
    ).place(x=405, y=500)




def render_register_screen(window:tk.Tk):
    destroy_widgets(window)

    username_label = tk.Label(window, text="Enter username").place(x=305, y=300)
    username_text = tk.Entry(window)
    username_text.place(x=400, y=300)

    passowrd_label = tk.Label(window,text = "Enter password").place(x=305,y=320)
    password_text = tk.Entry(window,show = '*')
    password_text.place(x=400, y=320)

    first_name_label = tk.Label(window,text = "Enter first name").place(x=305,y=340)
    first_name = tk.Entry(window)
    first_name.place(x=400, y=340)

    last_name_label = tk.Label(window,text = "Enter last name").place(x=305,y=360)
    last_name = tk.Entry(window)
    last_name.place(x=400, y=360)

    def on_register():
        if (first_name.get()).isalpha() == False or (last_name.get()).isalpha() == False:
            messagebox.showerror("Warning", "Name cannot contain numbers or special symbols. Please enter valid name.")
            return
        if len(username_text.get()) == 0 or len(password_text.get()) == 0 or len(first_name.get()) == 0 or len(last_name.get()) == 0:
            messagebox.showerror("Warning", "There is whitespace element. Please enter valid information")
            return
        result = register_users(username_text.get(),password_text.get(),first_name.get(),last_name.get())
        if result:
            render_login_screen(window)
        else:
            handler()


    tk.Button(
        window,
        text='Register',
        bg='#e1ad01',
        width='20',
        height='3',
        fg='white',
        command = lambda : on_register()
    ).place(x=400, y=500)

    tk.Button(
        window,
        text="Clear",
        width='15',
        height= "2",
        bg='#e1ad01',
        fg='white',
        command =lambda: clear_text(username_text,password_text,first_name,last_name),
    ).place(x=560, y=315)



def render_login_screen(window: tk.Tk):
   destroy_widgets(window)

   username_label = tk.Label(window, text="Enter username").place(x=305, y=300)
   username_text = tk.Entry(window)
   username_text.place(x=400, y=300)

   passowrd_label = tk.Label(window, text="Enter password").place(x=305, y=320)
   password_text = tk.Entry(window, show='*')
   password_text.place(x=400, y=320)

   def on_login():
       result = login(username_text.get(), password_text.get())
       if result:
           render_product_screen(window)
       else:
           messagebox.showerror("Warning", "Invalid username and password.")


   login_button = tk.Button(
       window,
       text='Enter',
       bg='green',
       width='20',
       heigh='3',
       fg='white',
       command=lambda: on_login()
   ).place(x=250, y=500)

def render_product_screen(window: tk.Tk):
    destroy_widgets(window)

    all_products = get_prod()

    row_idx = 0
    col_idx = 0
    for idx,product in enumerate(all_products):
        if idx % 3 == 0 and idx!=0:
            col_idx = 0
            row_idx = idx * 4
        tk.Label(window, text= product['name']).grid(row=row_idx, column=col_idx)
        tk.Label(window, text= product['image']).grid(row=row_idx+1, column=col_idx)
        tk.Label(window, text= product['count']).grid(row=row_idx+2, column=col_idx)

        tk.Button(
            window,
            text='Buy',
            bg='black',
            fg='white',
        ).grid(row=row_idx+3, column = col_idx)

        col_idx += 1