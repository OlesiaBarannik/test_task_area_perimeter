from area_perimeter import *

if __name__ == '__main__':
    str_input = input("Please, input info: ")
    class_name = str_input.split(" ")[0]

    try:
        class_instance = globals()[class_name](str_input)
        print(class_instance.get_Result())
    except KeyError:
        print(f"Class '{class_name}' not found.")
    except Exception as e:
        print(f"An error occurred when creating an instance of '{class_name}': {e}")
