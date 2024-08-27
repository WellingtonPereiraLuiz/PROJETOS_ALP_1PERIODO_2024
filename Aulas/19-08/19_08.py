from tkinter import *
import tkinter.font as tkfont

list_name =  []

def resize_font(event):
    new_size = max(10, int(frame.winfo_height() * 0.05))
    font.configure(size=new_size)

    label.configure(font=font)
    entry.config(font=font)
    display_label.config(font=font)

    for widget in additional_entries:
        widget.config(font=font)

def adicionar():
    name = entry.get()  
    list_name = [name]
    display_label.config(text='O nome digitado foi: "{}".'.format(name)) 


teste = Tk()
teste.title("TESTSTSETSTES")
teste.configure(background='#F8F8FF')

teste.grid_rowconfigure(0, weight=4)
teste.grid_rowconfigure(1, weight=6) 
teste.grid_columnconfigure(0,weight=1)

frame = LabelFrame(teste, text='Cadastro', borderwidth=1, relief='solid', background='white')
frame.grid(row=0, column=0, sticky='NSEW', padx=3, pady=3)
frame.bind('<Configure>', resize_font)

font = tkfont.Font(size=10)

label = Label(frame, text='Digite um nome:', font=font, background='white')
label.grid(row=0, column=0, sticky='W', padx=(3, 20))

entry = Entry(frame, font=font)
entry.grid(row=0, column=1, sticky='EW')

submit_button = Button(frame, text='Adicionar', command=adicionar, font=font, background='yellow')
submit_button.grid(row=2, column=2, sticky='S', padx=10)

display_label = Label(frame, text='', font=font, background='white')
display_label.grid(row=2, column=0, columnspan=2, sticky='w', padx=3)

teste.minsize(width=800, height=480)
teste.mainloop()