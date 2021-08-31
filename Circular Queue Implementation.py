class CircularQueue:

    # constructor
    def __init__(self, size):  # initializing the class
        self.size = size

        # initializing queue with none
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self, data):

        # condition if queue is full
        if (self.rear + 1) % self.size == self.front:
            return " Queue is Full\n"

        # condition for empty queue
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:

            # next position of rear
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1: # condition for empty queue
            return "Queue is Empty\n"

        # condition for only one element
        elif self.front == self.rear:
            temp = self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp

        else:
            temp = self.queue[self.front]
            self.front = (self.front + 1) % self.size
            return temp

    def display(self):

        # condition for empty queue
        if self.front == -1:
            return "Queue is Empty"

        elif self.rear >= self.front:
            print("Elements in the circular queue are:", end=" ")

            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
        else:
            print("Elements in Circular Queue are:",
                  end=" ")
            for i in range(self.front, self.size):
                print(self.queue[i], end=" ")
            for i in range(0, self.rear + 1):
                print(self.queue[i], end=" ")

        if (self.rear + 1) % self.size == self.front:
            print("Queue is Full")

#Run Coed
ob = CircularQueue(5)
ob.enqueue(120)
ob.enqueue(180)
ob.enqueue(163)
ob.enqueue(100)
ob.enqueue(69)
ob.display()

print("Deleted value = ", ob.dequeue())
print("Deleted value = ", ob.dequeue())
ob.enqueue(9)
ob.enqueue(20)
ob.enqueue(5)
print("Deleted value = ", ob.dequeue())
print("Deleted value = ", ob.dequeue())
print("Deleted value = ", ob.dequeue())
print("Deleted value = ", ob.dequeue())
print("Deleted value = ", ob.dequeue())
print(ob.display())
