"""
Problem 2: Greet Player
Step 1: Using the Villager class from Problem 1, add the following greet_player() method to your existing code:

Step 2: Create a second instance of Villager in a variable named bones.

The Villager object created should have name "Bones", species "Dog", and catchphrase "yip yip".
Step 3: Call the method greet_player() with your name and print out "Bones: Hey there, <your name>! How's it going, yip yip!". For example, if your name is Tram, "Bones: Hey there, Tram! How's it going, yip yip?" would be printed out to the console.

Example Usage:

print(bones.name)
print(bones.species)  
print(bones.catchphrase) 
print(bones.furniture) 
Example Output:
Bones
Dog
yip yip
[]
"""

"""
Problem 3: Update Catchphrase
In Animal Crossing, as players become friends with villagers, the villagers might ask the player to suggest a new catchphrase.

Adding on to your existing code, update bones so that his catchphrase is "ruff it up" instead of its current value, "yip yip".

Example Usage:

print(bones.greet_player("Samia"))
Example Output:

Bones: Hey there, Samia! How's it going, ruff it up!
"""
class Villager:
    def __init__(self, name, species, catchphrase):
        self.name = name
        self.species = species
        self.catchphrase = catchphrase
        self.furniture = []

    def greet_player(self, player_name):
        return f"{self.name}: Hey there, {player_name}! How's it going, {self.catchphrase}!"

def main():
    bones = Villager("Bones", "Dog", "ruff it up")
    print(bones.greet_player("Edson"))

if __name__ == "__main__":
    main()