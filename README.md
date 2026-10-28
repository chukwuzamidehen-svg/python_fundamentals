# Python Fundamentals

**Course:** INFO-U762 Interoperability  
**Assignment:** Module 2 - Python Fundamentals

## Project Overview

This repository contains two basic Python programs that demonstrate user input, mathematical calculations, string manipulation, and exception handling.

## Programs

### 1. Circle Area Calculator (`circle_area.py`)

This program asks the user to enter the radius of a circle and calculates its area using the formula:

Area = 3.14 × radius²

The program checks for invalid inputs and requires the radius to be greater than zero.

### 2. Temperature Converter (`temperature_converter.py`)

This program asks the user to enter a temperature in Celsius and converts it to Fahrenheit using:

Fahrenheit = (Celsius × 9/5) + 32

The program handles invalid inputs and allows negative temperatures.

## How to Run

1. Install Python 3.
2. Open either Python file in VS Code.
3. Run the file using the Python extension or terminal.
4. Follow the instructions displayed in the terminal.

## Testing

**Circle Area Calculator**

- Entered 5 and received an area of 78.50.
- Entered a negative radius and received an error message.
- Entered 0 and was prompted to try again.
- Entered letters instead of numbers and received an error message.

**Temperature Converter**

- Entered 0°C and received 32°F.
- Entered 100°C and received 212°F.
- Entered -40°C and received -40°F.
- Entered letters instead of numbers and received an error message.

Both programs demonstrate string transformation using `.upper()` and string analysis using `.split()`.

## Assumptions

The circle calculator uses 3.14 for pi as permitted by the assignment. The temperature converter accepts negative temperatures. Both programs require numeric input and prompt the user to retry if the input is invalid.
