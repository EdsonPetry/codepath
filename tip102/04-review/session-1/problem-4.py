"""
Problem 4: Fabric Pairing
You want to find pairs of fabrics that, when combined, maximize eco-friendliness 
while staying within a budget. Each fabric has a cost associated with it, and your 
goal is to identify the pair of fabrics whose combined cost is the highest possible 
without exceeding the budget.

Write the find_best_fabric_pair() function, which takes a list of fabrics (each with 
a name and cost) and a budget. The function should return the names of the two fabrics 
whose combined cost is the closest to the budget without exceeding it.

Evaluate the time and space complexity of your solution. Define your variables and provide 
a rationale for why you believe your solution has the stated time and space complexity.
"""

"""""""""
sort fabrics
[("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
"""

def main():
    fabrics = [("Organic Cotton", 30), ("Recycled Polyester", 20), ("Bamboo", 25), ("Hemp", 15)]
    fabrics_2 = [("Linen", 50), ("Recycled Wool", 40), ("Tencel", 30), ("Organic Cotton", 60)]
    fabrics_3 = [("Linen", 40), ("Hemp", 35), ("Recycled Polyester", 25), ("Bamboo", 20)]

    print(find_best_fabric_pair(fabrics, 45))
    print(find_best_fabric_pair(fabrics_2, 70))
    print(find_best_fabric_pair(fabrics_3, 60))

    """
    Example output:
    ('Hemp', 'Organic Cotton')
    ('Tencel', 'Recycled Wool')
    ('Bamboo', 'Linen')
    """


def find_best_fabric_pair(fabrics, budget):
    if len(fabrics) == 0:
        return []

    fabric_1 = ""
    fabric_2 = ""

    fabrics.sort(key=lambda pair: pair[1])

    left = 0
    right = len(fabrics) - 1

    while right > left:
        if fabrics[right][1] + fabrics[left][1] == budget:
            return (fabrics[right][0], fabrics[left][0])
        elif fabrics[right][1] + fabrics[left][1] > budget:
            right -= 1
        else:
            fabric_1 = fabrics[right][0]
            fabric_2 = fabrics[left][0]
            left += 1

    return (fabric_1, fabric_2)

if __name__ == "__main__":
    main()

