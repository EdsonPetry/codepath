def main():
    treasure_map1 = {
        "Cove": 3,
        "Beach": 7,
        "Forest": 5
    }

    treasure_map2 = {
        "Shipwreck": 10,
        "Cave": 20,
        "Lagoon": 15,
        "Island Peak": 5
    }

    print(total_treasures(treasure_map1)) 
    print(total_treasures(treasure_map2)) 

def total_treasures(treasure_map):
    sum=0
    for t in treasure_map.values():
        sum+=t
    return sum

if __name__ == "__main__":
    main()