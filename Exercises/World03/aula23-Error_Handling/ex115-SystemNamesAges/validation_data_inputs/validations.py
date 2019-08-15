def validated_name(name):
    """
    validated_name returns if the name informed is valid (Only lettres, no space at begening and at the end, no commas)

    Args:
        name (string): receive the name that user has informed.

    Returns:
        String: returns the error that was found to be print.
    """
    try:
        if not name:
            return False, 'Type a name to the new person.'
        elif (not name.isalpha()) and (has_forbiden_special_char(name)):
            return False, 'Name must contains only lettres and "-"'
        elif name.isnumeric() or has_numbers_inside_string(name):
            return False, 'Number are not allowed in Name.'
        elif (name[0] == '-' or (name[(len(name) - 1)] == '-')):
            return False, 'Name can not start or end with "-" (dash)'
        elif '-' in name:
            if name[(name.index('-') + 1)] == '-':
                return False, 'Name can not contain more than 1 "-" (dash) in sequence.'
        elif ' ' in name:
            no_space_name = " ".join(name.split())
            if no_space_name != name:
                return False, 'Name must not have more than one space in sequence.'
    except ValueError:
        return False, '"Name" must be a string.'
    else:
        return True, None


def has_forbiden_special_char(name):
    invalid_chars = '!@#$%^&*()\{\}[]|\\~:;?><,./`\'\"_+='
    return any(char in invalid_chars for char in name)


def has_numbers_inside_string(name):
    return any(char.isdigit() for char in name)


def validated_age(age):
    """
    validated_age reurn if the informed age is valid (integer, not null and higher than zero)

    Args:
        age (string): receive the age that user has informed.

    Returns:
        String: returns the error that was found to be print.
    """
    try:
        valid_age = int(age)
    except ValueError:
        return False, 'Age must be and integer value.'
    else:
        if valid_age <= 0:
            return False, 'Age must be higher than ZERO.'
        else:
            return valid_age


# age = input('age:'
# message = validated_age(age)
# if message == '':
#     return False, 'ok'
# else:
#     return message)
