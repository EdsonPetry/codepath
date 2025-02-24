def main():
    item_quantities = [2, 4, 6, 8]
    print(can_pair(item_quantities))

    item_quantities = [1, 2, 3, 4]
    print(can_pair(item_quantities))

    item_quantities = []
    print(can_pair(item_quantities))

def can_pair(item_quanitities: list) -> bool:
    return all(item % 2 == 0 for item in item_quanitities)

if __name__ == "__main__":
    main()