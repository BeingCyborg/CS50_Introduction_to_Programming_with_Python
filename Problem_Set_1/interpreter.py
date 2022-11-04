input = input('Expression : ')
input = input.replace(' ', '')
# print(input.find('+'))

if input.find('+') > -1:
    x = float(input[:input.find('+')])
    y = float(input[-input.find('+'):])
    print(x+y)
elif input.find('-') > -1:
    x = float(input[:input.find('-')])
    y = float(input[-input.find('-'):])
    print(x-y)
elif input.find('x') > -1:
    x = float(input[:input.find('x')])
    y = float(input[-input.find('x'):])
    print(x*y)
elif input.find('/') > -1:
    x = float(input[:input.find('/')])
    y = float(input[-input.find('/'):])
    print(x/y)
