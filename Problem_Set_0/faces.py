def convert(a):
    a = a.replace(':)','🙂')
    a = a.replace(':(','🙁')
    return a

def main():
    str = input()
    print(convert(str))
main()