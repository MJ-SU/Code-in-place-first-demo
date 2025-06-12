
MAX_NUMBER = 50
def is_even(i):
    """Check if the number is even."""
    return i % 2 == 0
def main():
    for i in range(1, MAX_NUMBER + 1):
        if is_even(i):
            print(f"{i} is even")
        else:
            print(f"{i} is odd")
if __name__ == "__main__":
    main()