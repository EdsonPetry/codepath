"""
Problem 5: Calculating the Power of the Fantastic Four
The superhero team, The Fantastic Four, are training to increase
their power levels. Their power level is represented as a power of
4. Write a recursive function that calculates the power of 4 raised
to the nth power to determine their training level.

Evaluate the time complexity of your solution. Define your variables
and provide a rationale for why you believe your solution has the
stated time complexity.

Example Output:

16
Example 1 Explanation: 4 to the 2nd power (4 * 4) is 16.
16
Example 2 Explanation: 4 to the -2th power is 1/(4 * 4) is 0.0625.

"""


def power_of_four(n):
    if n == 0:
        return 1
    if n == 1:
        return 4
    if n<0:
        return (1/power_of_four(-n))
    return power_of_four(n-1)*4


def main():
    print(power_of_four(2))
    print(power_of_four(-2))


if __name__ == "__main__":
    main()
