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
        print(f'Depositaste {amount}')
        return self
    
    def retiro(self, amount):
        if amount>self.balance:
            self.balance -= 5
            print('Fondos insuficientes: cobrando una tarifa de $5')
            return 1
        else:
            self.balance -= amount
            print(f'Retiraste {amount}')
        return self
    
    def mostrar_balance(self):
        print(f'Balance: ${self.balance}')
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
        Usuario.instancias.append(self)
        self.cuentas = []
        self.cuentastuple = []

    def crear_cuenta(self):
        tipo = input('Escoge tipo de cuenta(ahorros, corriente): ')
        self.cuentas.append(CuentaBancaria(tipo))
        print(f'Cuenta en {tipo} creada!')
        nrodecuenta = ''
    
    def verificacion_cuenta(self,numero_de_cuenta):
        for i in range(len(self.cuentas)):
            if  str(self.cuentas[i].nrodecuenta) == str(numero_de_cuenta):
                return self.cuentas[i]
            else:
                print('Cuenta no encontrada')
                return False
                
    def verificacion_destinatario(self,numero_de_cuenta):
        for usuario in Usuario.instancias: #chequea todos los nro de cuenta
            for cuenta in usuario.cuentas: #por cuenta en instancia
                if str(cuenta.nrodecuenta) == str(numero_de_cuenta):
                    print('Esta cuenta existe!')
                    return cuenta, usuario #devuelve toda la cuenta objeto CuentaBancaria
            
    def hacer_deposito(self,amount,numero_de_cuenta):
        cuenta = self.verificacion_cuenta(numero_de_cuenta)
        cuenta.deposito(amount)

    def hacer_retiro(self,amount,numero_de_cuenta):
        cuenta = self.verificacion_cuenta(numero_de_cuenta)
        respuesta = cuenta.retiro(amount)
        return respuesta #nos devuelve un valor 1 si la transaccion fue denegada
        
    def mostrar_balance(self,numero_de_cuenta):
        cuenta = self.verificacion_cuenta(numero_de_cuenta)
        cuenta.mostrar_balance()

    def mostrar_cuentas(self):
        i=0
        for i in range(len(self.cuentas)):
            cuenta = self.cuentas[i]
            print(f'{self.titular}, {cuenta.name} {cuenta.nrodecuenta} | $ {cuenta.balance}')
            

    def transfer_dinero(self): 
        #Ingresa el usuario
        nrousuario = input("Ingresa tu numero de cuenta: ")
        
        #Verifica el usuario
        solicitud_numero = self.verificacion_cuenta(nrousuario)
        if solicitud_numero == False:
            return
        
        #Ingresa el destinatario
        nrodestinatario = input("Ingresa numero de cuenta del destinatario: ")
        
        #verifica el destinatario
        NoneType = type(None)
        res_verificacion = self.verificacion_destinatario(nrodestinatario)
        
        if NoneType == type(res_verificacion): 
            print('Cuenta no encontrada')
            return
        #Empieza la transaccion
        else: 
            cuenta,usuario = res_verificacion
            print(cuenta,usuario)
            #Verifica el nombre de destinatario
            verificacion = (f'El destinatario es: {usuario.titular}? Ingresa (Si o No)')
            respuesta = input(verificacion)
            if respuesta.lower() == 'si':
                monto_str = input('Ingrese monto')
                monto_a_depositar = int(monto_str)
                #Verifica el monto / retira de cuenta usuario
                solicitud_monto = self.hacer_retiro(monto_a_depositar,nrousuario)
                if solicitud_monto == 1: # denegada
                    print ('DENEGADO')
                    return
                else: #deposita (transfiere) al destinatario
                    usuario.hacer_deposito(monto_a_depositar,nrodestinatario)
            else: 
                print('Vuelva a intentarlo')
                return
                

