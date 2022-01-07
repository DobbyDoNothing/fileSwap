def WordCounterFile():
    fileName=input ("enter the filename: ")
    file=open(fileName,'r')
    totalWords=0
    for i in file:
        words=i.split()
        totalWords+=len(words)
    print(totalWords)

WordCounterFile()