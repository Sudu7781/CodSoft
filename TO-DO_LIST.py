import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def mark_completed():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_text = task_listbox.get(selected_task_index)

        if not task_text.startswith("✔ "):
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, "✔ " + task_text)
        else:
            messagebox.showinfo("Info", "Task is already completed!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as completed!")

def update_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task:
            task_listbox.delete(selected_task_index)
            task_listbox.insert(selected_task_index, new_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Updated task cannot be empty!")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update!")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to remove!")

def clear_tasks():
    task_listbox.delete(0, tk.END)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x450")
root.config(bg="#F0F0F0")

task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=5)

add_btn = tk.Button(btn_frame, text="Add Task", command=add_task, width=12)
add_btn.grid(row=0, column=0, padx=5)

update_btn = tk.Button(btn_frame, text="Update Task", command=update_task, width=12)
update_btn.grid(row=0, column=1, padx=5)

remove_btn = tk.Button(btn_frame, text="Remove Task", command=remove_task, width=12)
remove_btn.grid(row=1, column=0, padx=5, pady=5)

complete_btn = tk.Button(btn_frame, text="Mark Completed", command=mark_completed, width=12)
complete_btn.grid(row=1, column=1, padx=5, pady=5)

clear_btn = tk.Button(root, text="Clear All Tasks", command=clear_tasks, width=30)
clear_btn.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

root.mainloop()