### Riddle 6
### Frank Olson
### V.1
### 17 April 2014
### Python 2.7.5
### Last Update: 17 April 2014

### You were suppose to realize that peak hill sounded like pickle, a python
### library utilized in serialization. There is a file in the page source
### called banner.p, which is a pickle file. This program will deserialize it
### the print the result.

### This one was a bit tricky. You had to know what the banner program was
### (UNIX) and the multiply the tuples in the pickle file to get the answer

import pickle

userFile = raw_input("Enter file name: ")

def deserializeURL(fileName):
    # Initialize variables
    answer = []
    answerStr = ""

    # Load the file
    pickleFile = pickle.load(open(fileName, 'r'))

    # Print the result
    for i in pickleFile:
        for e in i:
            answer.append(e[0]*e[1])
        answer.append('\n')

    # Convert to string
    answerStr = ""
    

    # Print result
    print answerStr.join(answer)
    
deserializeURL(userFile)
