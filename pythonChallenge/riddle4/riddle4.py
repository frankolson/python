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
    lineArray = fout.readlines()
    
    # Test
    print lineArray
    
    
