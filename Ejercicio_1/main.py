from tkinter import *
from tkinter import ttk, messagebox, font

class Aplicacion():
    __ventana = None
    __altura = None
    __peso = None
    __imc = None
    __composicion = None

    def __init__(self):
        #Configuraciones de la ventana
        self.__ventana = Tk()
        self.__ventana.geometry('400x200')
        self.__ventana.title('Calculadora de IMC')
        self.__ventana.resizable(0, 0)

        #Variables
        self.__altura = StringVar()
        self.__peso = StringVar()
        self.__imc = StringVar()
        self.__composicion = StringVar()

        #Titulo central
        ttk.Label(text="Calculadora de IMC").grid(column=0,row=0,columnspan=2)
        
        #Frame con los input
        frameInputs = ttk.Frame(self.__ventana) 
        frameInputs.grid(column=0,row=1,columnspan=2)
        frameInputs.columnconfigure(0,weight = 1)
        frameInputs.rowconfigure(0,weight = 1)
        frameInputs['borderwidth'] = 2
        frameInputs['relief'] = 'groove'

        #Fila 1
        ttk.Label(frameInputs,text="Altura:").grid(column=0,row=0)
        self.alturaEntry = ttk.Entry(frameInputs,width=50,textvariable=self.__altura)
        self.alturaEntry.grid(column=1,row=0)
        ttk.Label(frameInputs,text="cm").grid(column=2,row=0)

        #Fila 2
        ttk.Label(frameInputs,text="Peso:").grid(column=0,row=1)
        self.pesoEntry = ttk.Entry(frameInputs,width=50,textvariable=self.__peso)
        self.pesoEntry.grid(column=1,row=1)
        ttk.Label(frameInputs,text="kg").grid(column=2,row=1)        
        
        #Agrego paddings internos a los elementos del frame
        for hijo in frameInputs.winfo_children():
            hijo.grid_configure(padx = 5, pady = 5)
        
        #Botones
        ttk.Button(self.__ventana,text="Calcular",command=self.calcular).grid(column=0,row=2,pady=10)
        ttk.Button(self.__ventana,text="Limpiar", command=self.limpiar).grid(column=1,row=2,pady=10)
        
        #Frame con los resultados
        frameResultados = ttk.Frame(self.__ventana, padding="3 3 12 12") #izquierda arriba derecha abajo
        frameResultados.grid(column=0,row=3,columnspan=2)
        frameResultados.columnconfigure(0,weight = 1)
        frameResultados.rowconfigure(0,weight = 1)

        #Resultados
        fuenteIMC = font.Font(size = 10,weight='bold')
        fuenteComp = font.Font(size = 12)
        ttk.Label(frameResultados,text="Tu indice de masa corporal es:").grid(column=0,row=0)
        ttk.Label(frameResultados,textvariable=self.__imc, font=fuenteIMC).grid(column=1,row=0)
        ttk.Label(frameResultados,textvariable=self.__composicion, font=fuenteComp).grid(column=0,row=1, columnspan=2)

        self.alturaEntry.focus()
        self.__ventana.mainloop()

    def calcular(self):
        try:
            #Calculo IMC
            altura = float(self.alturaEntry.get())
            peso = float(self.pesoEntry.get())
            imc = peso / altura**2
            imc = round(imc,2)
            #averiguo composicion corporal
            if imc < 18.5:
                composicion = "Peso inferior al normal"
            elif imc >= 18.5 and imc < 25:
                composicion = "Peso normal"
            elif imc >= 25 and imc < 30:
                composicion = "Peso superior al normal"
            else:
                composicion = "Obesidad"
            
            self.__imc.set(str(imc) + ' kg/m2')
            self.__composicion.set(composicion)

        except ValueError:
            messagebox.showerror(title='Error de tipo',
                                    message='Debe ingresar valores numericos')

    def limpiar(self):
        self.__altura.set('')
        self.__peso.set('')
        self.__composicion.set('')
        self.__imc.set('')

def testAPP():
    mi_app = Aplicacion()

if __name__ == '__main__':
    testAPP()