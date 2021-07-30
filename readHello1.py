file = open('Austin.txt','rt')

str = file.read()
print(str, end='')
file.close()