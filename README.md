Python Calculator
A simple command-line calculator built with Python. It provides common arithmetic operations through an interactive menu and validates user input.
Requirements
Python 3.8 or newer
No third-party packages are required. The calculator uses Python's built-in `math` module.
How to Run
Save `calculator.py` to a folder.
Open a terminal or Command Prompt in that folder.
Run:
```bash
   python calculator.py
   ```
If your system uses `python3`, run:
```bash
   python3 calculator.py
   ```
Choose an operation by entering its menu number.
Enter the requested number(s).
Enter `0` to exit.
Available Functions
Menu option	Function	Description	Example
1	`add(a, b)`	Adds two numbers	`add(4, 3)` → `7`
2	`subtract(a, b)`	Subtracts the second number from the first	`subtract(4, 3)` → `1`
3	`multiply(a, b)`	Multiplies two numbers	`multiply(4, 3)` → `12`
4	`divide(a, b)`	Divides the first number by the second	`divide(6, 3)` → `2`
5	`power(a, b)`	Raises the first number to the second number's power	`power(2, 3)` → `8`
6	`modulus(a, b)`	Returns the remainder of division	`modulus(7, 3)` → `1`
7	`square\_root(a)`	Calculates the square root of a non-negative number	`square\_root(25)` → `5`
0	Exit	Closes the calculator	—
Input and Error Handling
Invalid number: The program asks again if text that is not a valid number is entered.
Division by zero: Displays an error instead of crashing.
Modulus by zero: Displays an error instead of crashing.
Square root of a negative number: Displays an error because this calculator supports real-number square roots only.
Invalid menu choice: Shows a message and returns to the menu.
Code Structure
Arithmetic functions: Perform the individual calculations.
`get\_number(prompt)`: Keeps asking until a valid numeric input is provided.
`format\_result(value)`: Displays whole-number results without a trailing `.0`.
`main()`: Displays the menu, reads the user's selection, runs the selected operation, and handles errors.
`if \_\_name\_\_ == "\_\_main\_\_":`: Starts the interactive calculator when the file is run directly.
Example Session
```text
PYTHON CALCULATOR

Choose an operation:
1. Addition (+)
2. Subtraction (-)
3. Multiplication (\*)
4. Division (/)
5. Power (a \*\* b)
6. Modulus (remainder)
7. Square root (√a)
0. Exit

Enter your choice: 1
Enter a number: 10
Enter the second number: 5
Result (Addition (+)): 15
```
License
You may use and modify this project for learning and personal use.
