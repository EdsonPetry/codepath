def main():
    s = "suspicerous"
    print(tiggerfy(s))

    s = "Trigger"
    print(tiggerfy(s))

    s = "Hunny"
    print(tiggerfy(s))

def tiggerfy(s: str) -> str:
    return "".join([c for c in s if c.lower() not in "tigger"])

if __name__ == "__main__":
    main()