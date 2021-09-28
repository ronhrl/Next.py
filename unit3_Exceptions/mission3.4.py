class UsernameContainsIllegalCharacter(Exception):
    def __init__(self, arg):
        self.args = arg

    def __str__(self):
        return "Username contains illegal Character"


class UsernameTooShort(Exception):
    def __init__(self, arg):
        self.args = arg

    def __str__(self):
        return "Username is Too Short. Min is 3"


class UsernameTooLong(Exception):
    def __init__(self, arg):
        self.args = arg

    def __str__(self):
        return "Username Too Long. Max is 16"


class PasswordMissingCharacter(Exception):
    def __init__(self, arg):
        self.args = arg

    def __str__(self):
        return "Password missing character"


class PasswordTooShort(Exception):
    def __init__(self, arg):
        self.args = arg

    def __str__(self):
        return "Password too short"


class PasswordTooLong(Exception):
    def __init__(self, arg):
        self.args = arg

    def __str__(self):
        return "Password too long"


def check_input(username, password):
    is_digit = False
    is_char = False
    is_line = False
    is_super = False
    is_lower = False
    is_num = False
    is_punc = False
    for char in username:
        if char.isdigit():
            is_digit = True

    for char in username:
        if char.alpha():
            is_char = True

    for char in username:
        if char == '_':
            is_line = True
    if 3 < username < 16 and is_digit and is_char and is_line:
        is_username_valid = True
    else:
        is_username_valid = False

    for char in password:
        if char.isuper():
            is_super = True

    for char in password:
        if char.islower():
            is_lower = True

    for char in password:
        if char.isdigit():
            is_num = True

    for char in password:
        if char.ispunctuation():
            is_punc = True

    if 8 < len(password) < 40 and is_num and is_punc and is_lower and is_super:
        is_password_valid = True
    else:
        is_password_valid = False

    if is_password_valid and is_username_valid:
        print("OK")
