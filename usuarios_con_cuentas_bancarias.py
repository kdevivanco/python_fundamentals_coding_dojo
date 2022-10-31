import random 

class CuentaBancaria:
    todas_las_cuentas = []
    todos_los_numeros = []
    
    def __init__(self, name, tasa_interes = 1, balance = 0): 
        self.name = name
        self.ta = tasa_interes
        self.balance = balance
        self.generar_numero()
        CuentaBancaria.todas_las_cuentas.append(self)
        CuentaBancaria.todos_los_numeros.append(self.nrodecuenta)
        
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
    
    def show_name(self):
        return self.name
    
        
    def generar_numero(self):
        self.nrodecuenta = ''
        for i in range(10):
            self.nrodecuenta += str(random.randint(0, 9))
        print('Numero de cuenta ' + self.nrodecuenta)



class Usuario: 
    instancias = []
    def __init__(self, titular):
        self.titular = titular
        Usuario.instancias.append(self.titular)
        self.cuentas = []
        self.cuentastuple = []

    def crear_cuenta(self,tipo):
        #tipo = input('Escoge tipo de cuenta(ahorros, corriente): ')
        self.cuentas.append(CuentaBancaria(tipo))
        print(f'Cuenta en {tipo} creada!')
        nrodecuenta = ''
    
    def verificacion_cuenta(self,numero_de_cuenta): #Se agrego metodo verificacion_cuenta: nos retorna la cuenta correspondiente al nro
        for i in range(len(self.cuentas)):
            if  str(self.cuentas[i].nrodecuenta) == str(numero_de_cuenta):
                return self.cuentas[i]
            else:
                print('Cuenta no encontrada')
            
    def hacer_deposito(self,amount,numero_de_cuenta):
        cuenta = self.verificacion_cuenta(numero_de_cuenta)
        cuenta.deposito(amount)

    def hacer_retiro(self,amount,numero_de_cuenta):
        cuenta = self.verificacion_cuenta(numero_de_cuenta)
        cuenta.retiro(amount)
        
    def mostrar_balance(self,numero_de_cuenta):
        cuenta = self.verificacion_cuenta(numero_de_cuenta)
        cuenta.mostrar_balance()

    def mostrar_cuentas(self): #Se modifico el metodo mostrar cuentas para mostrar la info completa
        i=0
        for i in range(len(self.cuentas)):
            cuenta = self.cuentas[i] #asignacion de variable para codigo mas limpio
            print(f'{self.titular}, {cuenta.name} {cuenta.nrodecuenta} | $ {cuenta.balance}')
            

    def transfer_dinero(self, nrousuario, nrodestinatario, amount): 
        nrousuario = input("Ingresa tu numero de cuenta: ")
        nrodestinatario = input("Ingresa numero de cuenta del destinatario: ")
        
        if nrodestinatario not in CuentaBancaria.todos_los_numeros:
            print('Esta cuenta no existe')
        else: 
            for cuenta in CuentaBancaria.todas_las_cuentas:
                verificacion = (f'El destinatario es: {cuenta.name}? Ingresa (Si o No)')
                respuesta = input(verificacion)
                
                if respuesta.lower() == 'si':
                    monto_a_depositar = input('Ingrese monto')
                    self.hacer_retiro(monto_a_depositar,nrousuario)
                    
                    
                else:
                    print('Vuelva a intentarlo')
                    break
#Proximos pasos: 
#1. Agregar funcion "verificacion" donde se verifica que el numero de cuenta ingresado es correcto
#2. Agregar esta funcion a cada metodo de CuentaBancaria o Usuario (por verse) para no tener que repetir codigo
#3. Terminar de construir el metodo transferir dinero 


