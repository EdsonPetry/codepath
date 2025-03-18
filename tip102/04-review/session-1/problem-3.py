"""
Problem 3: Fashion Trends
In the fast-changing world of fashion, certain materials and practices become trending based on how frequently they are adopted by brands. 
You want to identify which materials and practices are trending. A material or practice is considered "trending" if it appears in the dataset more than once.

Write the find_trending_materials() function, which takes a list of brands (each with a list of materials or practices) and returns a list 
of materials or practices that are trending (i.e., those that appear more than once across all brands).

Evaluate the time and space complexity of your solution. Define your variables and provide a rationale for why you believe your solution 
has the stated time and space complexity.

"""
from collections import defaultdict

def main():
    brands = [
        {"name": "EcoWear", "materials": ["organic cotton", "recycled polyester"]},
        {"name": "GreenThreads", "materials": ["organic cotton", "bamboo"]},
        {"name": "SustainableStyle", "materials": ["bamboo", "recycled polyester"]},
    ]

    brands_2 = [
        {"name": "NatureWear", "materials": ["hemp", "linen"]},
        {"name": "Earthly", "materials": ["organic cotton", "hemp"]},
        {"name": "GreenFit", "materials": ["linen", "recycled wool"]},
    ]

    brands_3 = [
        {"name": "OrganicThreads", "materials": ["organic cotton"]},
        {"name": "EcoFashion", "materials": ["recycled polyester", "hemp"]},
        {"name": "GreenLife", "materials": ["recycled polyester", "bamboo"]},
    ]

    print(find_trending_materials(brands))
    print(find_trending_materials(brands_2))
    print(find_trending_materials(brands_3))

    """
    Example output:
    ['organic cotton', 'recycled polyester', 'bamboo']
    ['hemp', 'linen']
    ['recycled polyester']
    """

def find_trending_materials(brands):
    d = defaultdict(int)

    for brand in brands:
        for material in brand["materials"]:
            d[material] += 1
    
    res = []
    for material in d:
        if d[material] > 1:
            res.append(material)

    return res

if __name__ == "__main__":
    main()
