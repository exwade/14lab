import tkinter as tk

def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def remove_task():
    try:
        selected_task_index = task_list.curselection()[0]
        task_list.delete(selected_task_index)
    except IndexError:
        pass

# Создание главного окна
root = tk.Tk()
root.title("To-Do List")

# Создание элементов интерфейса
task_entry = tk.Entry(root, width=40)
task_entry.grid(row=0, column=0, padx=10, pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.grid(row=0, column=1, padx=5, pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.grid(row=0, column=2, padx=5, pady=10)

task_list = tk.Listbox(root, width=50)
task_list.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

# Запуск главного цикла программы
root.mainloop()
