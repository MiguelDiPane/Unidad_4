import requests

class Clima:
    __url = None
    __key = None

    def __init__(self):
        self.__url = 'https://api.openweathermap.org/data/2.5/weather?q={San Juan},AR&units=metric&appid={564c4c901948a8f08a60d25f7a11040a}'

    def conectar(self,nombreCiudad):
        self.__solicitud = requests.get(self.__url)
        climaProvincia = self.__solicitud.json()
        print(climaProvincia)


    def getTemperatura(self,nombreCiudad):
        pass
    def getTermina(self,nombreCiudad):
        pass
    def getHumedad(self,nombreCiudad):
        pass       

clima = Clima()
clima.conectar('San Juan')