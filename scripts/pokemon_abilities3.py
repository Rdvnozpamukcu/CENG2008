fd=open('/home/umutmaz/Desktop/abilities.csv','r')
fk=open('/home/umutmaz/Desktop/orange.csv','r')
fw=open('/home/umutmaz/Desktop/hello.csv','w')
fq=open('/home/umutmaz/Desktop/hello1.csv','w')

abilitydict=dict()
arr=[]
arr2=[]
for line in fd:
    line=line.rstrip('\n')
    line=line.replace(' ','')
    line=line.split(',')
    line[1]=line[1].replace(' ','')
    abilitydict[line[1]]=line[0]

for line in fk:
    line = line.rstrip('\n')
    line = line.split(',')
    diff=6-line.__len__()
    if diff>1:
        for i in range(diff):
            line.append(',')
    elif diff>0:
        line.append(',')

    for i in line:
        arr.append(i)

for i in arr:
    i=i.replace(' ','')

    if i in abilitydict.keys():
        i=abilitydict[i]
        arr2.append(i)
    else:
        arr2.append(i)
for i in range(1,802):
    for j in range(1,7):
        fw.write(str(i)+'\n')

for i in arr2:
    fq.write(i+'\n')
