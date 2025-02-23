def main():
    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 2
    print(get_item(items, x))

    items = ["piglet", "pooh", "roo", "rabbit"]
    x = 5
    print(get_item(items, x))

def get_item(items: list, x: int):
    return items[x] if x < len(items) else None

if __name__ == "__main__":
    main()