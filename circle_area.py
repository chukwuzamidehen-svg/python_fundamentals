# Module 2 - Python Fundamentals
# Circle Area Calculator
# Calculates the area of a circle using a radius entered by the user.

while True:
    try:
        radius = float(input("Enter the circle's radius: "))

        if radius <= 0:
            print("Please enter a number greater than zero.")
            continue

        break

    except ValueError:
        print("Invalid input. Please enter a number.")

area = 3.14 * radius**2

print(f"\nCircle radius: {radius}")
print(f"Circle area: {area:.2f} square units")

# String transformation and analysis
result = f"Circle with radius {radius}"
print("Uppercase:", result.upper())
print("Number of words:", len(result.split()))
