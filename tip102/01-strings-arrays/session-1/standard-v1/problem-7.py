def main():
    race_times = [1, 2, 3, 4, 5, 6]
    threshold = 4
    print(count_less_than(race_times, threshold))

    race_times = []
    threshold = 4
    print(count_less_than(race_times, threshold))

def count_less_than(race_times: list, threshold: int) -> int:
    if threshold < 0:
        raise ValueError("Threshold must be a non negative number!")
    
    return len([times for times in race_times if times < threshold])

if __name__ == "__main__":
    main()