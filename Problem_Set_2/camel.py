input = input('camelcase : ')
print('snake_case : ', end="")
for i in range(len(input)):
    if 'A' <= input[i] <= 'Z':
        print('_'+input[i].lower(), end="")
    else:
        print(input[i], end="")
