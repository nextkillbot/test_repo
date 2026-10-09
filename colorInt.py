# (r x 65536) + (g x 256) + b
# 16??

import time

def RGBPreview_FG(TextOutput, _Red, _Green, _Blue):
    Reset = "\033[0m"
    Code = f"\033[38;2;{_Red};{_Green};{_Blue}m"
    
    print(f"{Code}{TextOutput}{Reset}")
    
def RGBPreview_BG(TextOutput, _Red, _Green, _Blue):
    Reset = "\033[0m"
    Code = f"\033[48;2;{_Red};{_Green};{_Blue}m"
    Contrast = f"\033[38;2;{255 - _Red};{255 - _Green};{255 - _Blue}m"
    
    print(f"{Code}{Contrast}{TextOutput}{Reset}")
  
def ReturnBalanced(InputValue, IdentiferVariable):
    try:
        Processed = int(InputValue)
    except ValueError:
        Processed = 0
        RGBPreview_FG(f"[Error]: {IdentiferVariable} cannot be changed into an integer, it is then defaulted to 0\n", 255, 0, 0)
        
        return Processed
    
    if Processed > 255:
        # More than 255
        
        Processed = 255
        RGBPreview_FG(f"[Warning]: {IdentiferVariable} is being defaulted to 255, your value is {Processed} in which it's beyond the maximum\n", 255, 255, 170)
        
        return Processed
    elif Processed < 0:
        # Less than 0; Negative numbers
        
        Processed = 0
        RGBPreview_FG(f"[Warning]: {IdentiferVariable} is being defaulted to 0, your value is {Processed} in which it's below the minimum\n", 255, 255, 170)
        
        return Processed
        
    else:
        return Processed
        

print("== COLOR INTEGER (Used in Minecraft: Java Edition)")
print("Created by @NextKillbot\n")

Red = ReturnBalanced(input("Red? [0 - 255]: "), "Red")
Green = ReturnBalanced(input("Green? [0 - 255]: "), "Green")
Blue = ReturnBalanced(input("Blue? [0 - 255]: "), "Blue")

time.sleep(1)

print("Your integer code:")

RGBPreview_FG(f"I;{(Red * 65536) + (Green * 256) + Blue}", Red, Green, Blue)
print("")
print("== OR ==")
print("")
RGBPreview_BG(f"I;{(Red * 65536) + (Green * 256) + Blue}", Red, Green, Blue)

End = input("End? ")