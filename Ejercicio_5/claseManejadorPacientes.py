from clasePaciente import Paciente

class ManejadorPacientes:
    indice = 0
    __pacientes = None

    def __init__(self):
        self.__pacientes = []
    
    def agregarPaciente(self,paciente):
        paciente.rowid = ManejadorPacientes.indice
        ManejadorPacientes.indice += 1
        self.__pacientes.append(paciente)
    
    def getListaPacientes(self):
        return self.__pacientes
    
    def deletePaciente(self,paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__pacientes.pop(indice)
    
    def updatePaciente(self,paciente):
        indice = self.obtenerIndicePaciente(paciente)
        self.__pacientes[indice] = paciente
    
    def obtenerIndicePaciente(self,paciente):
        bandera = False
        i = 0
        while i < len(self.__pacientes) and not bandera:
            if self.__pacientes[i].rowid == paciente.rowid:
                bandera = True
            else:
                i += 1
        return i 
    
    def toJSON(self):
        lista = [paciente.toJSON() for paciente in self.__pacientes]
        return lista

    def decodificarLista(self, lista):
        for paciente in lista:
            class_name=paciente['__class__']
            class_=eval(class_name)
            atributos=paciente['__atributos__']
            newPaciente=class_(**atributos)
            self.agregarPaciente(newPaciente)
