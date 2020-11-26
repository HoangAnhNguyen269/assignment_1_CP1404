def password_check(password):
    MIN_LENGTH = int(10)
    if len(password) < MIN_LENGTH:
        return False
    else:
        return True
def asterisk(password):
    for count in range(len(password)):
        print('*',end='')
    

def main():
    password = input('Enter password: ')
    while password_check(password) == False:
        password = input('Enter password: ')
    print('Valid password')
    asterisk(password)

main()
