def convert24(x):
    hours, min = x.split(":")
    hours = float(hours)
    min = (float(min)/60)
    return hours+min


# taking timezone input
timezone = input(
    'Press 1 for 12-hour times & Press 2 for 24-hour times :-->    ')
match timezone:
    case '1':  # for 12 hours time zone
        time = input('What time is it? -->  ')
        time = time.replace(' ', '').lower().replace('.', '')
        # print(time)
        if time[-2:] == 'am':
            temp = len(time)-2
            if convert24(time[:temp]) >= 7 and convert24(time[:temp]) <= 8:
                print('breakfast time')
        elif time[-2:] == 'pm':
            temp = len(time)-2
            if convert24(time[:temp]) >= 6 and convert24(time[:temp]) <= 7:
                print('dinner time')
            elif convert24(time[:temp]) >= 12 or convert24(time[:temp]) == 1:
                print('lunch time')

    case '2':  # for 24 hours time zone
        time = input('What time is it? -->  ')
        time = convert24(time)
        # print(time)
        if time >= 7 and time <= 8:
            print('breakfast time')
        elif time >= 12 and time <= 13:
            print('lunch  time')
        elif time >= 18 and time <= 19:
            print('dinner time')
        else:
            print('')
