def main():
    word = "Trigger"
    print(tiggerfy(word))

    word = "eggplant"
    print(tiggerfy(word))

    word = "Choir"
    print(tiggerfy(word))

def tiggerfy(word):
    word = word.lower()
    sub_strs = ["t", "i", "gg", "er"]
    for s in sub_strs:
        word = word.replace(s, "")
    return word


if __name__=="__main__":
    main()