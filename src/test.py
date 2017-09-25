from to_do import *

#Test
insert_element('Aufstehen')
insert_element('Duschen')
insert_element('Frühstück')
insert_element('Arbeit')
insert_element('Coden')
insert_element('Koten')

print_elements()
print()

delete_element(6)

print_elements()
print()

mark_done_element(1)
mark_done_element(2)

print(task_list[1].description, task_list[1].done)
print(task_list[3].description, task_list[3].done)
print()

print_elements()
print()

test = serialize()

print(test)
print()

deserialize(test)

print_elements()
