import random
class Producto():
    def __init__(self,name,price,cat):
        self.name = name
        self.price = price
        self.category = cat
        self.id = self.crear_codigo()
        
    def crear_codigo(self):
        self.id = '10'
        for i in range(4):
            num = random.randint(1, 9)
            self.id += str(num)
        return self.id
        
    def actualizar_precio(self,cambio_porcentaje,esta_elevado):
        if esta_elevado == True:
            self.price += self.price * cambio_porcentaje
        elif esta_elevado == False:
            self.price -= self.price * cambio_porcentaje
        else:
            print('Por favor indicar True/False')
        print(f'El nuevo precio de {self.name} es: {self.price}')
        
    def print_info(self):
        print(f'{self.id}       {self.name}        {self.category}             ${self.price}')
        print('') #line jump
