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



#Crea dos cuentas: 

cuenta1 = CuentaBancaria('Kayla Soles', 0.1, 200)

cuenta2 = CuentaBancaria('Maria Soles', 0.05,300)

#Para la primera cuenta, haz 3 depósitos y 1 retiro, luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)

cuenta1.deposito(300).deposito(1000).deposito(300).retiro(500).generar_interes().mostrar_balance()

#Para la segunda cuenta, haz 2 depósitos y 4 retiros, luego genera intereses y muestra la información de la cuenta, todo en una línea de código (es decir, encadenando)

cuenta2.deposito(300).deposito(1000).retiro(300).retiro(500).retiro(60).retiro(250).generar_interes().mostrar_balance()

#BONUS NINJA: utiliza un método de clase para imprimir todas las instancias de la información de una cuenta bancaria

CuentaBancaria.mostrar_instancias()