# Declare a list that holds all ToDo items
todos = []

while True:
    # Get choice from user whether user wants to add new item, show the list or exit the program
    user_action = input("Type add, show, edit or exit: ")

    # Remove any spaces in choice i.e. to make add == add(space)
    user_action = user_action.strip()

    # Depeding on user choice add, show or exit program
    match user_action:
        case 'add':
            todo = input("Enter a todo: ")
            todos.append(todo)
        case 'show':
            for items in todos:
                print(items)
        case 'edit':
            edit_number = int(input("Enter the To-Do to be edited"))
            edit_number = edit_number-1
            new_item = input("Enter new To-Do item")
            todos[edit_number] = new_item
        case 'exit':
            break
        case _: # If user enters invalid choice
            print("Hey, you have entered an invalid choice") 
    
print("Bye!")
