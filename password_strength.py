#!/usr/bin/python3
# -*- coding: utf-8

import re


def m1(pwd):  # number of upper letters
    return sum(1 for c in pwd if c.isupper())


def m2(pwd):  # number of lower letters
    return sum(1 for c in pwd if c.islower())


def m3(pwd):  # number of digits
    return sum(1 for c in pwd if c.isdigit())


def m4(pwd):  # number of special symbols
    return sum(1 for c in pwd if c in "$#@!%")


def m5(pwd):  # check if there are letter (upper and lower), digits and symbols
    return (m1(pwd) > 0) + (m2(pwd) > 0) + (m3(pwd) > 0) + (m4(pwd) > 0)


def m10(pwd):  # calculate number of consecutive uppercase letters
    dup = 0
    for m in re.finditer(r'([A-Z])\1*', pwd):
        if len(m.group(0)) > 1:
            dup += len(m.group(0))
    return dup


def m11(pwd):  # calculate number of consecutive lowercase letters
    dup = 0
    for m in re.finditer(r'([a-z])\1*', pwd):
        if len(m.group(0)) > 1:
            dup += len(m.group(0))
    return dup


def m12(pwd):  # calculate number of consecutive digits
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
    # add strengths
    strength = len(password) * 4
    strength += (len(password) - m1(password)) * 2
    strength += (len(password) - m2(password)) * 2
    strength += m3(password) * 4
    strength += m4(password) * 6
    strength += m5(password) * 2

    # subtract weaknesses
    strength -= letters_only(password)
    strength -= digits_only(password)
    strength -= m10(password) * 2
    strength -= m11(password) * 2
    strength -= m12(password) * 2

    return strength


def main():
    while True:
        pwd = input("enter password to check (5 <= length <= 20): ").strip()
        if pwd:
            if 4 < len(pwd) < 21:
                if ' ' in pwd:
                    print("no spaces allowed inside password")
                else:
                    print("password strength is {} (min=17,  max=270)".format(calculate_strength(pwd)))
            else:
                print("invalid password length {}".format(len(pwd)))
        else:
            break


if __name__ == '__main__':
    main()
