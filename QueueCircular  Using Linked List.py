# Python3 program for insertion and
# deletion in Circular Queue

# Structure of a Node
class Node:
    def __init__(self):
        self.data = None
        self.link = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None


# Function to create Circular queue
def enQueue(q, value):
    temp = Node()
    temp.data = value
    if q.front == None:
        q.front = temp
    else:
        q.rear.link = temp

    q.rear = temp
    q.rear.link = q.front


# Function to delete element from
# Circular Queue

def deQueue(q):
    if q.front == None:
        print("Queue is empty")
        return -999999999999

    # If this is the last node to be deleted
    value = None  # Value to be dequeued
    if q.front == q.rear:
        value = q.front.data
        q.front = None
        q.rear = None
    else:  # There are more than one nodes
        temp = q.front
        value = temp.data
        q.front = q.front.link
        q.rear.link = q.front
    return value
