"""
CP1404/CP5632 Practical
Store Emails
"""
email= input('Emails: ')
name_to_email ={}
while email != '':
    email_items = email.split('@')
    email_items[0] = email_items[0].split('.')
    email_items[0]= " ".join(email_items[0]).title()
    while True:
        answer =input('Is your name {}? (Y/n)'.format(email_items[0])).lower()
        if answer == 'y' or answer=='yes':
            name_to_email[email_items[0]] = email
            break
        elif answer =='n' or answer =='no':
            name = input('Name: ')
            name_to_email[name] = email
            break
        else:
            print('invalid input')
            answer = input('Is your name {}? (Y/n)'.format(email_items[0])).lower()
    email = input('Emails: ')
for name in name_to_email:
    print('{} ({})'.format(name,name_to_email[name]))

