def password_check(password):
    MIN_LENGTH = int(10)
    if len(password) < MIN_LENGTH:
        return False
    else:
        return True


def asterisk(password):
    for count in range(len(password)):
        print('*', end='')


def main():
    password = get_password()
    while password_check(password) == False:
        password = input('Enter password: ')
    print('Valid password')
    asterisk(password)


def get_password():
    password = input('Enter password: ')
    return password
