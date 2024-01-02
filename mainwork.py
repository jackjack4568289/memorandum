import tkinter as tk
import goodalarm
import shop
import subprocess

global points
points = 100
universal_background_color = "#ffffff"
universal_button_background_color = "#c7c7c7"

blue_background_color = "#1cbcf2"
blue_button_background_color = "#acd4f2"

green_background_color = "#2ecc0e"
green_button_background_color = "#d3eda5"

red_background_color = "#f95b5b"
red_button_background_color = "#e95a8c"

def alarm_click():
    global points
    result = subprocess.run(["python", "goodalarm.py", str(points), universal_background_color, universal_button_background_color])
    points = result.returncode
    return points

def contacts_click():
    subprocess.run(["python", "contacts.py", universal_background_color, universal_button_background_color])

def store_click():
    global points
    result = subprocess.run(["python", "shop.py", str(points), universal_background_color, universal_button_background_color], capture_output=True, text=True)
    points = result.returncode

def memorandum_click():
    content_to_display = "Your new content"  # Modify the content here
    subprocess.run(["python", "memorandum.py", universal_background_color, universal_button_background_color])

def apply_color_change_to_main_menu():
    alarm_button.configure(bg=universal_button_background_color)
    store_button.configure(bg=universal_button_background_color)
    memo_button.configure(bg=universal_button_background_color)
    contacts_button.configure(bg=universal_button_background_color)
    root.configure(bg=universal_background_color)

def change_color_to_blue():
    global universal_background_color, universal_button_background_color
    universal_background_color = blue_background_color
    universal_button_background_color = blue_button_background_color
    apply_color_change_to_main_menu()

def change_color_to_green():
    global universal_background_color, universal_button_background_color
    universal_background_color = green_background_color
    universal_button_background_color = green_button_background_color
    apply_color_change_to_main_menu()

def change_color_to_red():
    global universal_background_color, universal_button_background_color
    universal_background_color = red_background_color
    universal_button_background_color = red_button_background_color
    apply_color_change_to_main_menu()

# Create the main window
root = tk.Tk()
root.title("把握人生系統")
root.configure(bg=universal_background_color)

# Set the initial size of the window
root.geometry("400x600")  # You can adjust the size as needed (width x height)

# Add a centered title frame
title_frame = tk.Frame(root, bg=universal_background_color)
title_frame.pack(pady=10)

# Add a centered title label inside the title frame
title_label = tk.Label(title_frame, text="把握人生系統", font=("Helvetica", 30, "bold"), bg=universal_background_color)
title_label.pack()

# Create buttons with specified sizes and spacing
alarm_button = tk.Button(root, text="鬧鐘", command=alarm_click, width=30, height=5, bg=universal_button_background_color)
alarm_button.pack(pady=5)

contacts_button = tk.Button(root, text="聯繫人", command=contacts_click, width=30, height=5, bg=universal_button_background_color)
contacts_button.pack(pady=5)

store_button = tk.Button(root, text="商店", command=store_click, width=30, height=5, bg=universal_button_background_color)
store_button.pack(pady=5)

memo_button = tk.Button(root, text="備忘錄", command=memorandum_click, width=30, height=5, bg=universal_button_background_color)
memo_button.pack(pady=5)

blue_button = tk.Button(root, text="更換顏色-藍", command=change_color_to_blue, width=8, height=2, bg=blue_button_background_color)
blue_button.pack(side='right', padx=10)

green_button = tk.Button(root, text="更換顏色-綠", command=change_color_to_green, width=8, height=2, bg=green_button_background_color)
green_button.pack(side='right', padx=10)

red_button = tk.Button(root, text="更換顏色-紅", command=change_color_to_red, width=8, height=2, bg=red_button_background_color)
red_button.pack(side='right', padx=10)

# Start the event loop
root.mainloop()
