# this function will
def interact_with_numbers():
    # this list contains
    numbers = []
    for i in range(5):
        num = int(input('Number: '))
        numbers.append(num)

    print('The first number is {}'.format(numbers[0]))
    print('The last number is {}'.format(numbers[-1]))
    print('The smallest number is {}'.format(min(numbers)))
    print('The largest number is {}'.format(max(numbers)))
    print('The average of the number is {:.1f}'.format(sum(numbers) / len(numbers)))


# this function will
def check_usernames():
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface',
                 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer',
                 'bob']
    user_name = input('enter the username: ')
    if user_name in usernames:
        print('Access granted')
    else:
        print('Access denied')


interact_with_numbers()
check_usernames()
