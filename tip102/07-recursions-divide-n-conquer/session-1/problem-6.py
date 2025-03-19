"""
Problem 6: Strongest Avenger
The Avengers need to determine who is the strongest. Given a list of their
strengths, find the maximum strength using a recursive approach without using
the max() function.

Evaluate the time complexity of your solution. Define your variables and provide
a rationale for why you believe your solution has the stated time complexity.

Example Output:

100
Example 1 Explanation: The maximum strength among the Avengers is 100.

90
Example 2 Explanation: The maximum strength among the Avengers is 90.
"""


def strongest_avenger(strengths, curr_max=0):
    if len(strengths) == 1:
        if strengths[0]>curr_max:
            return strengths[0]
        else:
            return curr_max
    half = len(strengths)//2
    #return the max of left and right subarray
    left = strongest_avenger(strengths[:half], curr_max)
    right = strongest_avenger(strengths[half:], curr_max)
    if left>right:
        return left
    else:
        return right
    


def main():
    print(strongest_avenger([88, 92, 95, 99, 97, 100, 94]))
    print(strongest_avenger([50, 75, 85, 60, 90]))


if __name__ == "__main__":
    main()
