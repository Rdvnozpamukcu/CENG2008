fd=open('/home/umutmaz/Desktop/mild.csv','r')
fk=open('/home/umutmaz/Desktop/orange.csv','w')



for line in fd:
    line = line.strip(',')
    line = line.strip("[")
    line = line[0:-2]
    line = line.replace("'", "")
    line = line.replace("\"", "")
    line = line.replace("[", "")
    line = line.replace("]", "")
    # line=line.split(",")
    fk.write(line+'\n')
fd.close()
fk.close()

fkr=open('/home/umutmaz/Desktop/orange.csv','r')
fkw=open('/home/umutmaz/Desktop/stopped.csv','w')

for line in fkr:
    line=line.rstrip("\n")
    line=line.rstrip(",")
    line=line.split(",")
    print(line)
    for i in range(1,line.__len__()):
        toWrite=str(line[0])+'\n'
        print(toWrite)
        fkw.write(toWrite)



