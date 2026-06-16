from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
import webbrowser

file_name = None  # можно хранить имя текущего файла

# Функция для создания новой заметки
def new_file():
    global file_name
    file_name = "Без названия"
    text.delete("1.0", END)

# Функция для сохранения заметки
def save_as():
    out = asksaveasfile(mode="w", defaultextension=".txt")
    if out is None:  # пользователь нажал "Отмена"
        return

    data = text.get("1.0", END)
    try:
        out.write(data.rstrip())
        out.close()
    except Exception:
        messagebox.showerror("Ошибка!", "Не удалось сохранить файл!")

# Функция для открытия заметки
def open_file():
    global file_name
    inp = askopenfile(mode="r")
    if inp is None:  # пользователь нажал "Отмена"
        return

    file_name = inp.name
    data = inp.read()
    inp.close()

    text.delete("1.0", END)
    text.insert("1.0", data)

# Задача 2: справка -> открыть ссылку
def get_help():
    url = "https://www.google.com/search?q=%D0%BA%D0%B0%D0%BA+%D0%BF%D0%B8%D1%81%D0%B0%D1%82%D1%8C+%D0%B7%D0%B0%D0%BC%D0%B5%D1%82%D0%BA%D0%B8"
    webbrowser.open(url)

# Задача 3: выход из приложения
def exit_app():
    root.destroy()


root = Tk()
root.title("Заметки")
root.geometry("400x400")

text = Text(root, width=400, height=400)
text.pack()

# Создаём меню
menu_bar = Menu(root)

# Меню "Опции"
options_menu = Menu(menu_bar, tearoff=0)
options_menu.add_command(label="Создать...", command=new_file)
options_menu.add_command(label="Открыть...", command=open_file)
options_menu.add_command(label="Сохранить как...", command=save_as)
options_menu.add_separator()
options_menu.add_command(label="Выход", command=exit_app)

menu_bar.add_cascade(label="Опции", menu=options_menu)

# Меню "Справка"
help_menu = Menu(menu_bar, tearoff=0)
help_menu.add_command(label="Получить справку", command=get_help)
menu_bar.add_cascade(label="Справка", menu=help_menu)

root.config(menu=menu_bar)
root.mainloop()
