#Este trabajo pertenece a: KAYLA DE VIVANCO

class CuentaBancaria:
    # ¡No olvides agregar algunos valores predeterminados para estos parámetros!
    def __init__(self, name, tasa_interes = 1, balance = 0): 
        self.name = name
        self.ta = tasa_interes
        self.balance = balance
        # tu código aquí (recuerda, los atributos de instancia van aquí)
        # no te preocupes por la información del usuario aquí; pronto involucraremos la clase de usuario
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
        print(f'Balance: ${self.balance}, esta en {self.name}')
        return self
    def generar_interés(self):
        self.balance = self.balance + self.balance * self.ta 
        print(f'Tu nuevo balance es {self.balance}. TASA DE INTERES: {self.ta}')
        return self
    def showTipo(self):
        return self.name

class Usuario: 
    instancias = []
    def __init__(self, titular):
        self.titular = titular
        Usuario.instancias.append(self.titular)
        self.cuentas = []
        self.cuentastuple = []
        
    def crear_cuenta(self):
        moneda = input('Escoge moneda de cuenta(dolares,soles,euros): ')
        self.cuentas.append(CuentaBancaria(moneda))
        print(f'Cuenta en {moneda} creada!')
        
        
    
    def hacer_deposito(self,amount,indice):
        self.cuentas[indice].deposito(amount)
        
    def showCuentas(self):
        i=0
        for cuenta in self.cuentas:
            print(f'Cuenta n°{i} esta en {cuenta.showTipo()}')
            i+=1
    def cuentasdict(self):
        i=0
        for cuenta in self.cuentas:
            i+=1
            index = str(i)
            cuentatuple = (index,cuenta.name)
            self.cuentastuple.append(cuentatuple)
        
    
    def hacer_retiro(self,amount):
        pass
        
    def mostrar_balance(self):
        for cuenta in self.cuentas:
            
            cuenta.mostrar_balance()
        
    def transfer_dinero(self, other_user, amount): 
        pass
    
    def nombrar_cuentas(self):
        print(self.cuentas)
