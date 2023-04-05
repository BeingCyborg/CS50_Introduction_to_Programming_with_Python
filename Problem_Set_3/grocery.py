stuff = {}
while True:
    try:
        item = input()
        
    except EOFError:
        print()
        break
    if item.upper() in stuff:
            stuff[item.upper()]+=1
    else:
            stuff[item.upper()]=1
for item in sorted(stuff.keys()):
    print(stuff[item],item)