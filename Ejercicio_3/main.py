from tkinter import *
from tkinter import ttk
from datetime import datetime
from claseCotizador import Cotizador

class Aplicacion():
    __ventana = None
    __compras = []
    __ventas = []
    __fecha = None
    __cotizador = None
    __labels_compra = []
    __labels_venta = []

    def __init__(self):
        #Configuraciones de la ventana
        self.__ventana = Tk()

        self.__ventana.title('Cotizaciones del dolar')
        self.__ventana.resizable(0, 0)

        #Atributos
        self.__compras = []
        self.__ventas = []
        self.__fecha = StringVar()
        self.__cotizador = Cotizador()
        self.__cotizador.conectar() #Hace el request a la url
        self.__labels_compra = []
        self.__labels_venta = []

        #-------------------------------------#
        #       Creo y ordeno elementos       #
        #-------------------------------------#
        #Frame
        self.marco = ttk.Frame(self.__ventana,borderwidth=2,relief='groove',padding='10 10 10 10')
        self.marco.grid(column=0,row=0)
       
        #Header
        self.label1 = ttk.Label(self.marco,text='Moneda')
        self.label2 = ttk.Label(self.marco,text='Compra')
        self.label3 = ttk.Label(self.marco,text='Venta')
        self.sep1   = ttk.Separator(self.marco,orient='horizontal')

        self.label1.grid(column=0,row=0,columnspan=2, padx=(0,150), sticky=W)
        self.label2.grid(column=2,row=0, padx=(0,30),sticky=W)
        self.label3.grid(column=3,row=0,sticky=W)
        self.sep1.grid(column=0,row=1, columnspan=4, sticky=(W,E))

        #Cuerpo
        i = 0
        for tipo in self.__cotizador.getTipos():
            compra = StringVar()
            venta = StringVar()
            self.__compras.append(compra)
            self.__ventas.append(venta)
            self.lbl_tipo = ttk.Label(self.marco,text=tipo)
            self.lbl_tipo.grid(column=0,row=i+2,columnspan=2, padx=(0,150), pady=(10,0), sticky=W)

            lbl_compra = ttk.Label(self.marco,textvariable=self.__compras[i])
            lbl_compra.grid(column=2,row=i+2, pady=(10,0), sticky=W)
            lbl_venta = ttk.Label(self.marco,textvariable=self.__ventas[i])
            lbl_venta.grid(column=3,row=i+2, pady=(10,0), sticky=W)
            self.__labels_compra.append(lbl_compra)
            self.__labels_venta.append(lbl_venta)
            i += 1
        self.sep2 = ttk.Separator(self.marco,orient='horizontal')
        self.sep2.grid(column=0,row=i+3, columnspan=4, pady=(10,0), sticky=(W,E))

        #Footer
        self.btnActualizar = ttk.Button(self.marco,text="Actualizar", command=self.actualizar)
        self.lbl_fecha = ttk.Label(self.marco, textvariable=self.__fecha)

        self.btnActualizar.grid(column=0,row=i+4, padx=(0,150), pady=(10,0), sticky=W)
        self.lbl_fecha.grid(column=1,row=i+4,columnspan=3, pady=(10,0), sticky=W)         
        
        #Llamo a actualizar para inicializar los valores al arrancar la aplicacion
        self.actualizar()

        self.__ventana.mainloop()

    def actualizar(self):
        self.__cotizador.conectar() #Hace el request a la url
        i = 0
        for tipo in self.__cotizador.getTipos():
            compra = self.__cotizador.getPrecioCompra(tipo)
            venta = self.__cotizador.getPrecioVenta(tipo)
            self.__compras[i].set(compra)
            self.__ventas[i].set(venta)
            i += 1
        fecha = datetime.today()
        fecha = fecha.strftime('%d/%m/%Y, %H:%M:%S')
        self.__fecha.set('Actualizado ' + fecha)

def testAPP():
    mi_app = Aplicacion()

if __name__ == '__main__':
    testAPP()