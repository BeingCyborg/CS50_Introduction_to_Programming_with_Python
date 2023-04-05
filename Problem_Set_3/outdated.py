def slash(txt):
    if txt.find('/') != -1:
        return True


def main():
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            dateinput = input("Date: ")
            if slash(dateinput):
                dmy = dateinput.split('/')
                mm = dmy[0]
                if 1 <= int(mm) <= 12:
                    dd = dmy[1]
                    yy = dmy[2]
                    print(f"{yy}-{mm}-{dd}")
                    break
            else:
                # dateinput = input("Date: ")
                import re
                dateinput = re.sub(',', '', dateinput)
                dmy = dateinput.split(' ')
                mm = dmy[0]
                mm = month.index(mm) + 1
                dd = dmy[1]
                yy = dmy[2]
                print(f"{yy}-{mm}-{dd}")
                break
        except:
            pass


main()
