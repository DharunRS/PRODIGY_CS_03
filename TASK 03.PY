import re

def check_digit(pwd: str) -> bool:
    return bool(re.search(r'[0-9]', pwd))

def check_uppercase(pwd: str) -> bool:
    return bool(re.search(r'[A-Z]', pwd))

def check_lowercase(pwd: str) -> bool:
    return bool(re.search(r'[a-z]', pwd))

def check_special_char(pwd: str) -> bool:
    return bool(re.search(r'[!@#$%^&*?]', pwd))

def check_length(pwd: str) -> bool:
    return 6<=len(pwd)<=18

pwd = input(' choose a password for your account:')

if all([check_digit(pwd),
        check_lowercase(pwd),
        check_lowercase(pwd),
        check_special_char(pwd),
        check_length(pwd)]):
    print(' Your  password id strong, you are good to go!')
else:
    print(' your password has not met the following requirment(s): ')

    if not check_digit(pwd):
        print(' - password must have at least one digit (0-9)') 

    if not check_uppercase(pwd):
        print(' - password must have at least one upper-case latter (A-Z)')

    if not check_lowercase(pwd):
        print(' - password must have at least one lower-case latter (a-z)')

    if not check_special_char(pwd):
        print(' - password must have at least one special characters (!@#$%^&*?)')



