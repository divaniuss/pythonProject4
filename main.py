from tkinter import *
from tkinter import ttk

def obmin():
    grivni = int(entry.get())
    value = combo.current()

    if value == 0:
        result = grivni / 41
        currency = "$"
    elif value == 1:
        result = grivni / 44
        currency = "€"
    elif value == 2:
        result = grivni / 50
        currency = "£"
    else:
        result_label.config(text="error")
        return
    result_label.config(text=f"Результат обмена: {result} {currency}")

root = Tk()
root.title("obmin")
root.geometry('750x500')

combo = ttk.Combobox(root, values=["Доллары", "Евро", "Фунты"])
combo.grid(row=0, column=1, padx=5, pady=5)

entry = Entry(width=40)
entry.grid(row=1, column=1, padx=5, pady=5)

label = Label(text='Введите гривены: ')
label.grid(row=1, column=0, padx=5, pady=10, sticky=W)

button = Button(text='Обменять', padx=20, command=obmin)
button.grid(row=1, column=2, padx=5, pady=5)

result_label = Label(text='', font=('Times New Roman', 15))
result_label.grid(row=2, column=0, columnspan=4, pady=10)


root.mainloop()