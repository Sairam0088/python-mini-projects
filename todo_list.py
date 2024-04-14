#to do list using python

tasks = []

def add_task(task):
    tasks.append(task)
    print(f"\nSuccessfully added {task} to the tasks")
def remove_task(task):
    tasks.remove(task)
    print(f"\nSuccessfully removed the {task} from tasks")
def display_tasks():
    if tasks:
        print('\nTodo List')
        for i,j in enumerate(tasks, start=1):
            print(f'{i}. {j}')
    else:
        print('No tasks pending')
        
while True:
    print('\n==Todo List==')
    print('1. Add Task')
    print('2. Remove Task')
    print('3. Display Tasks')
    print('4. Quit')
    choice = input('Enter your choice (1-4): ')
    if choice == '1':
        task = input('Enter a task to add: ')
        add_task(task)
    elif choice == '2':
        task = input('Enter a task to remove: ')
        remove_task(task)
    elif choice == '3':
        display_tasks()
    elif choice == '4':
        print('Quiting the game. Goodbye!')
        break
    else:
        print('Your choice is invaid. Please select a number between 1 and 4')
    