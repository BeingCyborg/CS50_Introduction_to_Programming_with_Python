a = input(
    'What is the Answer to the Great Question of Life, the Universe, and Everything?')

if a == '42' or a.lower().replace(' ', '') == 'fortytwo' or a.lower().replace('-', '') == 'fortytwo':
    print('Yes')
else:
    print('No')