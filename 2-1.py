def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError as e:
            return e

    return inner

contacts = dict()

def parser(user_input):
    if user_input.startswith('add'):
        command, name, phone = user_input.split(' ') # add Edd 14324
        return add_handler(name, int(phone))
    elif user_input.startswith('change'):
        command, name, phone = user_input.split(' ') # change Edd 654332
        return change_handler(name, phone)

@input_error
def add_handler(name, phone):
    if name in contacts:
        raise KeyError('Name already in contacts')
    contacts[name] = phone
    return 'User added!'

@input_error
def change_handler(name, new_phone):
    if name in contacts:
        contacts[name] = new_phone
        return f'Phone number for user {name} changed'
    raise KeyError('Name is not in contacts')

def main():
    while True:
        user_input = input(">>>")
        if user_input in ['exit', 'bye']:
            print("Good bye!")
            break
        print(parser(user_input))

main()