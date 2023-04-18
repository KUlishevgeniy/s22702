f=open('1.txt', 'r')

#print(f)
#print(*f)
#print(f.read(3))
#print(f.readline())
print(f.readlines())
f.close()

f=open('files/2.txt', 'w')
#f=open('..files/2.txt', 'w') на директорию выше относительно которой находимся
f.write('Hello\n world')
f.close()