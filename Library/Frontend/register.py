import tkinter as tk
from components.RoundedButton import RoundedButton
from library import open_library_window
from Backend.Librarian import *


def center_window(window, width, height):
    # Get the screen's width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window's geometry to center it
    window.geometry(f"{width}x{height}+{x}+{y}")


def submit_register(name_entry, password_entry, current_window):
    # Get the input values from the entry fields
    name = name_entry.get()
    password = password_entry.get()

    # Validate inputs
    if not name or not password:
        # Display an alert message if inputs are invalid
        alert_label = tk.Label(current_window, text="Name and Password are required!", fg="red", font=("Arial", 12))
        alert_label.pack(pady=(10, 5))

        # Remove the alert after 3 seconds
        current_window.after(3000, alert_label.destroy)
        return

    # Create a new Librarian
    new_librarian = Librarian(name, password)
    print(f"Librarian {new_librarian.name} created!")

    # Close the current window and open the library interface
    current_window.destroy()
    open_library_window()


def open_register_window():
    # Main window setup
    register = tk.Tk()
    center_window(register, 500, 400)
    register.title("Library/Register")
    register.configure(bg="#f8f0fc")

    # Header
    header = tk.Label(register, text="Register", font=("Ariel", 24, "bold"), bg="#f8f0fc", fg="#4b0082")
    header.pack(pady=(10, 15))

    # Frame for the form
    form_frame = tk.Frame(register, bg="#f8f0fc")
    form_frame.pack(pady=(10, 0))

    # Username Label and Entry
    username_label = tk.Label(form_frame, text="Username:", font=("Ariel", 16), bg="#f8f0fc", fg="#4b0082")
    username_label.pack(pady=(10, 5))
    username_entry = tk.Entry(form_frame, font=("Ariel", 14), width=25)
    username_entry.pack(pady=5)

    # Password Label and Entry
    password_label = tk.Label(form_frame, text="Password:", font=("Ariel", 16), bg="#f8f0fc", fg="#4b0082")
    password_label.pack(pady=(15, 5))
    password_entry = tk.Entry(form_frame, font=("Ariel", 14), show="*", width=25)
    password_entry.pack(pady=5)

    # Submit Button
    submit_canvas = tk.Canvas(form_frame, bg="#f8f0fc", width=400, height=80, highlightthickness=0)
    submit_canvas.pack(pady=(15, 5))
    RoundedButton(submit_canvas, 100, 15, 200, 50, 25, "Submit", lambda: submit_register(username_entry, password_entry, register))

    # Start Tkinter loop
    register.mainloop()

