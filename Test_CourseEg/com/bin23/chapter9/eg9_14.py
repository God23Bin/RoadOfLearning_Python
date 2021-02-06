class Display:
    def __init__(self,size):
        self.size = size

class Memory:
    def __init__(self,size):
        self.size = size

class Computer:
    def __init__(self,displaySize,memorySize):
        self.display = Display(displaySize)
        self.memory = Memory(memorySize)
        # 类似Java中
        # this.display = new Display(displaySize);
        # this.memory = new Memory(memorySize);