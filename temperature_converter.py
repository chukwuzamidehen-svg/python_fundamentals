# Module 2 - Python Fundamentals
# Celsius to Fahrenheit Converter
# Converts user-entered Celsius temperatures to Fahrenheit.

while True:
    try:
        Celsius = float(input("Enter temperature in Celsius: "))
        break

    except ValueError:
        print("Invalid input. Please enter a number.")

fahrenheit = (Celsius * 9 / 5) + 32

result = f"{Celsius} Celsius = {fahrenheit:.2f} Fahrenheit"

print("\n" + result)
print("Uppercase:", result.upper())
print("Word count:", len(result.split()))
