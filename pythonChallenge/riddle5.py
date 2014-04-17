### Riddle 5
### Frank Olson
### V.1
### 17 April 2014
### Python 2.7.5
### Last Update: 17 April 2014

### The title of this riddle is called follow the chain, appropriate. There is
### a comment in the page source that instructs you to use urllib.

### When running the program you will notice a gap. The gap is the only page
### that does not have a number and the answer is contained on that page.

import urllib

# Initial webpage
initURL = raw_input("Enter first webpage: ")
response = urllib.urlopen(initURL)
pageURL = response.read()
response.close()

def getNum(page):
    # Initialize output str and add store website
    number = ""

    # Search for numbers
    for e in page:
        if e.isdigit():
            number = number + e
    return number

def cyclePages(page):
    count = 0
    newPageURL = page

    #Cycle 400 types
    while count < 400:
        num = getNum(newPageURL)
        htmlStr = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=" + num
        newResponse = urllib.urlopen(htmlStr)
        newPageURL = newResponse.read()
        print getNum(newPageURL)
        count = count+1

cyclePages(pageURL)

