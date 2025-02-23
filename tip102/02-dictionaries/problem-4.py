def main():
    code1 = "arghh"
    code2 = "haha"

    print(is_balanced(code1)) 
    print(is_balanced(code2)) 
    
def is_balanced(code):
    hist = {}
    for c in code:
        if c in hist:
            hist[c] += 1
        else:
            hist[c] = 1
    # Check if all values are ==
    for v in hist.values():
        ...

if __name__ == "__main__":
    main()