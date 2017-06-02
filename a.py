from microbit import *
import music
#default 987
#B 424
#A 4-5
#C 447-455
#D 456-465
#E 542-557


#while True:
careless_whisper = ("C#6:4","B5:2","F#5:3","D5:4","C#6:4","B5:2","F#5:3","D5:4","R:2","A5:4","G5:2","D5:3","B4:4","A5:4","G5:2",
                     "D5:6","R:4","G5:4","F#5:2","D5:4","B4:4","G4:15","F#4:4","G4:4","A4:4","B4:4","C#5:4","D5:4","E5:4","F#5:4",
                     "C#6:4","B5:2","F#5:3","D5:4","C#6:4","B5:2","F#5:3","D5:4","R:2","A5:4","G5:2","D5:3","B4:4","A5:4","G5:2",
                     "D5:6","R:4","G5:4","F#5:2","D5:4","B4:4","G4:15","F#4:4","G4:4","A4:4","B4:4","C#5:4","D5:4","E5:4","F#5:4",
                     "B4:16")
    
   
    
    
#if key_value in values:
    #display.scroll("Y")
#else:
    #display.scroll("N")
while True:
    key_value = pin3.read_analog()
    display.scroll(str(key_value))
    
    if key_value in range(4,6):
        display.scroll("a")
        music.play(careless_whisper)
    if key_value in range(420,426):
        display.scroll("b")   
    if key_value in range(447,455):
        display.scroll("c")
    if key_value in range(456,466):
        display.scroll("d")
    if key_value in range(542,558):   
        display.scroll("e")
        careless_whisper = ("C#6:4","B5:2","F#5:3","D5:4","C#6:4","B5:2","F#5:3","D5:4","R:2","A5:4","G5:2","D5:3","B4:4","A5:4","G5:2",
                     "D5:6","R:4","G5:4","F#5:2","D5:4","B4:4","G4:15","F#4:4","G4:4","A4:4","B4:4","C#5:4","D5:4","E5:4","F#5:4",
                     "C#6:4","B5:2","F#5:3","D5:4","C#6:4","B5:2","F#5:3","D5:4","R:2","A5:4","G5:2","D5:3","B4:4","A5:4","G5:2",
                     "D5:6","R:4","G5:4","F#5:2","D5:4","B4:4","G4:15","F#4:4","G4:4","A4:4","B4:4","C#5:4","D5:4","E5:4","F#5:4",
                     "B4:16")
