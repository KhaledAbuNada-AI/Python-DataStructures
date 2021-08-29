class CircularQueue():

    # constructor
    def __init__(self, size):  # initializing the class
        self.size = size

        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):

        if ((self.rear + 1) % self.size == self.front):
            return (" Queue is Full\n")
