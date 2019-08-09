def validated_name(name):
    """
    validated_name returns if the name informed is valid (Only lettres, no space at begening and at the end, no commas)

    Args:
        name (string): receive the name that user has informed.

    Returns:
        String: returns the error that was found to be print.
    """
    pass
    return ''


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
        return 'Age must be and integer value.'
    else:
        if valid_age <= 0:
            return 'Age must be higher than ZERO.'
        else:
            return valid_age


# age = input('age:')
# message = validated_age(age)
# if message == '':
#     print('ok')
# else:
#     print(message)
