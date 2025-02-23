def main():
    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))

def final_value_after_operations(operations):
    tigger = 1
    for op in operations:
        if op in ["bouncy", "flouncy"]:
            tigger += 1
        elif op in ["trouncy", "pouncy"]:
            tigger -= 1
    return tigger
     

if __name__ == "__main__":
    main()