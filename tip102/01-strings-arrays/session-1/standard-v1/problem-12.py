def main():
    items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
    print(locate_thistles(items))

    items = ["book", "bouncy ball", "leaf", "red balloon"]
    print(locate_thistles(items))

def locate_thistles(items: list) -> list:
    return [i for i in range(len(items)) if items[i].lower() == "thistle"]

if __name__ == "__main__":
    main()