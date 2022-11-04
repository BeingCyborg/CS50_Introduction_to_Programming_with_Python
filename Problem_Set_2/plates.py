def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    lenth = len(s)

    if s[:2].isalpha():
        if 2 <= lenth <= 6:
            if s[lenth-1].isalpha():
                if s[1:lenth-2].isalpha() == False:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False
    else:
        return False


main()
