def print_pattern(n):
    for i in range(1, n + 1):
        # Print numbers from 1 to i in ascending order
        for j in range(1, i + 1):
            print(j, end='')
        print()

    # Print numbers from 1 to n in descending order
    for i in range(n - 1, 0, -1):
        for j in range(1, i + 1):
            print(j, end='')
        print()


if __name__ == "__main__":
    n = 5  # You can change this value to modify the pattern size
    print_pattern(n)