from tkinter import ttk
from tkinter import *
res = 'km'
class Product:
    def __init__(self, window):
        self.wind = window
        self.wind.title('Encriptacion RSA')

        frame = LabelFrame(self.wind, text = 'Encriptar:')
        frame.grid(row = 0, column=0, columnspan = 3,pady= 20)


        Label(frame,text= 'p: ').grid(row =1,column =0)
        self.p =Entry(frame)
        self.p.focus()
        self.p.grid(row =1,column=1)

        Label(frame,text= 'q: ').grid(row =2,column =0)
        self.q =Entry(frame)
        self.q.grid(row =2,column=1)

        Label(frame,text= 'd: ').grid(row =3,column =0)
        self.d =Entry(frame)
        self.d.grid(row =3,column=1)

        Label(frame,text= 'word: ').grid(row =4,column =0)
        self.word =Entry(frame)
        self.word.grid(row =4,column=1)

        ttk.Button(frame,text = 'encriptar',command = self.encriptar).grid(row=6,columnspan =2,sticky = W+E)
        
        
        
    def encriptar(self):
        Label(frame,text= 'goa').grid(row =7,column =0)
        
        

if __name__ == '__main__':
    window = Tk()
    application = Product(window)
    window.mainloop()
    
    