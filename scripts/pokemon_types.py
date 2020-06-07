fd= open('/home/umutmaz/Desktop/t1t2.csv')
fk= open('/home/umutmaz/Desktop/types.csv','r')
fn= open('/home/umutmaz/Desktop/asd.csv','w')
arr=[]
arr2=[]
arr3=[]
typedict=dict()

for line in fd:
    line=line.rstrip('\n')
    line=line.split(',')

    if line[0]==line[1]:
        line[1]='null'

    arr.append(line)

for i in range(801):
    for j in range(2):
        arr2.append(arr[i][j])

for line in fk:
    line=line.rstrip('\n')
    line=line.split(',')
    typedict[line[1]]=line[0]



for i in arr2:
    if i in typedict.keys():
        i=typedict[i]
        arr3.append(i)

for i in arr3:
    fn.write(i+'\n')



