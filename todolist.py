# ToDoGen Project

import os
import sys

# Variables
currentInputIndex = 0
currentRetrievedText = ""
todos = {}
question = input(str("Would you like to revisit your 'old' to-do list or create a 'new' one?"))
# If old, open existing to do list
if question == "old":
    if os.path.exists("ToDoList.txt") and os.path.isfile("ToDoList.txt"):
        if os.name == "nt":
            # Windows
            os.system("start ToDoList.txt")

        elif os.name == "posix":
            # Linux
            os.system("open ToDoList.txt")
# If new, wipe to do list and create another one
if question == "new":
    maximumInputSize = input("Number of TODO list items: ")
    while currentInputIndex < int(maximumInputSize):
        currentInputIndex += 1
        currentRetrievedText = input(str(currentInputIndex) + ". ")

        todos.update({str(currentInputIndex): currentRetrievedText})

    if os.path.exists("ToDoList.txt") and os.path.isfile("ToDoList.txt"):
        open('ToDoList.txt', 'w')

    todoFile = open("ToDoList.txt", "a")

    todoFile.write("\n")
    for key, value in todos.items():
        todoFile.write(key + ". " + value + "\n")

    todoFile.close()

    if os.name == "nt":
        # Windows
        os.system("start ToDoList.txt")

    elif os.name == "posix":
        # Linux
        os.system("open ToDoList.txt")

    sys.exit("Program finished.")
