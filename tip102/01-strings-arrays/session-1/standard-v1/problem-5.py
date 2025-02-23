def main():
    hunny_jars = [2, 3, 4, 5]
    print(sum_honey(hunny_jars))

    hunny_jars = []
    print(sum_honey(hunny_jars))


def sum_honey(hunny_jars: list) -> int:
    return sum(hunny_jars)


if __name__ == "__main__":
    main()
