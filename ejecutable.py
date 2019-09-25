from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        _p = int(p.get())
        _q = int(q.get())
        _d = int(d.get())
        _word = str(word.get())

        n = _p*_q
        En = (_p-1)*(_q-1)
        euler = 0

        while True:
            mod = (_d * euler) % En
            if mod == 1:
                break
            euler += 1

        cPriv = "clave privada("+ str(n)+"," +str(_d)+")"
        cPub = "clave publica("+ str(n)+"," +str(euler)+")"
        clv1.set(cPriv)
        clv2.set(cPub)


        palabra = list(_word)

        end_word = ""
        
        for caracter in palabra:
            c = ord(caracter)
            encrypt = (c ** euler)%n
            end_word += chr(encrypt)

        encript.set(end_word)





    except ValueError:
        pass

root = Tk()
root.title("Encriptacion RSA")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

p = StringVar()
q = StringVar()
d = StringVar()
word = StringVar()

clv1 = StringVar()
clv2 = StringVar()
encript = StringVar()

p_entry = ttk.Entry(mainframe, width=12, textvariable=p)
p_entry.grid(column=2, row=1, sticky=(W, E))
q_entry = ttk.Entry(mainframe, width=12, textvariable=q)
q_entry.grid(column=2, row=2, sticky=(W, E))
d_entry = ttk.Entry(mainframe, width=12, textvariable=d)
d_entry.grid(column=2, row=3, sticky=(W, E))
word_entry = ttk.Entry(mainframe, width=12, textvariable=word)
word_entry.grid(column=2, row=4, sticky=(W, E))


ttk.Label(mainframe, textvariable=clv1).grid(column=2, row=5, sticky=(W, E))
ttk.Label(mainframe, textvariable=clv2).grid(column=2, row=6, sticky=(W, E))
ttk.Label(mainframe, textvariable=encript).grid(column=2, row=7, sticky=(W, E))
ttk.Button(mainframe, text="Encriptar", command=calculate).grid(column=2, row=8, sticky=W)
ttk.Button(mainframe, text="Desencriptar", command=calculate).grid(column=2, row=9, sticky=W)
ttk.Label(mainframe, text="p:").grid(column=1, row=1)
ttk.Label(mainframe, text="q:").grid(column=1, row=2)
ttk.Label(mainframe, text="d:").grid(column=1, row=3)
ttk.Label(mainframe, text="word:").grid(column=1, row=4)



for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

p_entry.focus()
root.bind('<Return>', calculate)

root.mainloop()
