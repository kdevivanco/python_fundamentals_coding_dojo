
class SLList:
    def __init__(self):
        self.head = None #apunta a un nodo self.head = primer nodo 
        
    def add_to_front(self, val):
        new_node = SLNode(val) #crea un nuevo node
        current_head = self.head #Variable temporal 
        new_node.next = current_head #vuelve todo el objeto/nodo current el next (lo empuja)
        self.head = new_node  #establece el nuevo 
        return self
    
    def print_values(self):
        runner = self.head #nodo 1
        #a_list = [] mi metodo
        while runner != None: #osea que no es el ultimo nodo
            print(runner.value)
            runner = runner.next #hace que itere, pasando al siguiente
            #a_list.append(runner.value)
        #print(a_list)
        return self
    
    def add_to_back(self, val):
        # si la lista está vacía
        if self.head == None:
            self.add_to_front(val)
            return self
        #caso contrario... normal
        new_node = SLNode(val)
        runner = self.head #empezamos en la cabeza
        while (runner.next != None): #mientras no sea el ultimo, pasa al siguiente 
            runner = runner.next #cuando runner es el ultimo elemento 
        runner.next = new_node #el nuevo nodo va a ser runnner.next del utlimo elemento
        # print(f'Despues de {runner.value} se anade a {new_node.value}')
        return self
    
    def remove_from_front(self):
        print(f'{self.head.value} was removed')
        self.head = self.head.next
        print('Now in SLList:')
        self.print_values()
        
    def fetch_last(self):
        runner = self.head
        while runner != None: #osea que no es el ultimo nodo
            runner = runner.next 
            if runner.next == None: # ubicamos al ultimo nodo
                print(runner.value)
                return runner
        #last_element = runner
        #return last_element
        
    def remove_from_back(self):
        last_element = self.fetch_last()
        
        runner = self.head #nodo 1
        #a_list = [] mi metodo
        while runner != None: #osea que no es el ultimo nodo
            if runner.next == last_element: # ubicamos al ultimo nodo
                runner.next = None
                return self
            runner = runner.next 

    
    def remove_val(self,val):
        runner = self.head

        #if value is the first element... 
        if runner.value == val:
            self.remove_from_front()
            return self
        else: 
            while runner != None:
                #para no tener atributeerror: 
                if runner.next == None:
                    return #esto previene que se salga de la iteracion 
                if runner.next.value == val:
                    first = runner
                    to_delete = runner.next
                    runner.next = to_delete.next 
                    print(val)
                runner = runner.next  #dentro del while, fuera de los if
    
    def create_index(self): #funcion para crear e imprimir indices
        counter =  0
        runner = self.head #nodo 1
        while runner != None:
            print(runner.value,counter)
            runner.index = counter  #crea un nuevo atributo para los nodos: indice
            runner = runner.next 
            counter +=1
        return self

    def insert_val(self,val,index):
        self.create_index() #crea los indices
        runner = self.head 
        while runner != None:
            if runner.next == None: #Evita salirse del scope de la lista
                    return
            if runner.next.index == index: #si el indice que sigue al nodo actual es el taarget ...
                (print(f'The node at position {index} is {runner.next.value}')) #solo para ubicarme
                
                after_node = runner.next #nodo que le sigue al nuevo nodo creado, esta es una variable temporal
                            
                new_node = SLNode(val) #crea un nuevo nodo 
                new_node.next = after_node #insertamos todo lo que le sigue a este nuevo nodo usando la variable temporal
                runner.next = new_node #el que le sigue al runner ahora es ese nodo
                return #esto breaks the loop 
                
            runner = runner.next #itera 

class SLNode:
    def __init__(self,val):
        self.value = val
        self.next = None


