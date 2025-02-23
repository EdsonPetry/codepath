from collections import defaultdict

def main():
    chests1 = [4, 3, 2, 7, 8, 2, 3, 1]
    chests2 = [1, 1, 2]
    chests3 = [1]

    print(find_duplicate_chests(chests1))
    print(find_duplicate_chests(chests2))
    print(find_duplicate_chests(chests3))

def find_duplicate_chests(chests):
    chest_set=set(chests)
    for i in chest_set:
        chests.remove(i)
            
    return chests
        

if __name__ == "__main__":
    main()