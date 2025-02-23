def main():
    nums = [4, 2, 3]
    print(non_decreasing(nums))

    nums = [4, 2, 1]
    print(non_decreasing(nums))

def non_decreasing(nums):
    if len(nums) < 2:
        
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            return False
    return True

if __name__ == "__main__":
    main()