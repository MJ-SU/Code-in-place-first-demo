
def convert_c_to_f(celsius):
    """Convert Celsius to Fahrenheit."""
    return (celsius * 9/5) + 32
def main():
    celsius = int(input("Enter temperature in Celsius: "))
    temperature_f = convert_c_to_f(celsius)
    print(f"{celsius}°C is {temperature_f}°F")

if __name__ == "__main__":
    main()