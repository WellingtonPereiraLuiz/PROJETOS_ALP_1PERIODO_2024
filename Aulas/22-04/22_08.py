"""
Wellington Pereia Luiz  - pt-br - utf-8 - 20-04-2024
22_08.py
"""


from tkinter import *
import tkinter.font as tkfont

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
    display_label.config(text='O nome digitado foi: "{}".'.format(name))  
   


app = Tk()
app.title('Análise e Desenvolvimento de Sistemas')
app.configure(background='#F8F8FF')

app.grid_rowconfigure(0, weight=4)
app.grid_rowconfigure(1, weight=6)
app.grid_columnconfigure(0, weight=1)


frame = LabelFrame(app, text='Cadastro', borderwidth=1, relief='solid', background='white')
frame.grid(row=0, column=0, sticky='NSEW', padx=3, pady=3)
frame.bind('<Configure>', resize_font)

font = tkfont.Font(size=10)

label = Label(frame, text='Digite um nome:', font=font, background='white')
label.grid(row=0, column=0, sticky='W', padx=(3, 20))


entry = Entry(frame, font=font)
entry.grid(row=0, column=1, sticky='EW')



submit_button = Button(frame, text='Adicionar', command=adicionar, font=font, background='yellow')
submit_button.grid(row=1, column=1, sticky='S', padx=10)




display_label = Label(frame, text='', font=font, background='white')
display_label.grid(row=2, column=0, columnspan=2, sticky='w', padx=3)

additional_entries = []





for i in range(4):
    new_label = Label(frame, text=f'Campo {i + 1}:', font=font, background='white')
    new_label.grid(row=3 + i, column=0, sticky='W', padx=(3, 20))

    new_entry = Entry(frame, font=font)
    new_entry.grid(row=3 + i, column=1, sticky='EW')

    additional_entries.extend([new_label, new_entry])

frame.grid_columnconfigure(1, weight=1)

app.minsize(width=800, height=480)
app.mainloop()



"""
from tkinter import *

app = Tk()
app.title('Analie e Desenvolvimento de Sistemas')
app.geometry('1360x680')
app.configure(background='#F8F8FF')
app.resizable(True, True)
app.maxsize(width=1360, height=670)
app.minsize(width=1360, height=670)

frame = LabelFrame(app, text="Cadastro", borderwidth=1, relief='solid')
frame.place(x=10, y=10, width=1340, height=340)

lb_1 = Label(frame, text='Contatos: ',fg = 'red', font =("Arial",14,"italic","bold"))
lb_1.place(x = 15, y = 10, width= 70, height= 20)

lb_2 = Label(frame, text= 'Dig')


app.mainloop()
"""
"""
from tkinter import *

def capturar():
    Ib_3['text'] = nome.get()

app = Tk()
app.title('Analise e Desenvolvimento de Sistemas')
app.geometry('1360x680')
app.configure(background='#F8F8FF')
app.resizable(True, True)
app.minsize(width=1280, height=670)
app.maxsize(width=1280, height=670)

frame = LabelFrame(app, text="Cadastro", borderwidth=1, relief='solid')
frame.place(x=10, y=10, width=850, height=275)

Ib_1 = Label(frame, text='contatos: ', fg='red', font=("Arial", 14, "bold italic"))
Ib_1.place(x=20, y=10, width=95, height=25)

Ib_2 = Label(frame, text='Digite um nome: ', font=("Arial", 14))
Ib_2.place(x=20, y=35, width=145, height=20)

nome = Entry(frame, font=('Arial', 14))
nome.place(x=160, y=35, width=300, height=20)

nome.focus_set()

Ib_3 = Label(app, text='', font=("Arial", 14), background='#F8F8FF')
Ib_3.place(x=135, y=370, width=250, height=20)

btn_captura = Button(app, text = 'Capturara dados', font=("Arial", 14, "bold"), command= capturar)
btn_captura.place(x=490, y=300, width=200, height=40)

app.mainloop()

"""