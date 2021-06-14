from claseProvincia import Provincia
from claseManejadorProvincias import ManejadorProvincias
from claseObjectEncoder import ObjectEncoder

#Enlaza el objectEncoder y el json con el manejador de provincias
class RespositorioProvincias:
    __conn=None
    __manejador=None

    def __init__(self, conn):
        self.__conn = conn
        lista=self.__conn.leerJSONArchivo()
        self.__manejador=ManejadorProvincias()
        self.__manejador.decodificarLista(lista)
   
    def obtenerListaProvincias(self):
        return self.__manejador.getListaProvincias()

    def agregarProvincia(self,provincia):
        self.__manejador.addProvincia(provincia)
        return provincia

    def grabarDatos(self):
        self.__conn.guardarJSONArchivo(self.__manejador.toJSON())