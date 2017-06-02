#!/usr/bin/python3

import re


def count_upper_chars(pwd):
    return sum(1 for c in pwd if c.isupper())


def count_lower_chars(pwd):  # number of lower letters
    return sum(1 for c in pwd if c.islower())


def count_digits(pwd):  # number of digits
    return sum(1 for c in pwd if c.isdigit())


def count_symbols(pwd):  # number of special symbols
    return sum(1 for c in pwd if c in "$#@!%")


def count_requirements(pwd):  # check if there are upper and lower letters, digits and symbols
    return (count_upper_chars(pwd) > 0) + (count_lower_chars(pwd) > 0) + (count_digits(pwd) > 0) + (
        count_symbols(pwd) > 0)


def repeating_upper_chars(pwd):  # calculate number of consecutive uppercase letters
    dup = 0
    for m in re.finditer(r'([A-Z])\1*', pwd):
        if len(m.group(0)) > 1:
            dup += len(m.group(0))
    return dup


def repeating_lower_chars(pwd):  # calculate number of consecutive lowercase letters
    dup = 0
    for m in re.finditer(r'([a-z])\1*', pwd):
        if len(m.group(0)) > 1:
            dup += len(m.group(0))
    return dup


def repeating_digits(pwd):  # calculate number of consecutive digits
    dup = 0
    for m in re.finditer(r'([0-9])\1*', pwd):
        if len(m.group(0)) > 1:
            dup += len(m.group(0))
    return dup


def letters_only(pwd):
    if all(c.isalpha() for c in pwd):
        return len(pwd)
    else:
        return 0


def digits_only(pwd):
    if all(c.isdigit() for c in pwd):
        return len(pwd)
    else:
        return 0


def calculate_strength(password: "str") -> "int":
    max_strength = 130
    # add strengths
    strength = len(password) * 4
    strength += (len(password) - count_upper_chars(password)) * 2
    strength += (len(password) - count_lower_chars(password)) * 2
    strength += count_digits(password) * 4
    strength += count_symbols(password) * 6
    strength += count_requirements(password) * 2

    # subtract weaknesses
    strength -= letters_only(password)
    strength -= digits_only(password)
    strength -= repeating_digits(password) * 2
    strength -= repeating_lower_chars(password) * 2
    strength -= repeating_upper_chars(password) * 2

    return (strength * 10) // max_strength  # return strength in scale from 1 to 10


def main():
    while True:
        pwd = input("enter password to check (5 <= length <= 10): ").strip()
        if pwd:
            if 5 <= len(pwd) <= 10:
                if ' ' in pwd:
                    print("no spaces allowed inside password")
                else:
                    print("password strength is {}".format(calculate_strength(pwd)))
            else:
                print("invalid password length {}".format(len(pwd)))
        else:
            break


if __name__ == '__main__':
    main()
