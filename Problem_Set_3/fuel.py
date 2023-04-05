def main():
    frac = get_int("Fraction: ")
    if frac*100 <= 1:
        print('E')
    elif frac*100 >= 99:
        print('F')
    else:
        print(f"{round(frac*100)}%")

def get_int(prompt):
    while True:
        try:
            frac1 = input(prompt)
            frac1.split("/")
            x = int(frac1[0])
            y = int(frac1[2])
            if x <= y:
                return float(x/y)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass

main()
