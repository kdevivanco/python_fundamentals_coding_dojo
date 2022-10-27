#Este trabajo pertenece a: KAYLA DE VIVANCO

#Solucion 1: 
x = [ [5,2,3], [10,8,9] ] 
estudiantes = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
directorio_deportes = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'futbol' : ['Messi', 'Ronaldo', 'Rooney']
}
z = [ {'x': 10, 'y': 20} ]

x[1][0] = 15
estudiantes[0]['last_name'] = "Bryant"
directorio_deportes['futbol'][0] = 'Messi'
z[0]['y']=30

#Solucion 2: 

estudiantes = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(some_list):
    pairlist = [] 
    mystring = ''
    for diccionario in some_list:                #para cada diccionario en la lista
        pairitem = list(diccionario.items())     #se crea un tuple de los key value pair
        pairlist.append(list(pairitem))          #Cada valor se append a la lista vacia
    
    for i in range(len(pairlist)):               #itera la lista y se crea un str vacio
        newlist = pairlist[i]                    #ademas crea una lista con los valores del par
        mysentence = ''
        for x,y in newlist:                      #por cada par se imprime: 
            mysentence += (f' {x} --- {y},') 
        print(mysentence[:-1])                   #esto se imprime dentro del segundo for para que se imprima una mysentence por diccionario y se le resta la ultima coma usando [:-1]

#Solucion 3

def iterateDictionary2(key_name, some_list):
    for diccionario in some_list:              #Por cada diccionario en la lista
        print(diccionario[key_name])           #imprime el valor asociado al argumento key_name


#Solucion 4


dojo = {
    'ubicaciones': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructores': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def printInfo(some_dict):
    for key in some_dict:                       #Por cada key en el argumento en some_dict
        valuelist = some_dict[key]              #valuelist = los valores de ese key 
        lengthoflist = len(valuelist)       
        print(f'{lengthoflist} {key.upper()}')  #imprime el largo de la lista de values + el nombre del key
        for some_value in valuelist:
            print (some_value)                  #por cada item (valor) en la lista imprime el valor
        print('')                               #line jump en el primer loop