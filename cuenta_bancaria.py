class CuentaBancaria:
    #Lista que acumula todas los objetos de la clase (instancias)
    instancias = []
    
    def __init__(self, name, tasa_interes = 1, balance = 0): 
        self.name = name
        self.ta = tasa_interes
        self.balance = balance
        CuentaBancaria.instancias.append(self) #Cada vez que se agrega un objeto se suma a la lista
        
    def deposito(self, amount):
        self.balance += amount
        print(f'Depositaste {amount} a tu cuenta')
        return self
    
    def retiro(self, amount):
        if amount>self.balance:
            self.balance -= 5
            print('Fondos insuficientes: cobrando una tarifa de $5')
        else:
            self.balance -= amount
            print(f'Retiraste {amount} a tu cuenta')
        return self
    
    def mostrar_balance(self):
        print(f'Balance: ${self.balance}')
        return self
    
    def generar_interes(self):
        if self.balance>0:
            self.balance = self.balance + (self.balance * self.ta) 
            print(f'Tu nuevo balance es {self.balance}. TASA DE INTERES: {self.ta}')
            return self
        else:
            print('Fondos insuficientes')
            return self
        
    #Bonus: imprime todas las instancias de la informacion de la cuenta
    @classmethod
    def mostrar_instancias(cls):
        for inst in CuentaBancaria.instancias: #por cada instancia en la clase... 
            print(f'Nombre: {inst.name} | Balance: {inst.balance}') #muestra el nombre y el balance