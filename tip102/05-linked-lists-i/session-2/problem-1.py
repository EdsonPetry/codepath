"""
Problem 1: Greatest Node
Write a function find_max() that takes in the head of a linked list and returns 
the maximum value in the linked list. You can assume the linked list will contain 
only numeric values.

Evaluate the time and space complexity of your solution. Define your variables and 
provide a rationale for why you believe your solution has the stated time and space complexity.
"""

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def find_max(head):
    max_val = head.value
    curr = head
    while curr:
        max_val = max(max_val, curr.value)
        curr = curr.next
    return max_val

def main():
    head1 = Node(5, Node(6, Node(7, Node(8))))

    # Linked List: 5 -> 6 -> 7 -> 8
    print(find_max(head1))

    head2 = Node(5, Node(8, Node(6, Node(7))))

    # Linked List: 5 -> 8 -> 6 -> 7
    print(find_max(head2))
"""
Expected Output:

8
8
"""

if __name__ == "__main__":
    main()