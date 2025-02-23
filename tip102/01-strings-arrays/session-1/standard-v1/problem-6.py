def main():
    hunny_jars = [1, 2, 3]
    print(doubled(hunny_jars))


def doubled(hunny_jars: list) -> list:
    return [jar * 2 for jar in hunny_jars]


if __name__ == "__main__":
    main()
