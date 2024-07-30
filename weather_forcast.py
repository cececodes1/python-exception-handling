def fahrenheit_to_celsius(fahrenheit):
    try:
        fahrenheit = float(fahrenheit)
        celsius = (fahrenheit - 32) * 5/9
        return celsius
    except ValueError:
        print("Error: Invalid input. Please enter a numeric value.")
        return None

def main():
    fahrenheit = input("Enter the temperature in Fahrenheit: ")
    celsius = fahrenheit_to_celsius(fahrenheit)
    if celsius is not None:
        print(f"{fahrenheit} degrees Fahrenheit is {celsius:.2f} degrees Celsius.")
    else:
        print("Unable to convert temperature.")    
    print("Thank you for using the weather forecast application!")

if __name__ == "__main__":
    main()
