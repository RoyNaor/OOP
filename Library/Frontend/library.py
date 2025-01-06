import tkinter as tk
from components.RoundedButton import RoundedButton


def center_window(window, width, height):
    # Get the screen's width and height
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()

    # Calculate the x and y coordinates to center the window
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2

    # Set the window's geometry to center it
    window.geometry(f"{width}x{height}+{x}+{y}")


def dummy_command(action):
    print(f"{action} button clicked!")


def open_library_window():
    # Main window setup
    root = tk.Tk()
    center_window(root, 1000, 500)  # Adjusted for more space
    root.title("Library")
    root.configure(bg="#f8f0fc")

    # Header Frame
    header_frame = tk.Frame(root, bg="#6a0dad", height=100)
    header_frame.pack(fill=tk.X)

    # Load the logo image
    logo_path = "assets/logo.png"
    logo_photo = tk.PhotoImage(file=logo_path)

    # Resize the image using subsample
    resized_logo = logo_photo.subsample(8, 8)  # Adjust the factor to resize the image

    # Logo Label
    logo_label = tk.Label(header_frame, image=resized_logo, bg="#6a0dad")
    logo_label.image = resized_logo  # Keep a reference to avoid garbage collection
    logo_label.pack(side=tk.LEFT, padx=10, pady=10)

    # Header Label (Library Title)
    header_label = tk.Label(header_frame, text="Library", font=("Ariel", 20, "bold"), fg="#ffffff", bg="#6a0dad")
    header_label.pack(side=tk.LEFT, padx=10)

    # Create a canvas for the buttons
    button_canvas = tk.Canvas(root, bg="#f8f0fc", width=1000, height=500, highlightthickness=0)
    button_canvas.pack()

    # Button data: (Label, Action)
    buttons = [
        ("Add Book", "Add Book"),
        ("Remove Book", "Remove Book"),
        ("Search Book", "Search Book"),
        ("View Books", "View Books"),
        ("Lend Book", "Lend Book"),
        ("Return Book", "Return Book"),
        ("Logout", "Logout"),
        ("Login", "Login"),
        ("Register", "Register"),
        ("Popular Books", "Popular Books"),
    ]

    # Create buttons in a grid-like layout
    cols = 4
    button_width = 200
    button_height = 50
    button_spacing = 20
    x_start = 50
    y_start = 50
    radius = 25

    for idx, (label, action) in enumerate(buttons):
        row = idx // cols
        col = idx % cols
        x = x_start + col * (button_width + button_spacing)
        y = y_start + row * (button_height + button_spacing)
        RoundedButton(button_canvas, x, y, button_width, button_height, radius, label, lambda a=action: dummy_command(a))

    # Start the Tkinter event loop
    root.mainloop()
