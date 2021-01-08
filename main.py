import random


def get_password_components_as_list():
    password_components = "a b c d e f g h i j k l m n o p q r" \
                          "s t u v w x y z 1 2 3 4 5 6 7 8 9"

    return password_components.split(" ")


def generate_password(password_components: list) -> list:
    result = []

    for item in range(len(password_components)):
        result.append(random.choice(password_components))

    return result


def convert_list_to_string(simple_list: list) -> str:
    list_as_string = ""

    for item in simple_list:
        list_as_string += item

    return list_as_string


def convert_password_to_binary(password_input: str) -> str:
    return ''.join(format(ord(i), 'b') for i in password_input)


def setup_password():
    components_of_list = get_password_components_as_list()
    password_as_list = generate_password(components_of_list)
    password_as_string = convert_list_to_string(password_as_list)

    return password_as_string


password = setup_password()
binary_password = convert_password_to_binary(password)

print(password)
print(binary_password)

