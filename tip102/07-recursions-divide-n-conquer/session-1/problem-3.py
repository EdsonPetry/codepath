"""
Problem 3: Counting Unique Suits
Some of Iron Man's suits are duplicates. Given a list of strings suits where each
 string is a suit in Stark's collection, count the total number of unique suits
 in the list.

Implement the solution iteratively.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?
Evaluate the time complexity of each solution. Are they the same? Define your
variables and provide a rationale for why you believe your solution has the stated
time complexity.

Example Output:
3
2
"""


def count_suits_iterative(suits):
    return len(set(suits))


def count_suits_recursive(suits, unique_set):
    if len(suits) == 1:
        unique_set.add(suits[0])
        return unique_set
    half = len(suits)//2
    count_suits_recursive(suits[0:half], unique_set)
    count_suits_recursive(suits[half:len(suits)],unique_set)
    return len(unique_set)


def main():
    print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
    print(count_suits_recursive(["Mark I", "Mark I", "Mark III"], set()))


if __name__ == "__main__":
    main()
