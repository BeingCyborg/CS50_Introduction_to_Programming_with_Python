while True :
        str = input('Input : ')
        print('Output : ', end="")
        for i in range(len(str)):
            if str[i]=='a' or str[i]=='e' or str[i]=='i' or str[i]=='o' or str[i]=='u':
                print(end="")
            else:
                print(str[i], end="")
        print('')
