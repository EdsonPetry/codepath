"""
Problem 8: Merging Missions
The Avengers are planning multiple missions, and each mission has a priority level
represented as a node in a linked list. You are given the heads of two sorted linked
lists, mission1 and mission2, where each node represents a mission with its priority
 level.

Implement a recursive function merge_missions() which merges these two mission lists
into one sorted list, ensuring that the combined list maintains the correct order of
priorities. The merged list should be made by splicing together the nodes from the
first two lists.

Return the head of the merged mission linked list.

Example output:
1 -> 1 -> 2 -> 3 -> 4 -> 4

mission1 = 1 -> 5
mission2 = 2->3->4
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


def merge_missions(mission1, mission2):
    if mission2 
    if mission2.value == mission1.value or (mission2.value >mission1.value and mission2.value<mission1.next.value):
        #do stuff to insert mission2 into mission1
    
        merge_missions(mission1, mission2.next)
    else:
        merge_missions(mission1.next, mission2.next)
    
    pass


def main():
    mission1 = Node(1, Node(2, Node(4)))
    mission2 = Node(1, Node(3, Node(4)))
    print_linked_list(merge_missions(mission1, mission2))


if __name__ == "__main__":
    main()
