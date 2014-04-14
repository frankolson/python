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
    answer = ""
    letterArray = []
    tempList = []
    lineArray = fout.readlines()

    # Populate letterArray
    for e in lineArray:
        tempList = list(e)
        letterArray.extend(tempList)
    
    # Test
    print letterArray
    
    
inputFile = raw_input("Enter file name: ")
lettersInFile(inputFile)
