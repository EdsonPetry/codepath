def main():
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    print(linear_search(items, target))

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    print(linear_search(items, target))

def linear_search(lst: list, target: int) -> int:
    return lst.index(target) if target in lst else -1

if __name__ == "__main__":
    main()