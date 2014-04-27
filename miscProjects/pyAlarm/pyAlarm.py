### Alarm 
### Frank Olson
### V.1
### 25 April 2014
### Python 2.7.5
### Last Update: 25 April 2014


# Import appropriate libraries
from pygame import mixer
import time
import sys

def mp3Alarm():
    # Variables
    iterator = 0

    # Get current time function
    def currentTime():
        hour = int(time.strftime("%H"))
        minute = int(time.strftime("%M"))
        sec = int(time.strftime("%S"))

        return (hour*60*60) + (minute*60) + sec

    # Cool cursor wheel function
    def cursorWheel(iterator):
        wheel = ['|','/','-','\\']
        return wheel[iterator % 4]

    # Print current time
    print "The current time is: " + time.strftime("%I:%M %p")
    print "\n"

    # Ask the user for the alarm time
    print "Please enter the time of your alarm: "
    alarmH = input("Hour (24): ")
    alarmM = input("Minute: ")
    print "\n"

    # Value checks
    if alarmH > 24:
        print "Invalid Hour entry."
        alarmH = input("Hour (24): ")
        print "\n"
    if alarmH < 0:
        print "Invalid Hour entry."
        alarmH = input("Hour (24): ")
        print "\n"
    if alarmM > 59:
        print "Invalid Minute entry."
        alarmH = input("Minute (24): ")
        print "\n"
    if alarmM < 0:
        print "Invalid Minute entry."
        alarmH = input("MInute (24): ")
        print "\n"

    # Get alarm sound file
    soundFile = raw_input("Enter alarm sound file location: ")

    # Convert input time for loop
    timeSec = (alarmH*60*60) + (alarmM*60)
                         
    # Loop until Alarm time
    while currentTime() != timeSec:
        sys.stdout.write(cursorWheel(iterator))
        sys.stdout.flush()
        time.sleep(0.1)
        sys.stdout.write('\b')
        iterator += 1

    # Finaly play sound
    print '\n'
    print "Alarm!!!"
    mixer.init()
    mixer.music.load(soundFile)
    mixer.music.play()

    # Ask for another alarm
    again = raw_input("Would you like to make another alarm?[Y/N]: ")
    if again.upper() == 'Y':
        print '\n'
        mixer.music.stop()
        mp3Alarm()
    
mp3Alarm()
