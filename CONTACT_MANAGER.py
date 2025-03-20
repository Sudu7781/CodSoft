import tkinter as tk
from tkinter import messagebox, simpledialog
import json

contacts = {}

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as file:
            contacts = json.load(file)
    except FileNotFoundError:
        contacts = {}

def save_contacts():
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    if not name:
        return

    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")

    if name and phone:
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        update_contact_list()
        messagebox.showinfo("Success", "Contact added successfully!")
    else:
        messagebox.showerror("Error", "Name and Phone Number are required!")

def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for name, details in contacts.items():
        contact_listbox.insert(tk.END, f"{name} - {details['Phone']}")

def search_contact():
    search_term = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
    if not search_term:
        return

    found = False
    contact_listbox.delete(0, tk.END)
    for name, details in contacts.items():
        if search_term.lower() in name.lower() or search_term in details["Phone"]:
            contact_listbox.insert(tk.END, f"{name} - {details['Phone']}")
            found = True

    if not found:
        messagebox.showinfo("Search Result", "No matching contact found.")

def update_contact():
    name = simpledialog.askstring("Update Contact", "Enter the Name of the contact to update:")
    if name in contacts:
        phone = simpledialog.askstring("Update Contact", "Enter new Phone Number:", initialvalue=contacts[name]["Phone"])
        email = simpledialog.askstring("Update Contact", "Enter new Email:", initialvalue=contacts[name]["Email"])
        address = simpledialog.askstring("Update Contact", "Enter new Address:", initialvalue=contacts[name]["Address"])

        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        save_contacts()
        update_contact_list()
        messagebox.showinfo("Success", "Contact updated successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")

def delete_contact():
    name = simpledialog.askstring("Delete Contact", "Enter the Name of the contact to delete:")
    if name in contacts:
        del contacts[name]
        save_contacts()
        update_contact_list()
        messagebox.showinfo("Success", "Contact deleted successfully!")
    else:
        messagebox.showerror("Error", "Contact not found!")

root = tk.Tk()
root.title("Contact Management System")
root.geometry("400x500")
root.config(bg="#F0F0F0")

title_label = tk.Label(root, text="Contact Management System", font=("Arial", 14, "bold"), bg="#F0F0F0")
title_label.pack(pady=10)

contact_listbox = tk.Listbox(root, width=50, height=10)
contact_listbox.pack(pady=10)

btn_frame = tk.Frame(root, bg="#F0F0F0")
btn_frame.pack(pady=10)

add_btn = tk.Button(btn_frame, text="Add Contact", font=("Arial", 10), width=15, command=add_contact)
add_btn.grid(row=0, column=0, padx=5, pady=5)

view_btn = tk.Button(btn_frame, text="View Contacts", font=("Arial", 10), width=15, command=update_contact_list)
view_btn.grid(row=0, column=1, padx=5, pady=5)

search_btn = tk.Button(btn_frame, text="Search Contact", font=("Arial", 10), width=15, command=search_contact)
search_btn.grid(row=1, column=0, padx=5, pady=5)

update_btn = tk.Button(btn_frame, text="Update Contact", font=("Arial", 10), width=15, command=update_contact)
update_btn.grid(row=1, column=1, padx=5, pady=5)

delete_btn = tk.Button(root, text="Delete Contact", font=("Arial", 10), width=20, command=delete_contact)
delete_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", font=("Arial", 10), width=20, command=root.quit)
exit_btn.pack(pady=5)

load_contacts()
update_contact_list()

root.mainloop()