import tkinter as tk
import os

from PIL import ImageTk, Image

from authentication_service import register, login
from products_service import get_all_products


def clear_window(window: tk.Tk):
    for widget in window.winfo_children():
        widget.destroy()


def render_main_screen(window: tk.Tk):
    tk.Button(
        window,
        text="Login",
        bg='green',
        fg='white',
        command=lambda: render_login_screen(window)
    ).grid(row=0, column=0)

    tk.Button(
        window,
        text="Register",
        bg='yellow',
        fg='black',
        command=lambda: render_register_screen(window)
    ).grid(row=0, column=1)


def render_register_screen(window: tk.Tk):
    clear_window(window)

    tk.Label(window, text="Username").grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text="Password").grid(row=1, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    tk.Label(window, text="First Name").grid(row=2, column=0)
    first_name = tk.Entry(window)
    first_name.grid(row=2, column=1)

    tk.Label(window, text="Last Name").grid(row=3, column=0)
    last_name = tk.Entry(window)
    last_name.grid(row=3, column=1)

    def on_register():
        result = register(username.get(), password.get(), first_name.get(), last_name.get())
        if result:
            render_login_screen(window)
        else:
            tk.Label(window, text="The username has been already registered!", fg='red').grid(row=0, column=2)

    tk.Button(
        window,
        text="Register",
        bg='green',
        fg='black',
        command=lambda: on_register()
    ).grid(row=4, column=1)


def render_login_screen(window: tk.Tk):
    clear_window(window)

    tk.Label(window, text="Username").grid(row=0, column=0)
    username = tk.Entry(window)
    username.grid(row=0, column=1)

    tk.Label(window, text="Password").grid(row=1, column=0)
    password = tk.Entry(window, show='*')
    password.grid(row=1, column=1)

    def on_login():
        result = login(username.get(), password.get())
        if result:
            render_products_screen(window)
        else:
            tk.Label(window, text="Incorrect username or password.", fg='red').grid(row=2, column=1)

    tk.Button(
        window,
        text="Enter",
        bg='green',
        fg='black',
        command=lambda: on_login()
    ).grid(row=3, column=1)


def render_products_screen(window: tk.Tk):
    clear_window(window)

    all_products = get_all_products()

    row_idx = col_idx = 0
    for idx, product in enumerate(all_products):
        if idx % 3 == 0 and idx != 0:
            col_idx = 0
            row_idx = idx * 4

        tk.Label(window, text=product['name']).grid(row=row_idx, column=col_idx)

        image = Image.open(os.path.join('db', 'images', product['image'])).resize((100, 100))
        photo_image = ImageTk.PhotoImage(image)

        image_label = tk.Label(image=photo_image)
        image_label.image = photo_image
        image_label.grid(row=row_idx + 1, column=col_idx)

        tk.Label(window, text=product['count']).grid(row=row_idx + 2, column=col_idx)

        tk.Button(
            window,
            text="Buy",
            bg='black',
            fg='white',
        ).grid(row=row_idx + 3, column=col_idx)

        col_idx += 1
