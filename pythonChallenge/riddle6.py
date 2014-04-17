### Riddle 6
### Frank Olson
### V.1
### 17 April 2014
### Python 2.7.5
### Last Update: 17 April 2014

### You were suppose to realize that peak hill sounded like pickle, a python
### library utilized in serialization. There is a file in the page source
### called banner.p, which is a pickle file. This program will download in and
### then deserialize it

import urllib
import pickle

# Get address
urlFile = raw_input("Enter the address: ")

def deserializeURL(inputURL):
    fileHTML = urllib.urlopen(inputURL)

    # load the file
    pickelFile = pickle.load(fileHTML)

    # print the result
    print picklFile
    

