import datetime

thisTime = datetime.datetime.now()

class Tienda:
    countTienda = 0 #Counter

    def __init__(self, direccion, provincia, region, telefono="none"):
        # Public variables
        self.direccion = direccion
        self.provincia = provincia
        self.region = region
        self.fechaCreacion = thisTime.date()
        self.telefono = telefono

        # Private variable
        self.__id = Tienda.countTienda + 1
        Tienda.countTienda += 1 # Increment the counter
        
        print(f"SE CREO TIENDA {self.__id}:")
        print(f"Dirección: \t\t{self.direccion} \nProvincia: \t\t{self.provincia} \nRegion: \t\t{self.region} \nTeléfono: \t\t{self.telefono} \nFecha de creación: \t{self.fechaCreacion}", end="\n\n")

    # Public method
    def get_info(self):
        print(f"INFORMACIÓN TIENDA {self.__id}:")
        print(f"Dirección: \t\t{self.direccion} \nProvincia: \t\t{self.provincia} \nRegion: \t\t{self.region} \nTeléfono: \t\t{self.telefono} \nFecha de creación: \t{self.fechaCreacion}", end="\n\n")

    def get_direccion(self):
        return self.direccion

    def set_tlf(self, tlf):
        self.telefono = tlf
    

'''
p1 = Tienda("direccion1", "provincia1", "region1")
p2 = Tienda("direccion2", "provincia2", "region2", "995847852")

p2.get_info()
p1.set_tlf("000258965")
p1.get_info()
print(p2.get_direccion())

print(Tienda.countTienda)  # Print counter
'''

class Producto:
    countProducto = 0 #Counter

    def __init__(self, descripcion, codigo, precioVenta, tiendaRelacionada, cantidad=0):
        # Public variables
        self.descripcion = descripcion
        self.codigo = codigo
        self.precioVenta = precioVenta
        self.tiendaRelacionada = tiendaRelacionada # Foreing key
        self.cantidad = cantidad

        # Private variable
        self.__id = Producto.countProducto + 1
        Producto.countProducto += 1 # Increment the counter
        
        print(f"SE CREO PRODUCTO {self.__id}:")
        print(f"Código: \t\t{self.codigo} \nPrecio Venta: \t\t{self.precioVenta} \nCantidad: \t\t{self.cantidad} \nTienda Relacionada: \t{self.tiendaRelacionada} \nDescripción: \n{self.descripcion}", end="\n\n")

    # Public method
    def get_info(self):
        print(f"INFORMACIÓN TIENDA {self.__id}:")
        print(f"Código: \t\t{self.codigo} \nPrecio Venta: \t\t{self.precioVenta} \nCantidad: \t\t{self.cantidad} \nTienda Relacionada: \t{self.tiendaRelacionada} \nDescripción: \n{self.descripcion}", end="\n\n")

    def get_cant(self):
        return self.cantidad

    def set_cant(self, cant):
        self.cantidad = cant
    
p1 = Producto("kajsndasndkasj as asd asadsd as dasd1", "cod1", 25.30, "Mantaro")
p2 = Producto("kajsndasndkasj as asd asadsd as dasd1", "cod2", 15.30, "Sonea", 10)

print("\n\n\n")

p2.get_info()
p1.set_cant(5)
p1.get_info()
print(p2.get_cant())

print("\n\n\n")

print(Producto.countProducto)  # Print counter
