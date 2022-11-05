class Tienda():
    def __init__(self,name):
        self.name = name
        self.productos =[]
    def agregar_producto(self,nuevo_producto):
        self.productos.append(nuevo_producto)
        
    def imprimir_productos(self):
        print('CODIGO       NOMBRE        CATEGORIA       PRECIO')
        for producto in self.productos:
            producto.print_info()
    
    def vender_producto(self,identificador):
        for producto in self.productos:
            if producto.id == str(identificador):
                producto.print_info()
                self.productos.remove(producto)
                print(f'{producto.name} fue vendido')
        print ('')

                
    def inflacion(self,porcentaje_aumento):
        for producto in self.productos:
            producto.actualizar_precio(porcentaje_aumento,True)
        print ('')
    
    def hacer_liquidcacion(self,categoria,porcentaje_descuento):
        for producto in self.productos:
            if producto.category == categoria:
                producto.actualizar_precio(porcentaje_descuento,False)
        print ('')
                

