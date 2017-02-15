import matplotlib.pyplot as plot

#Helpful posts

#resource for histogram plots https://bespokeblog.wordpress.com/2011/07/11/basic-data-plotting-with-matplotlib-part-3-histograms/
#http://stackoverflow.com/questions/18448847/import-txt-file-and-having-each-line-as-a-list
#http://stackoverflow.com/questions/10712002/create-an-empty-list-in-python-with-certain-size

fileName = 'names.txt'
#add all the lines into a large list deliminated by newline
with open(fileName) as line:
    nameList=line.readlines()

def hash(name,l): #takes in
    nameValue=0
    i=0
    while name[i] != ' ':
        nameValue+=ord(name[i])-64 #the ascii value of capital A is 65 and it increments up the alphabet since everything
    #is already all capitalf we dont need to downcase
        i=i+1

    return nameValue%l

def buildHashArray(l,numNames):
    table=[0]*l
    numCollisions=0
    for i in range(0,numNames):
        index=hash(nameList[i],l)
        table[index]=table[index]+1
        if table[index]>numCollisions:
            numCollisions=table[index]
    return table, numCollisions

#print (buildHashArray(200,len(nameList))[1])

hist200=buildHashArray(200,len(nameList))[0]
indexLocations=list(range(0,200))


plot.figure(1)
plot.hist(indexLocations,bins=range(0,200), weights=hist200)

plot.xlabel('Hash Index')
plot.ylabel('Number collisions')
plot.title("Histogram of number of collions")

collsionsPerInputSize=[0]*160

collisionIndex=0
for i in range(100,80000,500):
    collisions = buildHashArray(200,i)[1]
    collsionsPerInputSize[collisionIndex]=collisions
    collisionIndex=collisionIndex+1

print(str(collisionIndex) + str(len(collsionsPerInputSize)))
plot.figure(2)
plot.plot(range(0,len(collsionsPerInputSize)),collsionsPerInputSize)
plot.xlabel('Number of Names')
plot.ylabel('Max Number of Collisions')
plot.title("")


plot.show()


