import tkinter
from tkinter import END



tk = tkinter.Tk()
tk.title("Listbox")

listbox = tkinter.Listbox(tk)
listbox.pack()
listbox.insert(END, "hello", "Hi", "Yo")
listbox.insert(END, "hola", "ciao", "ca va")
listbox.delete(0)


tk.mainloop()