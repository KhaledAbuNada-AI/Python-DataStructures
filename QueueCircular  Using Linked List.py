# Python3 program for insertion and
# deletion in Circular Queue

# Structure of a Node
class Noed:
    def __init__(self):
        self.data = None
        self.link = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
