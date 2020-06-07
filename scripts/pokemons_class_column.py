import os

os.chdir('/home/umutmaz/Desktop')

file = open('newabt.txt','r')

arr=[]
clses=set()
clsdict=dict()
for line in file:
    line=line.rstrip('\n')
    arr.append(line)

sortedarr=sorted(arr)

i=0
for cls in sortedarr:
    if cls != '\n':
        clses.add(cls)
sortedset=sorted(clses)

for obj in sortedset:
    clsdict[obj]=i
    i+=1

#print(clsdict)
print(arr)
file2=open('pokemons_class_column.csv','w')
# for k in arr:
#   # print(clsdict[k])
#     file2.write(str(clsdict[k])+'\n')



file.close()





