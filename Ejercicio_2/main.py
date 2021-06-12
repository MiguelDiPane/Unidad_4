from tkinter import *
from tkinter import ttk, messagebox
from claseCotizador import Cotizador

class Aplicacion():
    __ventana = None
    __dolares = None
    __pesos = None
    __cotizador = None

    def __init__(self):
        #Configuraciones de la ventana
        self.__ventana = Tk()
        self.__ventana.geometry('300x130')
        self.__ventana.title('Conversor de moneda')
        self.__ventana.resizable(0, 0)

        #Atributos
        self.__dolares = StringVar()
        self.__pesos = StringVar()
        self.__cotizador = Cotizador()

        #Frame
        self.mainFrame = ttk.Frame(self.__ventana,borderwidth=2,relief='groove',padding='20 20 20 20')
        
        #Creo elementos
        self.label1 = ttk.Label(self.mainFrame,text='dólares')
        self.label2 = ttk.Label(self.mainFrame,text='pesos')
        self.label3 = ttk.Label(self.mainFrame,text='es equivalente a')
        self.label4 = ttk.Label(self.mainFrame,textvariable=self.__pesos)
        self.dolaresEntry = ttk.Entry(self.mainFrame,textvariable=self.__dolares, width=15)
        self.boton = ttk.Button(self.mainFrame,text="Salir", command=self.__ventana.destroy)
        
        #Ordeno elementos en la grilla
        self.mainFrame.grid(column=0,row=0)
        self.label1.grid(column=2,row=0)
        self.label2.grid(column=2,row=1)
        self.label3.grid(column=0,row=1)
        self.label4.grid(column=1,row=1)
        self.dolaresEntry.grid(column=1,row=0)
        self.boton.grid(column=2,row=2)

        #Calculo al momento de ingresar un valor en el campo de texto
        self.__dolares.trace('w',self.calcular)
        self.dolaresEntry.focus()
        self.__ventana.mainloop()

    def calcular(self,*args):
        if self.dolaresEntry.get() != '':
            try:
                ventaOficial = self.__cotizador.getCotizacion('oficial')
                dolares = float(self.dolaresEntry.get())
                pesos = ventaOficial * dolares
                self.__pesos.set(pesos)
            except ValueError:
                messagebox.showerror(title='Error de tipo',message='Debe ingresar un valor numérico')
        else:
            self.dolaresEntry.focus()
            self.__pesos.set('')

def testAPP():
    mi_app = Aplicacion()

if __name__ == '__main__':
    testAPP()