"""
Problem 2: Merge Playlists
You are given the head of two linked lists, playlist1 and playlist2 with lengths n
 and m respectively. Remove playlist1's nodes from the ath to the bth node and put
 playlist2 in its place. Assume the lists are 0-indexed.

The blue edges and nodes in the figure below indicate the result:

Merged playlists

Evaluate the time and space complexity of your solution. Define your variables and
provide a rationale for why you believe your solution has the stated time and space
complexity.

Example Output:

('Flea', 'St.Vincent') -> ('Juice', 'Lizzo') -> ('Dreams', 'Solange') -> ('First', 'Gallant') -> ('Empty', 'Kevin Abstract')

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


def merge_playlists(playlist1, playlist2, a, b):
    
    if not playlist1 and not playlist2: 
        return None
    
    curr = playlist1

    a_prev = None
    b_next = None

    count = 0
    while curr:
        if count == a - 1:
            a_prev = curr
        if count == b + 1:
            b_next = curr
        curr = curr.next
        count += 1
    
    a_prev.next = playlist2

    curr2 = playlist2

    while curr2 and curr2.next:
        curr2 = curr2.next

    curr2.next = b_next

    return playlist1



def main():
    playlist1 = Node(
        ("Flea", "St. Vincent"),
        Node(
            ("Juice", "Lizzo"),
            Node(
                ("Tenderness", "Jay Som"),
                Node(("Ego Death", "The Internet"), Node(("Empty", "Kevin Abstract"))),
            ),
        ),
    )

    playlist2 = Node(("Dreams", "Solange"), Node(("First", "Gallant")))

    print_linked_list(merge_playlists(playlist1, playlist2, 2, 3))


if __name__ == "__main__":
    main()
