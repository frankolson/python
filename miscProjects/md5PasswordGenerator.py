### md5PasswordGenerator
### Will Olson
### 01 October
### Python 2.7.7
### Last Update: 01 October 2014

### Based off of HP abstract that can be found here
### http://www.hpl.hp.com/personal/Alan_Karp/site_password/index_files/site_password.pdf

# Import Libraries
import hashlib

# Prompt for Key and Salt
masterKey = raw_input("Gimme the master key: ")
salt = raw_input("Gimme the specific key: ")

# Hash the the key and the salt and set to hex
hashPass = hashlib.md5( salt + masterKey ).hexdigest()

# Only take first 15 characters to strengthen security
hashSmallPass = hashPass[:15]

# Output the salt and the hash for user to see results

print "Your password variations: "
print "     full length -  %s: %s" % (salt, hashPass)
print "     shortened   -  %s: %s" % (salt, hashSmallPass)

# Wait until a key is pressed
raw_input()
