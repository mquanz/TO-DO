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

print_elements()
print()

a = serialize()

print(a)
print()

insert_element('Koten')

print_elements()
print()

print(deserialize(a))

print_elements()
