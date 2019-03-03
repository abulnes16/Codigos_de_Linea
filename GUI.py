from tkinter import *
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Interfaz:
    def __init__(self):
        self.v = Tk()
        self.ancho = self.v.winfo_width()
        self.alto = self.v.winfo_height()
        self.v.title('Proyecto II - Redes de Datos II')
        self.v.geometry('500x500')

        self.initComponents()

    def show(self):
        self.v.mainloop()


    def initComponents(self):
        self.v.grid_columnconfigure(1, weight = 1)
        self.titulo = Label(self.v, text= 'Graficador de codigos de linea')
        self.titulo.grid(row = 0, column = 0 , columnspan = 2, pady = (10,10))
        self.lb2 = Label(self.v, text= 'Ingrese la cadena binaria:')
        self.lb2.grid(row = 1, column = 0,padx = (30,10), pady =(5,5))
        self.binario = StringVar()
        self.txt = Entry(self.v, textvariable = self.binario)
        self.txt.configure(width = 25)
        self.txt.grid(row = 1, column = 1, padx = (10,10), pady = (5,5))
        self.lb3 = Label(self.v, text = 'Codigo de linea')
        self.lb3.grid(row = 2, column = 0, padx =(30,10), pady = (5,5))
        self.comboLineas = ttk.Combobox(self.v, state = 'readonly')
        self.comboLineas['values'] = ['NRZ','RZ','AMI','ADI','B3ZS','HDB3','B6ZS','Manchester','CMI']
        self.comboLineas.configure(width = 22)
        self.comboLineas.grid(row = 2, column = 1, padx = (10,10), pady =(5,5))
        self.comboLineas.bind("<<ComboboxSelected>>", self.selecciona)
        self.addMenu()
        #self.iniciarCanvas()


    def addMenu(self):
        self.barra = Menu(self.v)
        self.barra.add_command(label = 'Salir',command = self.v.destroy)
        self.barra.add_command(label = 'Integrantes', command = self.mostrarI)
        self.v.config(menu = self.barra)

    #No sé cómo hacerlo, pero lo que quiero es que al iniciar aparezca el lienzo vacío jaja, saludos!
    '''def iniciarCanvas(self):
        f = Figure(figsize=(4,2.5),dpi = 100)
        canvas = FigureCanvasTkAgg(f,master = self.v)
        canvas.get_tk_widget().grid(row = 3, column = 0, columnspan = 2,pady = (40,40))'''

    def crearGrafico(self,val,cod):
        X = []
        Y = []
        f = Figure(figsize=(4,2.5),dpi = 100)
        a = f.add_subplot(111)
        if val == 'NRZ':
            for i in range(len(cod)):
                X.append(i)
                X.append(i+1)
                Y.append(cod[i])
                Y.append(cod[i])
            a.plot(X,Y)
        canvas = FigureCanvasTkAgg(f,master = self.v)
        canvas.get_tk_widget().grid(row = 3, column = 0, columnspan = 2,pady = (40,40))

    #Esta función controla el evento del combobox
    def selecciona(self, event):
        cod = []
        val = self.comboLineas.get()
        aux = self.txt.get()
        aux = list(aux)
        for i in aux:
            cod.append(int(i))
        self.crearGrafico(val,cod)

    def mostrarI(self):
        nombres = ['Maverick Martinez ', 'Luis Irias','Mario Zavala', 'Luis Andino', 'Angel Bulnes']
        num_cuenta = ['20141001825','2015100','20161003851','20151003836','20161000007']
        self.acerca = Toplevel()
        self.acerca.geometry('250x250')
        self.acerca.configure(bg = '#2980b9')
        self.frame = Frame(self.acerca)
        ancho_a = self.acerca.winfo_screenwidth()
        alto_a = self.acerca.winfo_screenheight()
        self.frame.configure(width = 240 , height = 240, bg= '#ecf0f1')
        self.frame.grid(row = 0, column = 0, padx = (ancho_a*0.02, ancho_a*0.02), pady = (alto_a*0.05,alto_a*0.05))
        self.titulo = Label(self.frame,text = 'Integrantes')
        self.titulo.grid(row = 0, column = 0, columnspan = 2)

        i = 0
        for n in nombres:
            self.lbN = Label(self.frame, text = n)
            self.lbN.grid(row = i +1, column = 0, padx = (5,5), pady = (2,2))
            i += 1
        i = 0
        for num in num_cuenta:
            self.lbNum = Label(self.frame, text = num)
            self.lbNum.grid(row = i+1, column = 1, padx = (5,5), pady = (2,2))
            i+=1

if __name__ == "__main__":
    v = Interfaz()
    v.show()
