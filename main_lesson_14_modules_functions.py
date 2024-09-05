# Constant
FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """
    Read a text file and return the list of to-do items.
    :param filepath:
    :return:
    """
    with open(filepath, "r") as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """
    Write the to-do item list in the text file.
    :param todos_arg:
    :param filepath:
    :return:
    """
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


# Anything that you want executed only when this script is executed,
# put under this block --> will not execute this part if
# called from another script (only execute if name is main file).
if __name__ == "__main__":
    print("Hello")
    print(get_todos())
