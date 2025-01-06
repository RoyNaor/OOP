import tkinter as tk
import os
from components.RoundedButton import RoundedButton
from login import open_login_window
from Backend.FileHandler import FileHandler


def center_window(window, width, height):
    # Get the screen's width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window's geometry to center it
    window.geometry(f"{width}x{height}+{x}+{y}")


def on_button_click():
    landing.destroy()  # Close the current window
    open_login_window()  # Call the function to open the login window


# create users with the new Path
backend_path = os.path.join(os.path.dirname(__file__), "..", "Backend")
users_csv_path = os.path.join(backend_path, "users.csv")
FileHandler.create_csv(users_csv_path, ["name", "password"])  # create the users csv

# Main window setup
landing = tk.Tk()
center_window(landing, 500, 400)  # Adjusted smaller window size
landing.title("Library/landing")
landing.configure(bg="#f8f0fc")


# Header Frame
header_frame = tk.Frame(landing, bg="#6a0dad", height=100)
header_frame.pack(fill=tk.X)
header_label = tk.Label(header_frame, text="Welcome to Our Library", font=("Ariel", 20, "bold"), fg="#ffffff", bg="#6a0dad")
header_label.pack(pady=10)

# Main Content Frame
content_frame = tk.Frame(landing, bg="#f8f0fc")
content_frame.pack(expand=True, fill=tk.BOTH, padx=20, pady=20)

# Add a subtitle
subtitle_label = tk.Label(
    content_frame,
    text="Ex3 in Ariel University's OOP course!",
    font=("Ariel", 14, "italic"),
    fg="#4b0082",
    bg="#f8f0fc"
)  # Adjusted font size
subtitle_label.pack(pady=10)

# Canvas for the rounded button
canvas = tk.Canvas(content_frame, bg="#f8f0fc", width=460, height=120, highlightthickness=0)  # Adjusted size
canvas.pack(pady=10)  # Added padding to fit smaller screen

# Add the rounded button by instantiating the RoundedButton class
RoundedButton(canvas, 130, 60, 200, 50, 25, "Get Started", on_button_click)  # Adjusted button position

landing.mainloop()
