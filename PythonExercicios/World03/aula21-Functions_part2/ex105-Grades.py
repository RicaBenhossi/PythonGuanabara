from statistics import mean


def ClassGrades(*grades, status=False):
    """
    ClassGrades calculates the grades of a class, returning a dictionary having:
        - quantity of grade passed as a parameter;
        - Highest grade;
        - Lowest grade;
        - Status (optional) of the average grade [GOOD, REGULAR, BAD]

    Args:
        *grades: (tuple): all the grades (integer and float) passed as parameter.
        status (bool, optional): whether to return the status of the average grade of the class. Defaults to False.
    """

    average = mean(grades)
    results = dict()
    results['Average Grade:'] = average
    # Calculate average by hand.
    average_hand = 0
    for grade in grades:
        average_hand += grade
    average_hand /= len(grades)
    results['Average Grade (hand):'] = average_hand
    results['Quantity of grades:'] = len(grades)
    results['Highest grade:'] = max(grades)
    results['Lowest grade:'] = min(grades)
    if status:
        if average >= 7:
            results['Average Grade Status:'] = 'GOOD'
        elif average >= 5:
            results['Average Grade Status:'] = 'REGULAR'
        else:
            results['Average Grade Status:'] = 'BAD'

    return results


print(help(ClassGrades))
resp = ClassGrades(10, 2, 5.8, 2)
print(f'Class 1: {resp}\n')
resp = ClassGrades(10, 10, 5.8, 7, status=True)
print(f'Class 2: {resp}')
print('=' * 40)
for k, v in resp.items():
    print(k, v)
