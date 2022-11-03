class Ninja:
    def __init__ (self, nombre, apellido, premios, comida_mascota, mascota):
        self.nombre = nombre
        self.apellido = apellido
        self.premios = premios
        self.comida_mascota = comida_mascota 
        self.mascota = Mascota(mascota, tipo = 'por definir', golosinas = 'por definir')

    def caminar(self):
        print('Vamos a pasear y a jugar')
        self.mascota.jugar()

    def alimentar(self):
        print(f'Vamos a alimentar a {self.mascota.name} con {self.comida_mascota}')
        self.mascota.comer()

    def banar(self):
        print(f'Vamos a banar a {self.mascota.name}')
        self.mascota.banar()

class Mascota: 
    def __init__(self, name,tipo,golosinas,energia = 50, salud = 50):
        self.name = name
        self.tipo = tipo
        self.golosinas = golosinas
        self.energia = energia
        self.salud = salud

    def dormir(self):
        print(f'{self.name} esta durmiendo')
        self.energia += 5 
        print(f'Energia subio a: {self.energia}')
    
    def comer(self):
        print(f'{self.name} está comiendo!')
        self.energia += 5
        self.salud += 10
        print(f'Energia subio a: {self.energia}')
        print(f'Salud subio a: {self.salud}')
    
    def jugar(self):
        print(f'Estas jugando con {self.name}')
        self.salud += 5
        print(f'Salud subio a: {self.salud}')
    
    def ruido(self):
        print(f'{self.name}: woof')

    
        
# implementa los siguientes métodos:
# caminar(): pasea a la mascota del ninja invocando el método de mascota jugar()
# alimentar(): alimenta a la mascota del ninja invocando el método de mascota comer()
# bañar(): limpia la mascota del ninja invocando el método de mascota sonido()
