task_list = []

def insert_elements(task):
    task_list.append(task)

def print_elements():
    number = 0
    for task in task_list:
        number = number + 1
        print(number,task)

#Test
insert_elements('Aufstehen')
insert_elements('Duschen')
insert_elements('Frühstück')
insert_elements('Arbeit')
insert_elements('Coden')
insert_elements('Koten')
print_elements()
