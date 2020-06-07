fd=open('/home/umutmaz/Desktop/stats_data.csv','r')
fk=open('/home/umutmaz/Desktop/statmtat.csv','a')

arr=[]
arr1=[]


for line in fd:
    line=line.rstrip('\n')
    line=line.split(',')
    arr.append(line)
for i in range (0,801):
    for j in range (0,32):
        print(i,' ',j)
        fk.write(str(arr[i][j]+'\n'))
