# GUI
# tkinter

from tkinter import *

window = Tk()
window.title('First GUI programe')

def click():
    x = ent.get()
    lbl.config(text=f'You are selected, {x}')

lbl = Label(
    window,
    text='Hello',
    fg= 'red',
    bg='yellow',
    font=('Arial Bold', 20)
)


btn = Button(
    window,
    text='Click Here',
    fg='green',
    bg='lavender',
    font=('Arial Bold', 15),
    command=click
)

ent = Entry(
    width=50
)



lbl.pack()
btn.pack()
ent.pack()


window.mainloop()

