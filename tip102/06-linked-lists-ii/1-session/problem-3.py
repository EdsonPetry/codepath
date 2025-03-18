"""
Problem 3: Shuffle Playlist
You are given the head of a singly linked list playlist. The list can be represented as:

L0 → L1 → … → Ln - 1 → Ln

Shuffle the playlist to have the following form:

L0 → Ln → L1 → Ln-1 → L2 → Ln-2 → …

You may not modify the values in the list's nodes. Only the order of the nodes themselves
may be changed. Return the head of the shuffled list.

Evaluate the time and space complexity of your solution. Define your variables and provide
a rationale for why you believe your solution has the stated time and space complexity.

Example Output:

1 -> 4 -> 2 -> 3
('Respect', 'Aretha Franklin') -> ('Bohemian Rhapsody', 'Queen') -> ('Superstition', 'Stevie Wonder') ->
('Like a Prayer', 'Madonna') -> ('Wonderwall', 'Oasis')

L0 → L1 → … → Ln - 1 → Ln

Ln -> Ln-1 -> ... -> L1 -> L0

L0 -> Ln -> L1 

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


def shuffle_playlist(playlist):
    pass


def main():
    # Linked List playlist1 before and after shuffling

    playlist1 = Node(1, Node(2, Node(3, Node(4))))

    playlist2 = Node(
        ("Respect", "Aretha Franklin"),
        Node(
            ("Superstition", "Stevie Wonder"),
            Node(
                ("Wonderwall", "Oasis"),
                Node(
                    ("Like a Prayer", "Madonna"), Node(("Bohemian Rhapsody", "Queen"))
                ),
            ),
        ),
    )

    print_linked_list(shuffle_playlist(playlist1))
    print_linked_list(shuffle_playlist(playlist2))


if __name__ == "__main__":
    main()
