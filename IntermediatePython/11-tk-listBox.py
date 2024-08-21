#import tkinter
#from tkinter import END



#tk = tkinter.Tk()
#tk.title("Listbox")

#listbox = tkinter.Listbox(tk)
#listbox.pack()
#listbox.insert(END, "hello", "Hi", "Yo")
#listbox.insert(END, "hola", "ciao", "ca va")
#listbox.delete(0)


#tk.mainloop()


import tkinter
from tkinter import END

def add_to_list():
    listbox.insert(END, entry.get())
    entry.delete(0, END)

def remove_from_list():
    listbox.delete(listbox.curselection())
    



tk = tkinter.Tk()
tk.title("Listbox")

listbox = tkinter.Listbox(tk)
listbox.pack()

entry = tkinter.Entry(tk)
entry.pack()

button = tkinter.Button(tk, text="Add Value", command=add_to_list)
button.pack()

button = tkinter.Button(tk, text="Remove Selected Value", command=remove_from_list)
button.pack()


tk.mainloop()