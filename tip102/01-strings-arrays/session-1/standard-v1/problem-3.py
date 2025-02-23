def main():
    print_catchphrase("Pooh")
    print_catchphrase("tigger")
    print_catchphrase("Piglet")

def print_catchphrase(character: str) -> None:
    match character.lower():
        case "pooh":
            print("Oh bother!")
        case "tigger":
            print("TTFN: Ta-ta for now!")
        case "eeyore":
            print("Thanks for noticing me.")
        case "christopher robin":
            print("Silly old bear.")
        case _:
            print(f"Sorry! I don't know {character}'s catchphrase!")

if __name__ == "__main__":
    main()