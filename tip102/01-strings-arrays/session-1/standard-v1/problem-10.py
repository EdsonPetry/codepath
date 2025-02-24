def main():
    quantity = 6
    print(split_haycorns(quantity))

    quantity = 1
    print(split_haycorns(quantity))

def split_haycorns(quantity: int) -> list:
    return [i for i in range(1, quantity+1) if quantity % i == 0]

if __name__ == "__main__":
    main()