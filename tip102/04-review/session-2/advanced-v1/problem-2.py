"""
Problem 2: Find Most Frequent Keywords
Identify the most frequently used keywords from a dictionary where the keys are scene names 
and the values are lists of keywords used in each scene. Return the keyword that appears the
most frequently across all scenes. If there is a tie, return all the keywords with the highest frequency.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""
from collections import defaultdict

def main():
    scenes = {
        "Scene 1": ["action", "hero", "battle"],
        "Scene 2": ["hero", "action", "quest"],
        "Scene 3": ["battle", "strategy", "hero"],
        "Scene 4": ["action", "strategy"]
    }
    print(find_most_frequent_keywords(scenes))

    scenes = {
        "Scene A": ["love", "drama"],
        "Scene B": ["drama", "love"],
        "Scene C": ["comedy", "love"],
        "Scene D": ["comedy", "drama"]
    }
    print(find_most_frequent_keywords(scenes)) 
    """
    Example Output:

    ['action', 'hero']
    ['love', 'drama']
    """

def find_most_frequent_keywords(scenes):


    val_dict = defaultdict(int)
    for k,v in scenes.items():
        for words in v:
            val_dict[words]+=1

    max_val = 0

    for k, v in val_dict.items():
        if v>=max_val:
            max_val=v

    lst=[]
    for k, v in val_dict.items():
        if v == max_val:
            lst.append(k)
    
    return lst





    


  

if __name__ == "__main__":
   main()