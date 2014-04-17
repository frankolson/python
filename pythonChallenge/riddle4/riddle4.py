### Riddle 4
### Frank Olson
### V.1
### 14 April 2014
### Python 2.7.5
### Last Update: 14 April 2014

### Based on the clue the program will search through the input file looking for
### a lowercase letter surrounded on each side by three uppercase letters

def lettersInFile( file_name ):
    # Open the file
    fout = open(file_name, 'r')
    
    # Initialize variables and arrays
    letterArray = []
    tempList = []
    lineArray = fout.readlines()
    count = 0

    # Populate letterArray
    for e in lineArray:
        tempList = list(e)
        letterArray.extend(tempList)

    # Loop through file for boddy guards
    while count < len(letterArray)-9:
        if letterArray[count].islower():
            if letterArray[count+1].isupper():
                if letterArray[count+2].isupper():
                    if letterArray[count+3].isupper():
                        if letterArray[count+4].islower():
                            if letterArray[count+5].isupper():
                                if letterArray[count+6].isupper():
                                    if letterArray[count+7].isupper():
                                        if letterArray[count+8].islower():
                                            print letterArray[count+4]
        count = count+1
    
    
inputFile = raw_input("Enter file name: ")
lettersInFile(inputFile)
