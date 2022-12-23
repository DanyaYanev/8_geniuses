from tkinter import *
from tkinter import messagebox
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.colorchooser import askcolor

file_name = NONE

def change_bg():
    colors = askcolor(title="Цвет фона")
    text.configure(bg=colors[1])

def change_fg():
    colors = askcolor(title="Цвет текста")
    text.configure(fg=colors[1])

def dark_theme():
    text['bg'] = '#262626'
    text['fg'] = 'white'

def white_theme():
    text['bg'] = 'white'
    text['fg'] = 'black'

def new_file():
    global file_name
    file_name = 'Без названия'
    text.delete('1.0', END)

def save_as():
    out = asksaveasfile(mode='w', defaultextension='.txt')
    data = text.get('1.0', END)
    try:
        out.write(data.rstrip())
    except Exception:
        messagebox.showerror('Нельзя сохранить файл')

def open_file():
    global file_name
    inp = askopenfile(mode='r')
    if inp is None:
        return
        file_name = inp.name
    data = inp.read()
    text.delete('1.0', END)
    text.insert('1.0', data)


root = Tk()
root.title('Заметки')
root.geometry('600x600')

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

text = Text(root, height=600, width=600, yscrollcommand=scrollbar.set, padx=5, pady=5, spacing3=5)
text.pack()

scrollbar.config(command=text.yview)

menu_bar = Menu(root)
file_menu = Menu(menu_bar, tearoff=0)
view_menu = Menu(menu_bar, tearoff=0)
theme_menu = Menu(view_menu, tearoff=0)
view_menu.add_cascade(label="Темы", menu=theme_menu)


menu_bar.add_cascade(label='Файл', menu=file_menu)
menu_bar.add_cascade(label='Вид', menu=view_menu)

file_menu.add_command(label='Новый', command=new_file)
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить как', command=save_as)

view_menu.add_command(label='Цвет фона', command=change_bg)
view_menu.add_command(label='Цвет текста', command=change_fg)

theme_menu.add_command(label='Тёмная тема', command=dark_theme)
theme_menu.add_command(label='Светлая тема', command=white_theme)


root.config(menu=menu_bar)
root.mainloop()