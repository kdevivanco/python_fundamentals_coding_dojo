from tienda import Tienda
from producto import Producto



mercattino = Tienda('Mercattino')


queso = Producto('Queso',18,'Lacteos')
pan_de_molde = Producto('Pan de molde',9,'Panes')
pan_frances = Producto ('Pan Frances',1,'Panes')
fresa = Producto('Fresa',10,'Fruta')
papaya = Producto('Papaya',5,'Fruta')

mercattino.agregar_producto(queso)
mercattino.agregar_producto(pan_de_molde)
mercattino.agregar_producto(pan_frances)
mercattino.agregar_producto(papaya)
mercattino.agregar_producto(fresa)


mercattino.imprimir_productos()

mercattino.vender_producto(105897)

mercattino.hacer_liquidcacion('Fruta',0.2)

mercattino.inflacion(.10)