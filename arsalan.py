# Q: 9.1

class Counter():
    def __init__(self):
        self.value = 0

    def getVal(self):
        return self.value

    def click(self):
        self.value = self.value+1

    def reset(self):
        self.value = 0

    def undo(self):
        self.value = self.value-1
        if self.value < 0:
            self.value = 0

# Q: 9.2

class maxCount():
    def __init__(self,maximum):
        self.maximum = maximum
        self.value = 0
    
    def click(self):
        if self.value == self.maximum:
            print("Limit Exceeded")
        else:
            self.value = self.value+1

# Q: 9.6

class Car():
    def __init__(self,efficiency):
        self.eff = efficiency
        self.fuel = 0
        
    def drive(self,distance):
        self.tot_dis = distance
        
    def addGas(self,gas):
        self.gas = gas
        
    def getGasLevel(self):
        self.gallonsConsumed = self.tot_dis/self.eff
        self.remFuel = self.gas - self.gallonsConsumed
        return self.remFuel

# Q: 9.11

class Letter():
    def __init__(self, letterFrom, letterTo):
        self.sender = letterFrom
        self.recipient = letterTo
        self.text = ""
    
    def addLine(self, line):
        self.line = line
        self.text = self.text + "\n"
        self.text = self.text + self.line
    
    def getText(self):
        print("Dear", self.recipient)
        print(self.text)
        print("")
        print("Sincerely,")
        print("")
        print(self.sender)

 ## Driver Program:

##let = Letter("Mary","John")
##let.addLine("I am sorry we must part.")
##let.addLine("I wish you all the best.")
##let.getText()

# Q: 9.12

class Bug:
    def __init__(self,initialPosition):
        self.pos = initialPosition
        self.dir = 0
    
    def turn(self):
        if self.dir == 0:
            self.dir = 1
        elif self.dir == 1:
            self.dir = 0
    
    def move(self):
        if self.dir == 1:
            self.pos = self.pos - 1
        elif self.dir == 0:
            self.pos = self.pos + 1

    def getPosition(self):
        print(self.pos)


# Q: 11.1

def getArea_rect(h,w):
    if w == 0:
        return 0
    if w == 1:
        return h
    else:
        h = h + getArea_rect(h,w-1)
        return h
# Q 11.2

def getArea_sqr(w):
    if w == 0:
        return 0
    if w == 1:
        return 1
    y = getArea_sqr(w-1)
    return y + w + (w-1)

# Q 11.6

def find(text, string):
    if len(string)>len(text):
        return False
    if text.startswith(string):
        return True
    else:
        return find(text[1:], string)

# Q: 11.7

def main(text,string,count):
    if len(string)>len(text):
        return -1
    if text.startswith(string):
        return count
    else:
        return main(text[1:], string, count + 1)

def indexOf(text,string):
    return main(text, string, 0)

# Q: 11.12

def substrings(s):
    lst = [s]
    if len(s) > 0:
        lst.extend(substrings(s[1:]))
        lst.extend(substrings(s[:-1]))
    return list(set(lst))







        
