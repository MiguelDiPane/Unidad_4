import requests

class Cotizador:
    __url = None
    __solicitud = None
    __cotizaciones = None
 
    def __init__(self):
        self.__url = 'https://www.dolarsi.com/api/api.php?type=valoresprincipales'
        self.__solicitud = None
        self.__cotizaciones = None

    def conectar(self):
        self.__solicitud = requests.get(self.__url)
        self.__cotizaciones = self.__solicitud.json()

    #nombre indica el nombre de la cotizacion, ejemplo oficial
    def getTipos(self):
        tipos = []
        for tipo in self.__cotizaciones:
            nombre = tipo['casa']['nombre'].lower()
            if nombre.find('dolar') != -1:
                tipos.append(tipo['casa']['nombre'])
        return tipos
    
    def getPrecioVenta(self,nombre):
        i = 0
        esta = False
        while i < len(self.__cotizaciones) and not esta:
            nomCotizacion = self.__cotizaciones[i]['casa']['nombre']
            if nomCotizacion.lower() == nombre.lower():
                esta = True
            else:
                i += 1
        cotizacion = self.__cotizaciones[i]['casa']['venta']
        if cotizacion.lower() != 'no cotiza':
            #reemplazo la , por . y retorno un flotante
            cotizacion = cotizacion.replace(',','.')
            cotizacion = float(cotizacion)
        return cotizacion

    def getPrecioCompra(self,nombre):
        i = 0
        esta = False
        while i < len(self.__cotizaciones) and not esta:
            nomCotizacion = self.__cotizaciones[i]['casa']['nombre']
            if nomCotizacion.lower() == nombre.lower():
                esta = True
            else:
                i += 1
        cotizacion = self.__cotizaciones[i]['casa']['compra']
        if cotizacion.lower() != 'no cotiza':
            #reemplazo la , por . y retorno un flotante
            cotizacion = cotizacion.replace(',','.')
            cotizacion = float(cotizacion)
        return cotizacion

