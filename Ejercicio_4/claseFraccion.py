class Fraccion:
    __num = 0
    __den = 1

    def __init__(self,num=0,den=1):
        self.__num = num
        self.__den = den
    
    def getNumerador(self):
        return self.__num
    def getDenominador(self):
        return self.__den
    
    def simplificar(self):
        resto_division = self.__num % self.__den
        if resto_division != 0:
            if self.__num < self.__den:
                i = self.__num
                while i > 1:
                    num_resto = self.__num % i
                    den_resto = self.__den % i
                    if num_resto == 0 and den_resto == 0:
                        self.__num = self.__num / i
                        self.__den = self.__den / i
                    i -= 1
            elif self.__num > self.__den:
                i = self.__den
                while i > 1:
                    num_resto = self.__num % i
                    den_resto = self.__den % i
                    if num_resto == 0 and den_resto == 0:
                        self.__num = self.__num / i
                        self.__den = self.__den / i
                    i -= 1
        else:
            self.__num = self.__num / self.__den
            self.__den = 0

    def __str__(self):
        if self.__den != 0:
            cadena = str(int(self.__num))+'/'+str(int(self.__den))
        else:
            cadena = str(int(self.__num))
        return cadena 

    def getValor(self):
        return self.__num / self.__den

    #----------------------------#
    #  Sobrecarga de operadores  #
    #----------------------------#

    #suma
    def __add__(self, otro):
        if isinstance(otro,Fraccion):
            newNum1 = self.__num * otro.__den
            newNum2 = otro.__num * self.__den
            newDen = self.__den * otro.__den 
            return Fraccion(newNum1+newNum2,newDen)
        elif isinstance(otro,int) or isinstance(otro,float):
            newNum = self.__den * otro + self.__num
            return Fraccion(newNum,self.__den)

    #Resta
    def __sub__(self,otro):
        if isinstance(otro,Fraccion):
            newNum1 = self.__num * otro.__den
            newNum2 = otro.__num * self.__den
            newDen = self.__den * otro.__den      
            return Fraccion(newNum2-newNum1,newDen)
        elif isinstance(otro,int) or isinstance(otro,float):
            newNum = self.__den * otro - self.__num
            return Fraccion(newNum,self.__den)       

    #Multiplicacion
    def __mul__(self,otro):
        if isinstance(otro,Fraccion):    
            return Fraccion(self.__num * otro.__num,self.__den * otro.__den)
        elif isinstance(otro,int) or isinstance(otro,float):
            return Fraccion(self.__num * otro,self.__den)           

    #Division
    def __truediv__(self,otro):
        if isinstance(otro,Fraccion):    
            return Fraccion(self.__num * otro.__den,self.__den * otro.__num)
        elif isinstance(otro,int) or isinstance(otro,float):
            return Fraccion(self.__num * otro,self.__den)        




