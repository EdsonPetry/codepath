"""
Problem 1: Count Unique Characters in a Script
Given a dictionary where the keys are character names and the values are lists of their 
dialogue lines, count the number of unique characters in the script.

Evaluate the time and space complexity of your solution. Define your variables and provide 
a rationale for why you believe your solution has the stated time and space complexity.
"""

def main():
    script = {
        "Alice": ["Hello there!", "How are you?"],
        "Bob": ["Hi Alice!", "I'm good, thanks!"],
        "Charlie": ["What's up?"]
    }
    print(count_unique_characters(script)) 

    script_with_redundant_keys = {
        "Alice": ["Hello there!"],
        "Alice": ["How are you?"],
        "Bob": ["Hi Alice!"]
    }
    print(count_unique_characters(script_with_redundant_keys)) 
"""
Example Output:

3
2
"""

def count_unique_characters(script):
  return len(set(script.keys()))

if __name__ == "__main__":
   main()