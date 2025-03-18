"""
Problem 7: Fishing Probability
Imagine that Animal Crossing is still using a linked list to represent the order fish 
will appear to a player who is fishing in the river! The head of the list represents 
the next fish that a player will catch if they keep fishing.

Write a function fish_chances() that accepts the head of a list and a string fish_name. 
Return the probability rounded down to the nearest hundredth that the player will catch 
a fish of type fish_name.

A function print_linked_list() which accepts the head, or first element, of a linked list 
and prints the list data has also been provided for testing purposes.
"""
class Node:
    def __init__(self, fish_name, next=None):
        self.fish_name = fish_name
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.fish_name, end=" -> " if current.next else "\n")
        current = current.next

def fish_chances(head, fish_name):
    total = 0
    count = 0
    current = head
    while current:
        if current.fish_name == fish_name:
            count += 1
        total += 1
        current = current.next
    return round(count/total, 2) if total > 0 else 0.00
        


def main():
    """
    Example Output:
    0.33
    0.00
    """
    fish_list = Node("Carp", Node("Dace", Node("Cherry Salmon")))
    print(fish_chances(fish_list, "Dace"))
    print(fish_chances(fish_list, "Rainbow Trout"))

if __name__ == "__main__":
    main()