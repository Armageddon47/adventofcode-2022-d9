
coordinates = []
direction = {
    "R": [1, 0],
    "U": [0, 1],
    "L": [-1, 0],
    "D": [0, -1]
}
class Knots:          #
    def __init__(self):
        self.x = 0
        self.y = 0
        self.tail_visited = set()

    def Add(self, i):
        self.x += i[0]
        self.y += i[1]
        
    def Follow(self, temp1):
        xVal = 0
        yVal = 0
        if (self.x == temp1.x):
            xVal = 0
        else:
            xVal = int((temp1.x - self.x) / abs(temp1.x - self.x))
        if (self.y == temp1.y):
            yVal = 0
        else:
            yVal = int((temp1.y - self.y) / abs(temp1.y - self.y))
        
        self.tail_visited.add((self.x, self.y))
        self.x += xVal
        self.y += yVal
        
with open('input.txt') as f:
    for line in f:
        coordinates.append(line.strip())

def touching(h,t):
    return abs(h.x - t.x) <= 1 and abs(h.y - t.y) <= 1

def Move(line,h,t):
        
        size = int(line[line.find(" "):])   
        temp = 0  
        
        if (line[0]=="R"):
            
            while(temp < size):
                
                h.Add(direction["R"])
                temp += 1
                if(not touching(h,t)): 
                    
                    t.Follow(h)

        elif (line[0]=="L"):
            
             while(temp < size):
                 
                h.Add(direction["L"])
                temp += 1
                if(not touching(h,t)): 
                    
                    t.Follow(h)
      
        elif (line[0]=="U"):
             while(temp < size):
                
                h.Add(direction["U"])
                temp += 1
                if(not touching(h,t)): 
                    
                    t.Follow(h)

        elif (line[0]=="D"):
             while(temp < size):
                
                h.Add(direction["D"])
                temp += 1
                if(not touching(h,t)): 
                    
                    t.Follow(h)
        
    

head = Knots()
tail = Knots()

for line in coordinates:
        Move(line,head,tail)
    
            
print("Part One Answer is :", len(tail.tail_visited) )


#### End of part 1
####################################

def MoveTails(line,h,t): #Changed Tails to array
    
        count = len(t)   # getting Length of the array 
        tempCount = 0    # To keep track of movement in the array
        
        size = int(line[line.find(" "):])   
        temp = 0         # To keep track of the movement of Head
        
        if (line[0]=="R"):
            
            while(temp < size):
                tempCount = 0
                h.Add(direction["R"])
                temp += 1
                
                if(not touching(h,t[0])): 
                    
                    t[0].Follow(h)
                for i in t:
                    if (tempCount >= count - 1):
                        break
                    elif(not touching(t[tempCount],t[tempCount+1])):
                        t[tempCount+1].Follow(t[tempCount])
                    tempCount += 1
                    

        elif (line[0]=="L"):
            
             while(temp < size):
                tempCount = 0
                h.Add(direction["L"])
                temp += 1
                if(not touching(h,t[0])): 
                    
                    t[0].Follow(h)
                for i in t:
                    if (tempCount >= count - 1):
                        break
                    elif(not touching(t[tempCount],t[tempCount+1])):
                        t[tempCount+1].Follow(t[tempCount])
                    tempCount += 1
      
        elif (line[0]=="U"):
             while(temp < size):
                tempCount = 0
                h.Add(direction["U"])
                temp += 1
                if(not touching(h,t[0])): 
                    
                    t[0].Follow(h)
                for i in t:
                    if (tempCount >= count- 1):
                        break
                    elif(not touching(t[tempCount],t[tempCount+1])):
                        t[tempCount+1].Follow(t[tempCount])
                    tempCount += 1
        elif (line[0]=="D"):
             while(temp < size):
                tempCount = 0
                h.Add(direction["D"])
                temp += 1
                if(not touching(h,t[0])): 
                    
                    t[0].Follow(h)
                for i in t:
                    if (tempCount >= count - 1):
                        break
                    elif(not touching(t[tempCount],t[tempCount+1])):
                        t[tempCount+1].Follow(t[tempCount])
                    tempCount += 1

knots_list = []
for i in range(0,9):
     knot = Knots()
     knots_list.append(knot)
     
head1 = Knots()

for line in coordinates:
    MoveTails(line,head1,knots_list)

print("Part Two Answer is :",len(knots_list[-1].tail_visited) + 1)
