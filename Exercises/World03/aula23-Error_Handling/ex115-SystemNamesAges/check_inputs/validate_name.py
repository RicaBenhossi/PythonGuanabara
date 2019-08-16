def validated_name(name):
    if name == '0':
        return False, None
    else:
        (name_is_valid, data_to_print) = validated_name_syntax(name)
        if not name_is_valid:
            return False, data_to_print
        else:
            return True, f'Name: {data_to_print}'


def validated_name_syntax(name):
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
        return True, name


def has_forbiden_special_char(name):
    invalid_chars = '!@#$%^&*()\{\}[]|\\~:;?><,./`\'\"_+='
    return any(char in invalid_chars for char in name)


def has_numbers_inside_string(name):
    return any(char.isdigit() for char in name)
