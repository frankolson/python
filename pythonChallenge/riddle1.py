### Riddle 1
### Frank Olson
### V.1
### 10 April 2014
### Python 2.7.5
### Last Update: 10 April 2014

### Solution for riddle 1. Really simple, just calculate the exponent number on
### the computer screen in the picture, then use said number to replace the '0' 
### character in the URL.

exponent = input("Select and exponent of 2 to calculate: ")

answer = pow(2, exponent)

print(answer)
