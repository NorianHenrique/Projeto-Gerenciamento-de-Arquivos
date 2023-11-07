from tkinter import *
from tkinter import messagebox

# Classe para representar uma tarefa
class Task:
    def __init__(self, title, description, category):
        self.title = title
        self.description = description
        self.category = category

# Função para adicionar uma nova tarefa
def add_task():
    title = entry_title.get()
    description = entry_description.get()
    category = entry_category.get()

    task = Task(title, description, category)
    tasks.append(task)

    messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")

    entry_title.delete(0, END)
    entry_description.delete(0, END)
    entry_category.delete(0, END)

# Função para exibir todas as tarefas
def show_tasks():
    for task in tasks:
        print("Título:", task.title)
        print("Descrição:", task.description)
        print("Categoria:", task.category)
        print("")

# Lista para armazenar as tarefas
tasks = []

# Criação da janela principal
window = Tk()
window.title("Sistema de Gerenciamento de Tarefas")

# Criação dos campos de entrada
label_title = Label(window, text="Título:")
label_title.pack()
entry_title = Entry(window)
entry_title.pack()

label_description = Label(window, text="Descrição:")
label_description.pack()
entry_description = Entry(window)
entry_description.pack()

label_category = Label(window, text="Categoria:")
label_category.pack()
entry_category = Entry(window)
entry_category.pack()

# Criação dos botões
button_add = Button(window, text="Adicionar Tarefa", command=add_task)
button_add.pack()

button_show = Button(window, text="Exibir Tarefas", command=show_tasks)
button_show.pack()

# Execução da janela principal
window.mainloop()
