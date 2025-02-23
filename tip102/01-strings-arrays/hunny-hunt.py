def main():
    items = ['haycorn', 'haycorn', 'haycorn', 'hunny', 'haycorn']
    target = 'hunny'
    print(linear_search(items, target))

    items = ['bed', 'blue jacket', 'red shirt', 'hunny']
    target = 'red balloon'
    print(linear_search(items, target))

def linear_search(lst, target):
    for i in range(len(lst)):
        if lst[i] == target:
            return i
    return -1

if __name__ == "__main__":
    main()