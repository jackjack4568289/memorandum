import tkinter as tk
import sys

class ContactsApp:
    def __init__(self, root, universal_background_color, universal_button_background_color):
        self.root = root
        self.contacts = []

        self.frame = tk.Frame(root, bg=universal_background_color)
        self.frame.pack()

        self.add_contact_fields()

        self.add_button = tk.Button(self.frame, text="Add Contact", command=self.add_contact, bg=universal_button_background_color)
        self.add_button.pack()

        self.delete_button = tk.Button(self.frame, text="Delete Contact", command=self.delete_contact, bg=universal_button_background_color)
        self.delete_button.pack()

        self.contacts_list = tk.Listbox(self.frame)
        self.contacts_list.pack()
        self.contacts_list.bind("<Double-Button-1>", self.on_double_click)

    def add_contact_fields(self):
        self.name_label = tk.Label(self.frame, text="Name:", bg=universal_background_color)
        self.name_label.pack()

        self.name_entry = tk.Entry(self.frame)
        self.name_entry.pack()

        self.phone_label = tk.Label(self.frame, text="Phone:", bg=universal_background_color)
        self.phone_label.pack()

        self.phone_entry = tk.Entry(self.frame)
        self.phone_entry.pack()

    def add_contact(self):
        name = self.name_entry.get()
        phone = self.phone_entry.get()
        if name and phone:
            contact_info = f"{name}: {phone}"
            self.contacts.append(contact_info)
            self.update_contact_list()

    def delete_contact(self):
        selected_contact = self.contacts_list.get(tk.ACTIVE)
        if selected_contact:
            self.contacts.remove(selected_contact)
            self.update_contact_list()

    def update_contact_list(self):
        self.contacts_list.delete(0, tk.END)
        for contact in self.contacts:
            self.contacts_list.insert(tk.END, contact)

    def on_double_click(self, event):
        selected_idx = self.contacts_list.curselection()
        if selected_idx:
            contact_idx = selected_idx[0]
            selected_contact = self.contacts[contact_idx]
            self.show_calling_interface(selected_contact)

    def show_calling_interface(self, selected_contact):
        view_contact_window = tk.Toplevel(self.root)
        view_contact_window.title(f"Contact")

        contact_info = selected_contact.split(": ")
        name_label = tk.Label(view_contact_window, text=f"Name: {contact_info[0]}")
        name_label.pack()

        phone_label = tk.Label(view_contact_window, text=f"Phone: {contact_info[1]}")
        phone_label.pack()

        calling_label = tk.Label(view_contact_window, text="Calling...")
        calling_label.pack()

    def open_contact_interface(content):
        root = tk.Tk()
        root.title("Contacts Application")
        #root.configure(bg=universal_background_color)
        app = ContactsApp(root)
        app.frame.pack_propagate(False)
        root.mainloop()

if __name__ == "__main__":

    # 列印傳遞給腳本的參數
    if len(sys.argv) > 1:
        universal_background_color = sys.argv[1]
        universal_button_background_color = sys.argv[2]
    else:
        print("沒有傳遞參數給腳本")

    root = tk.Tk()
    root.configure(bg=universal_background_color)
    root.title("Contacts Application")
    #root.configure(bg=universal_background_color)
    app = ContactsApp(root, universal_background_color, universal_button_background_color)

    root.mainloop()