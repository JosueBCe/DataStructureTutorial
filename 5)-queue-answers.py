class Queue:
    """
    A basic implementation of a Queue
    """

    def __init__(self):
        """
        Start with an empty queue.
        """
        self.queue = []

    def enqueue(self, value):
        """
        Add an item to the queue
        """
        self.queue.append(value)

    def dequeue(self):
        """
        Remove the next item from the queue. 
        """
        if len(self.queue) <= 0: 
            raise IndexError()  
        
        value = self.queue.pop()
        return value

    def is_empty(self):
        """
        Check to see if the queue is empty.
        """
        return len(self.queue) == 0

    def __len__(self):
        """
        Support the len() function
        """
        return len(self.queue)

    def __str__(self):
        """
        Provide a string representation for this object.
        """
        result = "["
        for item in self.queue:
            result += str(item)
            result += ", "
        result += "]"
        return result
    
     #TODO: create a method to print_elements of the queue 
    def print_elements(self):
        for num in self.queue:
            print(num)

my_queue = Queue()

# This should be called after completing the length method

if my_queue.is_empty():
    my_queue.enqueue(1)

# After completing the dequeue method this should be the value of 1
print("dequeued:" ,my_queue.dequeue())

my_queue.enqueue(10)
my_queue.enqueue(20)
my_queue.enqueue(30)

# After completing the dequeue method this should be the value of 10
print("dequeued:" ,my_queue.dequeue())


# Using iteration or something, print the values of the queue
print()
print("Elements of the queue")
my_queue.print_elements()

# Hoped answer 
# 20 
# 30 