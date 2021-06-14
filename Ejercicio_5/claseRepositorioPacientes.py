from clasePaciente import Paciente
from claseManejadorPacientes import ManejadorPacientes
from claseObjectEncoder import ObjectEncoder

class RepositorioPacientes:
    __conn = None
    __manejador = None

    def __init__(self,conn):
        self.__conn = conn
        lista = self.__conn.leerJSONArchivo()
        self.__manejador = ManejadorPacientes()
        self.__manejador.decodificarLista(lista)
    
    def obtenerListaPacientes(self):
        return self.__manejador.getListaPacientes()
    
    def agregarPaciente(self,paciente):
        self.__manejador.agregarPaciente(paciente)
        return paciente
    def modificarPaciente(self,paciente):
        self.__manejador.updatePaciente(paciente)
        return paciente
    def borrarPaciente(self,paciente):
        self.__manejador.deletePaciente(paciente)
    
    def grabarDatos(self):
        lista = self.__manejador.toJSON()
        self.__conn.guardarJSONArchivo(lista)