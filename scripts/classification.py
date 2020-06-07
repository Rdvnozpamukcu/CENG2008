import os

os.chdir('/home/umutmaz/Desktop/')
class_array=[]

file = open('/home/umutmaz/Desktop/classes', 'r')
i=0
print(i)
for line in file:
    line = line.rstrip('\n')
    class_array.append(line)

class_set=set(class_array)


file.close( )
os.system('touch class.csv')

file = open('/home/umutmaz/Desktop/class.csv', 'w')

for i in class_set:
    i+='\n'
    file.write(i)
