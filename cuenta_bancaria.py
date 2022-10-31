class CuentaBancaria:
    instanciascuenta = []
    def __init__(self, name, tasa_interes = 1, balance = 0): 
        self.name = name
        self.ta = tasa_interes
        self.balance = balance
        self.info = (f'nombre {self.name} | balance {self.balance}')

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
    def showinstances(self):
        CuentaBancaria.instanciascuenta.append(self.info)
        for instancia in CuentaBancaria.instanciascuenta:
            print(instancia)
