fd=open('/home/umutmaz/Desktop/abilities.csv','r')
fk=open('/home/umutmaz/Desktop/orange.csv','r')
fw=open('/home/umutmaz/Desktop/pokemon_abilities.csv','a+')

abilitydict=dict()

for line in fd:
    line=line.rstrip('\n')
    line=line.split(',')
    key=line[1]
    abilitydict[key]=line[0]
k=','


for line in fk:
    line=line.rstrip('\n')
    line=line.rstrip(',')
    line=line.replace(' ','')
    line=line.split(',')
    # print(line)


    line1=line[1:]
#    print(line1)


    for i in line1:

        print(i)
        if i in abilitydict.keys():
            toWrite=k+abilitydict[i]+'\n'
            toWrite=str(toWrite)
            print(toWrite)
            fw.write(toWrite)

    #print(line)
