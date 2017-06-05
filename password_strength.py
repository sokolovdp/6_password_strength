import re
import getpass


def count_upper_chars(pwd):
    return sum(1 for c in pwd if c.isupper())


def count_lower_chars(pwd):
    return sum(1 for c in pwd if c.islower())


def count_digits(pwd):
    return sum(1 for c in pwd if c.isdigit())


def count_symbols(pwd):
    return sum(1 for c in pwd if c in "$#@!%")


def count_requirements(pwd):
    return (count_upper_chars(pwd) > 0) + (count_lower_chars(pwd) > 0) + (count_digits(pwd) > 0) + (
        count_symbols(pwd) > 0)


def repeating_upper_chars(pwd):
    return sum(len(m.group(0)) for m in re.finditer(r'([A-Z])\1*', pwd) if len(m.group(0)) > 1)


def repeating_lower_chars(pwd):
    return sum(len(m.group(0)) for m in re.finditer(r'([a-z])\1*', pwd) if len(m.group(0)) > 1)


def repeating_digits(pwd):
    return sum(len(m.group(0)) for m in re.finditer(r'([0-9])\1*', pwd) if len(m.group(0)) > 1)


def if_letters_only_return_length(pwd):
    if all(c.isalpha() for c in pwd):
        return len(pwd)
    else:
        return 0


def if_digits_only_return_length(pwd):
    if all(c.isdigit() for c in pwd):
        return len(pwd)
    else:
        return 0


def calculate_strength(password: "str") -> "int":
    max_strength = 130
    strength = len(password) * 4
    strength += (len(password) - count_upper_chars(password)) * 2
    strength += (len(password) - count_lower_chars(password)) * 2
    strength += count_digits(password) * 4
    strength += count_symbols(password) * 6
    strength += count_requirements(password) * 2

    strength -= if_letters_only_return_length(password)
    strength -= if_digits_only_return_length(password)
    strength -= repeating_digits(password) * 2
    strength -= repeating_lower_chars(password) * 2
    strength -= repeating_upper_chars(password) * 2

    return (strength * 10) // max_strength  # return strength in scale from 1 to 10


def main():
    while True:
        password = getpass.getpass("enter password to check (5 <= length <= 10):")
        if password:
            if 5 <= len(password) <= 10:
                if ' ' in password:
                    print("no spaces allowed inside password")
                else:
                    print("password strength is {}".format(calculate_strength(password)))
            else:
                print("invalid password length {}".format(len(password)))
        else:
            break


if __name__ == '__main__':
    main()
