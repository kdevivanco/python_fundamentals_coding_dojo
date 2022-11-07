from listas_simples_enlazadas import SLList
from listas_simples_enlazadas import SLNode


#testing: 
my_list = SLList()

my_list.add_to_front('Kayla').add_to_front('Maria').add_to_back('Adriana').add_to_front('Lupe')

my_list.print_values()

print('')
print('Testing insert values...')
print('')

my_list.insert_val('Maia',2)

my_list.print_values()


print('')
print('Testing remove values...')
print('')

my_list.remove_from_back()

my_list.print_values()

print('')
print('Testing remove values...')
print('')

my_list.remove_from_back()

my_list.print_values()
print('')
print('Testing remove values...')
print('')

my_list.remove_from_back()

my_list.print_values()

print('')
print('Testing remove values...')
print('')

my_list.remove_from_back()

my_list.print_values()

print('')
print('Testing remove values...')
print('')

my_list.remove_from_back()

my_list.print_values()

print('')
print('Testing to see that SLList is now empty...')
print('')


my_list.create_index() #No funciona, sigue habiendo un elemento None