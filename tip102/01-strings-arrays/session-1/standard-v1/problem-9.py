def main():
    item_quantities = [2, 4, 6, 8]
    can_pair(item_quantities)

    item_quantities = [1, 2, 3, 4]
    can_pair(item_quantities)

    item_quantities = []
    can_pair(item_quantities)

def can_pair(item_quanitities):
    return len(item_quanitities) % 2 == 0

if __name__ == "__main__":
    main()