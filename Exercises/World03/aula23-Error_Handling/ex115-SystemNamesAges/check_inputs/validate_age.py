def validated_age(age):
    if age == '0':
        return False, None
    else:
        (age_is_valid, data_to_print) = validated_age_syntax(age)
        return age_is_valid, data_to_print


def validated_age_syntax(age):
    try:
        valid_age = int(age)
    except ValueError:
        return False, 'Age must be and integer value.'
    else:
        if valid_age <= 0:
            return False, 'Age must be higher than ZERO.'
        else:
            return True, f'Age: {valid_age}'
