import requests

class Cotizador:
    __url = None
    __solicitud = None
    __cotizaciones = None
 
    def __init__(self):
        self.__url = 'https://www.dolarsi.com/api/api.php?type=dolar'
        self.__solicitud = requests.get(self.__url)
        self.__cotizaciones = self.__solicitud.json()

    #nombre indica el nombre de la cotizacion, ejemplo oficial
    def getCotizacion(self,nombre):
        i = 0
        esta = False
        while i < len(self.__cotizaciones) and not esta:
            nomCotizacion = self.__cotizaciones[i]['casa']['nombre']
            if nomCotizacion.lower() == nombre.lower():
                esta = True
            else:
                i += 1
        cotizacion = self.__cotizaciones[i]['casa']['venta']
        #reemplazo la , por . y retorno un flotante
        cotizacion = cotizacion.replace(',','.')
        cotizacion = float(cotizacion)
        return cotizacion

     

