import os

os.chdir('/home/umutmaz/Desktop')

file = open('newabt.txt','r')

typeset= set()
arr=[]
for line in file:
    line=line.rstrip('\n')
    if line == '':
        line='null'
    typeset.add(line)
print(typeset)
i=1
for type in typeset:
    row= str(i)+','+type+'\n'
    i+=1
    arr.append(row)
    print(arr)

file.close()

file=open('/home/umutmaz/Desktop/types.csv','w')

for i in arr:
    file.write(i)

file.close()
