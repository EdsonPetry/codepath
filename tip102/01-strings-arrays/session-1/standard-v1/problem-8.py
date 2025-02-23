def main():
    tasks = [
        "Count all the bees in the hive",
        "Chase all the clouds from the sky",
        "Think",
        "Stoutness Exercises",
    ]
    print_todo_list(tasks)

    tasks = []
    print_todo_list(tasks)

def print_todo_list(tasks: list) -> None:
    print("Pooh's To Dos:")
    for i in range(len(tasks)):
        print(f"{i+1}. {tasks[i]}")

if __name__ == "__main__":
    main()