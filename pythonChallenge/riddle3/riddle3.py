### Riddle 3.1
### Frank Olson
### V.1
### 10 April 2014
### Python 2.7.5
### Last Update: 11 April 2014

### Wanted to check how many of each character was in the mess of character. 
### This was because I have no idea what they mean by 'rare character' so I 
### thought sorting them out would make it easier to identify said characters

### Turns out this worked!!! I found the characters a,e,i,1,q,u,t,y then I 
### seached for those characters specifically in the text and found the order
### giving me the result 'equality'... pretty cool

def charactersInFile( file_name ):
    # Open file
    fout = open(file_name, 'r')

    # Initialize dictionary and line array
    dic = {}
    lineArray = fout.readlines()

    # Array of 'rare characters'
    rare = ['a','e','i','l','q','u','t','y']
    
    # Evaluate each character
    for e in lineArray:
        for c in e:
            if c in dic:
                dic[c] = dic[c] + 1
            else:
                if c != '\n':
                    dic[c] = 1

    # find order of rare characters
    for e in lineArray:
        for c in e:
            if c in rare:
                print c
	
    # Close file and return value
    fout.close()
    return dic

#for testing purposes
def printDictionary( dic ):
    for e in dic:
        print e, ':', dic[e]

user_file = raw_input("enter a file name: ")
charactersInFile(user_file)
