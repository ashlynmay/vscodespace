import re
from cs50 import get_int, get_string

mastercard = [51, 52, 53, 54, 55]
amex = [34, 37]
acceptedlength = [13, 15, 16]


def main():
    cardn = card_prompt()
    length = card_length(cardn)
    if length in acceptedlength:
        if checksum(cardn, length):
            card_type(cardn)
        else:
            invalid()
    else:
        invalid()


def card_prompt():
    return input("Number: ")


def card_length(string):
    if (re.match(r"^\d{13}$", string)) is not None:
        return 13
    elif (re.match(r"^\d{15}$", string)) is not None:
        return 15
    elif (re.match(r"^\d{16}$", string)) is not None:
        return 16


def checksum(cardn, length):
    c1 = 0
    c2 = 0
    for i in range(length):
        if (i % 2) != 0:
            c4 = str(int(cardn[-(i+1)]) * 2)
            if (int(c4) > 9):
                c1 += (int(c4[-1]) + int(c4[-2]))
            else:
                c1 += int(c4)
        else:
            c2 += int(cardn[-(i+1)])

    c = c1 + c2
    c = str(c)

    if int(c[-1]) == 0:
        return True
    else:
        return False


def card_type(string):
    # If start with 34 or 37: Amex #
    if int(string[0:2]) in amex:
        print("AMEX")
    # If start with 4: Visa #
    elif int(string[0]) == 4:
        print("VISA")
    # If start with 5(1,2,3,4,5): Mastercard #
    elif int(string[0:2]) in mastercard:
        print("MASTERCARD")
    else:
        invalid()


def invalid():
    print("INVALID")


main()
