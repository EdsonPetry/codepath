def main():
    operations = ["trouncy", "flouncy", "flouncy"]
    print(final_value_after_operations(operations))

    operations = ["bouncy", "bouncy", "flouncy"]
    print(final_value_after_operations(operations))

def final_value_after_operations(operations: list) -> int:
    tigger = 1
    for op in operations:
        if op.lower() in ["bouncy", "flouncy"]:
            tigger += 1
        elif op.lower() in ["trouncy", "pouncy"]:
            tigger -= 1
    return tigger

if __name__ == "__main__":
    main()