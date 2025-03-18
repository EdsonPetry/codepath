"""
Problem 1: Next in Queue
Each user on a music app should have a queue of songs to play next. Implement the class
 Queue using a singly linked list. Recall that a queue is a First-In-First-Out (FIfO)
 data structure where elements are added to the end (the tail) and removed from the front
   (the head).

Your queue must have the following methods:

__init()__: Initializes an empty queue (provided)
enqueue(): Accepts a tuple of two strings (song, artist) and adds the element with the
specified tuple to the end of the queue.
dequeue(): Removes and returns the element at the front of the queue. If the queue is empty,
 returns None.

peek(): Returns the value of the element at the front of the queue without removing it. If
the queue is empty, returns None.

is_empty(): Returns True if the queue is empty, and False otherwise.

Example Output:

('Love Song', 'Sara Bareilles') -> ('Ballad of Big Nothing', 'Elliot Smith') -> ('Hug from a Dinosaur', 'Torres')
Peek:  ('Love Song', 'Sara Bareilles')
Dequeue:  ('Love Song', 'Sara Bareilles')
Dequeue:  ('Ballad of Big Nothing', 'Elliot Smith')
Is Empty:  False
Dequeue:  ('Hug from a Dinosaur', 'Torres')
Is Empty: True
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# For testing
def print_queue(head):
    current = head.front
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.rear is None

    def enqueue(self, tup):
        if self.is_empty():
            self.front = Node(tup)
            self.rear = self.front
        else:
            tmp = self.rear
            tmp.next = Node(tup)
            self.rear = tmp.next


    def dequeue(self):
        is_One = False
        if self.is_empty():
            return None
        if self.front == self.rear:
            is_One = True
        tmp = self.front
        self.front = self.front.next
        if is_One:
            self.rear = self.front
        return tmp.value

    def peek(self):
        return self.front.value if self.front else None


def main():
    # Create a new Queue
    q = Queue()

    # Add elements to the queue
    q.enqueue(("Love Song", "Sara Bareilles"))
    q.enqueue(("Ballad of Big Nothing", "Elliot Smith"))
    q.enqueue(("Hug from a Dinosaur", "Torres"))
    print_queue(q)

    # View the front element
    print("Peek: ", q.peek())

    # Remove elements from the queue
    print("Dequeue: ", q.dequeue())
    print("Dequeue: ", q.dequeue())

    # Check if the queue is empty
    print("Is Empty: ", q.is_empty())

    # Remove the last element
    print("Dequeue: ", q.dequeue())

    # Check if the queue is empty
    print("Is Empty:", q.is_empty())


if __name__ == "__main__":
    main()
