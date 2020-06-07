tx_begin="INSERT INTO pokemon_stats " \
   "VALUES("

tx_end=", null);"

fd=open('/home/umutmaz/Desktop/pokemon_stats2.csv','r')

fx=open('/home/umutmaz/Desktop/injection.sql','w')


arr=[]

for line in fd:
    line=line.rstrip('\n')
    arr.append(line)
# print(arr)

for i in range (138):
    text=tx_begin+arr[i]+tx_end
    fx.write(text+'\n')
