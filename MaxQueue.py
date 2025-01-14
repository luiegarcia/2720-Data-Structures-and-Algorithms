# Luis Garcia
# CSC 2720 Lab 8
# Lab Time: Friday, 1:00 - 1:50 
# Due Time: Mar 3, 2024

from collections import deque

class MaxQueue:
    def __init__(self):
        self.main_queue = deque()
        self.max_queue = deque()

    def enqueue(self, value):
        self.main_queue.append(value)
        # Remove elements from the back of max_queue until finding an element >= value
        while self.max_queue and self.max_queue[-1] < value:
            self.max_queue.pop()
        self.max_queue.append(value)

    def dequeue(self):
        if not self.main_queue:
            return None
        value = self.main_queue.popleft()
        if value == self.max_queue[0]:
            self.max_queue.popleft()
        return value

    def get_max(self):
        if not self.max_queue:
            return None
        return self.max_queue[0]

# Test cases
if __name__ == "__main__":
    # Initialize the max queue
    max_queue = MaxQueue()

    # Test case 1: enqueue elements and verify max
    max_queue.enqueue(1)
    print("Max after enqueuing 1:", max_queue.get_max())  # Output: 1
    max_queue.enqueue(4)
    print("Max after enqueuing 4:", max_queue.get_max())  # Output: 4
    max_queue.enqueue(2)
    print("Max after enqueuing 2:", max_queue.get_max())  # Output: 4
    max_queue.enqueue(3)
    print("Max after enqueuing 3:", max_queue.get_max())  # Output: 4

    # Test case 2: dequeue elements and verify max
    max_queue.dequeue()
    print("Max after dequeuing 1:", max_queue.get_max())  # Output: 4
    max_queue.dequeue()
    print("Max after dequeuing 4:", max_queue.get_max())  # Output: 3
    max_queue.dequeue()
    print("Max after dequeuing 2:", max_queue.get_max())  # Output: 3
    max_queue.dequeue()
    print("Max after dequeuing 3:", max_queue.get_max())  # Output: None
