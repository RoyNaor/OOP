import tkinter as tk
from components.RoundedButton import RoundedButton
from register import open_register_window
from Backend.Librarian import *
from library import open_library_window


def center_window(window, width, height):
    # Get the screen's width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window's geometry to center it
    window.geometry(f"{width}x{height}+{x}+{y}")

    # go to Register screen
def on_button_click(current_window):
    current_window.destroy()  # Close the current window
    open_register_window()    # Open the register window

    # check the login and Enter Library
def submit_login(username_entry, password_entry, current_window):
    # Get the input values from the entry fields
    name = username_entry.get()
    password = password_entry.get()

    if Librarian.check_login(name, password):
        current_window.destroy()  # Close the current window
        open_library_window()  # Open the library interface
    else:
        # Display an alert message on the same window
        alert_label = tk.Label(current_window, text="Invalid username or password!", fg="red", font=("Arial", 12))
        alert_label.pack(pady=(10, 5))

        current_window.after(2000, alert_label.destroy)

def open_login_window():

    # Main window setup
    login = tk.Tk()
    center_window(login, 500, 600)
    login.title("Library/Login")
    login.configure(bg="#f8f0fc")

    # Header (Placed at the top of the window)
    header = tk.Label(login, text="Login", font=("Ariel", 24, "bold"), bg="#f8f0fc", fg="#4b0082")
    header.pack(pady=(5, 5))  # Space above and below the header

    # Frame to center the form
    form_frame = tk.Frame(login, bg="#f8f0fc")
    form_frame.pack(expand=True, pady=5)

    # Username Label and Entry
    username_label = tk.Label(form_frame, text="Username:", font=("Ariel", 18), bg="#f8f0fc", fg="#4b0082")
    username_label.pack(pady=(10, 5))  # Small padding above and below the label
    username_entry = tk.Entry(form_frame, font=("Ariel", 18), width=25)
    username_entry.pack(pady=5)

    # Password Label and Entry
    password_label = tk.Label(form_frame, text="Password:", font=("Ariel", 18), bg="#f8f0fc", fg="#4b0082")
    password_label.pack(pady=(15, 5))  # Padding above and below
    password_entry = tk.Entry(form_frame, font=("Ariel", 18), show="*", width=25)
    password_entry.pack(pady=5)

    # Submit Button
    submit_canvas = tk.Canvas(form_frame, bg="#f8f0fc", width=400, height=80, highlightthickness=0)
    submit_canvas.pack(pady=(15, 5))  # Padding above and below the submit button
    RoundedButton(submit_canvas, 100, 15, 200, 50, 25, "Submit", lambda: submit_login(username_entry, password_entry, login))

    # Doesn't have a user? Text (Now directly above the register button)
    register_text = tk.Label(form_frame, text="Doesn't have an account?", font=("Ariel", 14), bg="#f8f0fc", fg="#4b0082")
    register_text.pack(pady=(10, 5))

    # Register Button
    register_canvas = tk.Canvas(form_frame, bg="#f8f0fc", width=400, height=80, highlightthickness=0)
    register_canvas.pack(pady=5)
    RoundedButton(register_canvas, 100, 15, 200, 50, 25, "Register", lambda: on_button_click(login))

    # Start the Tkinter loop
    login.mainloop()
