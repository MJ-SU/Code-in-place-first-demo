
print("Hello, World!")
def greet(name):
    """Greet the user by name."""
    return f"Hello, {name}!"
def main():
    user_name = input("Enter your name: ")
    print(greet(user_name))

if __name__ == "__main__":
    main()