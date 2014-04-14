### Riddle 2
### Frank Olson
### V.1
### 10 April 2014
### Python 2.7.5
### Last Update: 10 April 2014

### Solution is to shift each letter in the string they give you over to the
### right by two characters. Then replace map in the url with its coresponding
### translation

newText = ""

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l", "m",
              "n","o","p","q","r","s","t","u","v","w","x","y","z"]

inputString = raw_input("Enter string to convert: ")
inputShift = input("Input shift number: ")

dictionary = {}

# Create dictionary
for let in range(0,len(alphabet)):
    dictionary[alphabet[let]] = alphabet[(let + inputShift) % 26]

# Convert letters
for l in inputString.lower():
    if l in dictionary:  
        l=dictionary[l]  
    newText+=l

print newText