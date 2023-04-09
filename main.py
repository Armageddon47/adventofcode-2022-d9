
coordinates = []

class Knots:          #
    def __init__(self, UpDown, LeftRight):
        self.UpDown = UpDown
        self.LeftRight = LeftRight
        
with open('input.txt') as f:
    for line in f:
        coordinates.append(line.strip())
        
arr = [[0 for j in range(999)] for i in range(999)]
arr[0][0] = "S" #Starting point

     
head = Knots(0,0)
tail = Knots(0,0)

def Move():
    for line in coordinates:
        
        size = int(line[line.find(" "):])   
        temp = 0  #how many times will it move? each movement counts as one
                  # forexample  R 2 will move twice
        
        if (line[0]=="R"):  # is the order to move right left top or down?
            
            while(temp < size):
                
                head.LeftRight += 1
                temp += 1
                if(not IsInRange()): 
                    tail.UpDown = head.UpDown
                    tail.LeftRight = head.LeftRight
                    tail.LeftRight -= 1
                    if (not arr[tail.UpDown][tail.LeftRight] == "S"):
                        arr[tail.UpDown][tail.LeftRight] = "T"
                        
        elif (line[0]=="L"):
            
             while(temp < size):
                 
                head.LeftRight -= 1
                temp += 1
                if(not IsInRange()):
                    tail.UpDown = head.UpDown
                    tail.LeftRight = head.LeftRight
                    tail.LeftRight += 1
                    if (not arr[tail.UpDown][tail.LeftRight] == "S"):
                        arr[tail.UpDown][tail.LeftRight] = "T"
                        
                
        elif (line[0]=="U"):
             while(temp < size):
                
                head.UpDown += 1
                temp += 1
                if(not IsInRange()):
                    tail.UpDown = head.UpDown
                    tail.LeftRight = head.LeftRight
                    tail.UpDown -= 1
                    if (not arr[tail.UpDown][tail.LeftRight] == "S"):
                        arr[tail.UpDown][tail.LeftRight] = "T"
            
        elif (line[0]=="D"):
             while(temp < size):
                
                head.UpDown -= 1
                temp += 1
                if(not IsInRange()):
                    tail.UpDown = head.UpDown
                    tail.LeftRight = head.LeftRight
                    tail.UpDown += 1
                    if (not arr[tail.UpDown][tail.LeftRight] == "S"):
                        arr[tail.UpDown][tail.LeftRight] = "T"

            

    

def IsInRange():                                             #       if head taile is like below its in range
                                                             #    -1+1     +1    +1+1
    updown = False                                           #      -1   Value   +1
    leftright = False                                        #    -1-1     -1    -1+1
    if(head.LeftRight > tail.LeftRight):                     #
        if(head.LeftRight == tail.LeftRight + 1):               
            leftright =True
    elif(head.LeftRight < tail.LeftRight):
        if(head.LeftRight == tail.LeftRight - 1):
            leftright =True
    elif(head.LeftRight == tail.LeftRight):
            leftright =True

    if(head.UpDown > tail.UpDown):
        if(head.UpDown == tail.UpDown +1):
            updown = True
    elif(head.UpDown < tail.UpDown):
        if(head.UpDown == tail.UpDown - 1):
            updown = True
    elif(head.UpDown == tail.UpDown):
        updown = True
    

    if(updown and leftright):
        return True
    else:
        return False
    
Move()          # Start the movement
    

count = 0

for i in range(len(arr)):         #Array is the History Map  of the movement
    for j in range(len(arr[i])):
        if arr[i][j] == "T":
            count += 1            #Adding starting point as movement 
            
print(count + 1)

#### End of part 1