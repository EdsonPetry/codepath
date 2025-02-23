from collections import defaultdict

def main():
    message1 = "sphinx of black quartz judge my vow"
    message2 = "trust me"
    message3 = "Sphinx o432f black q32uartz !4judg54^e my vow"
    message4 = ""

    print(can_trust_message(message1))
    print(can_trust_message(message2))
    print(can_trust_message(message3))
    print(can_trust_message(message4))
    
def can_trust_message(message):
    dict1=defaultdict(int)
    for i in range(97, 123):
        dict1[chr(i)] = 0
    
    for c in (message.lower()):
        if c in dict1:
            dict1[c]+=1
    
    for j in dict1.values():
        if j==0:
            return False
    return True


if __name__ == "__main__":
    main()