# Diccionario para almacenar los números y sus clasificaciones
numbers = {}

# Lista de tuplas para las clasificaciones
classifications = [(lambda x: x % 15 == 0, "Type 3"), 
                   (lambda x: x % 3 == 0, "Type 1"), 
                   (lambda x: x % 5 == 0, "Type 2"),
                   (lambda x: True, lambda x: str(x))
                  ]


def add_number(num):
    for check, type in classifications:
        if check(num):
            try:
                result = type(num)
            except TypeError:
                result = type
            numbers[num] = result
            return {num: result}


def get_number(num):
    if num in numbers:
        return {num: numbers[num]}
    else:
        return {"error": "Number not found"}


def get_all():
    return numbers
