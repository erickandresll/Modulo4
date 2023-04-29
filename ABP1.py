class bodega:
    def __init__(self, producto, precio, unidad):
        self.producto = producto
        self.precio = precio
        self.unidad = unidad
        
    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio
        
    def stock(self):
        return f"El stock de {self.producto} es {self.unidad}"
    
    def agregar_producto(self, nuevo_producto, nuevo_precio, nueva_unidad):
        self.producto = nuevo_producto
        self.precio = nuevo_precio
        self.unidad = nueva_unidad
                    
class venta: 
    def __init__(self, producto, unidad, lugar_venta):
        self.producto = producto
        self.unidad = unidad
        self.lugar_venta = lugar_venta
    
    def registrar_venta(self, cantidad, precio):
        total = cantidad * precio
        return f"Venta registrada de {self.producto} por {cantidad} en {self.lugar_venta}. Total a pagar: {total}"
    
    def historial_ventas(self):
        return f"Productos vendidos {self.producto}"
    
    def actualizar_venta(self, id_venta, nuevos_datos):
        return f"La venta con ID {id_venta} ha sido actualizada con los siguientes datos: {nuevos_datos}"
    
        
class cliente:
    def __init__(self, nombre, cantidad, total_pagar):
        self.nombre = nombre
        self.cantidad = cantidad
        self.total_pagar = total_pagar
    
    def realizar_compra(self, producto, cantidad, precio):
        total = cantidad * precio 
        return f"Compra realizada por {self.nombre} de {cantidad} {producto} por un total de {total}."
    
    def historial_compras(self):
        return f"Este es el historial de compras de {self.nombre}"
    
    def actualizar_datos(self, nuevos_datos):
        for k, v in nuevos_datos.items():
            setattr(self,k,v)
        return f"Los datos del cliente {self.nombre} han sido actualizados."        
        
bodega_chile = bodega("Notebook", 400000, 10)

print(bodega_chile.stock()) 
bodega_chile.actualizar_precio(500000)
print(bodega_chile.precio)

venta_1 = venta("Notebook", 1, "Tienda 1")
print(venta_1.registrar_venta(1,400000))
print(venta_1.historial_ventas())
print(venta_1.actualizar_venta(1, "Impresora"))

cliente_1 = cliente("Juan", 1, 400000)
print(cliente_1.realizar_compra("Notebook", 1, 400000))
print(cliente_1.historial_compras())
print(cliente_1.actualizar_datos({"cantidad": 2, "total_pagar": 800000}))


