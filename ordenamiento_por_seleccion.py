

def selection_sort(some_list):
    index_counter = 0
    for num in some_list:
        index_min = some_list.index(min(some_list[index_counter:len(some_list)]))
        some_list[index_counter], some_list[index_min] =  some_list[index_min],some_list[index_counter]
        index_counter +=1
        #print(some_list)  # --> descomentar para ver como se imprime en cada iteracion
    return some_list

my_list=[8,9,0,1,3,4,5,7,2]
print(my_list)
print(selection_sort(my_list))