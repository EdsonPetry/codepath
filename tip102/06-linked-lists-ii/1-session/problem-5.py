"""
Problem 5: Double Listening Count
A new artist is blowing up and the number of people listening to their music
has doubled in the last month. Given the head of a non-empty linked list
monthly_listeners representing a non-negative integer without leading zeroes,
return the head of the linked list after doubling its integer value.

Evaluate the time and space complexity of your solution. Define your variables
and provide a rationale for why you believe your solution has the stated time
and space complexity.

Example Output:

3 -> 7 -> 8
Example 1 Explanation: 189 * 2 = 378

1 -> 9 -> 9 -> 8
Example 2 Explanation: 999 * 2 = 1998
"""


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "")
        current = current.next
    print()


def double_listeners(monthly_listeners):
    pass


def main():
    monthly_listeners1 = Node(1, Node(8, Node(9)))  # 189
    monthly_listeners2 = Node(9, Node(9, Node(9)))  # 999

    print_linked_list(double_listeners(monthly_listeners1))
    print_linked_list(double_listeners(monthly_listeners2))


if __name__ == "__main__":
    main()
