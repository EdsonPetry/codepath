"""
Problem 7: Identify Repeated Themes
Themes often recur across different scenes to reinforce key ideas or emotions. 
Identifying these repeated themes is crucial for analyzing the narrative structure 
and ensuring thematic consistency. Write a function that, given a list of scenes with 
their associated themes, identifies themes that appear more than once and returns a list 
of these repeated themes.

Track the occurrence of each theme and then extract and return the themes that appear more than once.

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution has the stated time and space complexity.
"""

def main():
    scenes = [
        {"scene": "The hero enters the dark forest.", "theme": "courage"},
        {"scene": "A mysterious figure appears.", "theme": "mystery"},
        {"scene": "The hero faces his fears.", "theme": "courage"},
        {"scene": "An eerie silence fills the air.", "theme": "mystery"},
        {"scene": "The hero finds a hidden treasure.", "theme": "discovery"}
    ]

    repeated_themes = identify_repeated_themes(scenes)
    print(repeated_themes)

    scenes = [
        {"scene": "The spaceship lands on an alien planet.", "theme": "exploration"},
        {"scene": "A strange creature approaches.", "theme": "danger"},
        {"scene": "The crew explores the new world.", "theme": "exploration"},
        {"scene": "The crew encounters hostile forces.", "theme": "conflict"},
        {"scene": "The crew makes a narrow escape.", "theme": "danger"}
    ]

    repeated_themes = identify_repeated_themes(scenes)
    print(repeated_themes)
    """
    Example Output:

    ['courage', 'mystery']
    ['exploration', 'danger']
    """
def identify_repeated_themes(scenes):
    visited = set()
    res = set()

    for theme in scenes:
        if theme["theme"] in visited:
            res.add(theme['theme'])
        else:
            visited.add(theme['theme'])

    return list(res)
if __name__ == "__main__":
   main()