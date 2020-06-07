abilities=open("abilities.txt",'r')
skills=set()
skillslast=set()
for line in abilities:
    values=line.strip(',')
    values2=values.strip("[")
    values3=values2[0:-2]
    values4=values3.replace("'","")
    values5=values4.split(",")
    for i in values5:
        skills.add(str(i))
abilitynew=open("newabt.txt", 'w')
for i in skills:
    abilitynew.write(i+"\n")
abilitynew.close()
with open("newabt.txt","r") as file1:
    for line in file1:
        value=line.replace(" ","")
        skillslast.add(value)
k=sorted(skillslast)

with open("newabt.txt",'w')as file2:
    for i in k:
        file2.write(i)
