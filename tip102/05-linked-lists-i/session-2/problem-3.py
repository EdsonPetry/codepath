"""
Problem 3: Delete Duplicates in a Linked List
Given the head of a sorted linked list, delete all elements that occur more 
than once in the list (not just the duplicates). The resulting list should 
maintain sorted order. Return the head of the linked list.

Evaluate the time and space complexity of your solution. Define your variables 
and provide a rationale for why you believe your solution has the stated time 
and space complexity.

1 1 1 2 3 4 6 6
^     ^
curr.next = temp
1 -> 2
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

def delete_dupes(head):
    
    dummy = Node(None)
    dummy.next = head
    prev = dummy
    curr = head

    while curr:
        ifDuplicate = False
        while curr.next and curr.value == curr.next.value:
            ifDuplicate = True
            curr = curr.next

        if ifDuplicate:
            prev.next = curr.next
        else:
            prev = prev.next
            
        curr = curr.next

    return dummy.next
        



def main():

    # Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
    

    # 1 1 1 2 3 4 5
    head = Node(1, Node(1, Node(1, Node(2, Node(3, Node(4, Node(5)))))))
    print_linked_list(delete_dupes(head))

# Example Output:

# 1 -> 2 -> 4 -> 5

if __name__ == "__main__":
    main()