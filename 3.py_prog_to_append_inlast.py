file=open('test.txt','a')
print('write something here to append in file test.txt')
while 1:
    text=input()
    if text=='~':
        break
    file.write(text+"\n")
file.close()
