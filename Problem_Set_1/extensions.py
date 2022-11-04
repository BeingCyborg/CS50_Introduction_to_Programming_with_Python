input = input('File Name : ')
input = input.lower()
# print(input[-3:])
if input[-5:] == '.jpeg':
    print('image/jpeg')
elif input[-4:] == '.gif':
    print('image/gif')
elif input[-4:] == '.jpg':
    print('image/jpeg')
elif input[-4:] == '.png':
    print('gif image')
elif input[-4:] == '.pdf':
    print('application/pdf')
elif input[-4:] == '.txt':
    print('text/plain')
elif input[-4:] == '.zip':
    print('application/zip')
else:
    print('pplication/octet-stream')
