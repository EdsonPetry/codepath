"""
Problem 1: Counting Iron Man's Suits
Tony Stark, aka Iron Man, has designed many different suits over the years. Given a list
of strings suits where each string is a suit in Stark's collection, count the total number
 of suits in the list.

Implement the solution iteratively without the use of the len() function.
Implement the solution recursively.
Discuss: what are the similarities between the two solutions? What are the differences?

Example Output:
3
4
"""


def count_suits_iterative(suits):
    count = 0
    for suit in suits:
        count += 1
    return count


def count_suits_recursive(suits):
    if len(suits) == 1:
        return 1
    half = len(suits)//2
    return count_suits_recursive(suits[0:half])+count_suits_recursive(suits[half:len(suits)])


def main():
    print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
    print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))


if __name__ == "__main__":
    main()
