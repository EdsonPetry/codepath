def main():
    word = "Trigger"
    print(tiggerfy(word))

    word = "eggplant"
    print(tiggerfy(word))

    word = "Choir"
    print(tiggerfy(word))

def tiggerfy(word: str) -> str:
    return word.lower().replace("t", "").replace("i", "").replace("gg", "").replace("er", "")

if __name__ == "__main__":
    main()