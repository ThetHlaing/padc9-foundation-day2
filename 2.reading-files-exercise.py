#Request a name of the file
filePath = input('Please enter the file path : ')

#Read the inputted file
handler = open(filePath,'r')

lineList = []
while True :
    line = handler.readline()
    
    if not line:
        #fail if the line is not there
        break
    #display the content line by line with while loop
    print(line)
    #save the lines into the list
    lineList.append(line)
    
print(lineList)
    


