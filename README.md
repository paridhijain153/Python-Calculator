Basic Calculator using Python and Tkinter
Project Overview
This project is a basic desktop calculator developed using Python and Tkinter.

The application provides a graphical user interface (GUI) with a display screen and clickable buttons for entering numbers and arithmetic operators.
Features
- Simple graphical user interface
- Number buttons from 0 to 9
- Addition (+)
- Subtraction (-)
- Multiplication (*)
- Division (/)
- Equals (=) button to calculate the result
- Clear (C) button to clear the display
- Basic handling of invalid expressions and arithmetic errors, including division by zero
Technologies Used
- Python — application logic
- Tkinter — graphical user interface
- Regular expressions (re) — basic expression-character validation
- Visual Studio Code — code editor
- GitHub — source-code hosting (if uploaded)
Project Structure
BasicCalculator/
├── calculator.py
└── README.md
Requirements
- Python 3 installed
- Tkinter available in your Python installation
Tkinter is commonly included with standard Python installations on Windows. Some Linux distributions may require a separate Tkinter package.
How to Run
1. Download or clone this repository.
2. Open the project folder in Visual Studio Code or a terminal.
3. Open a terminal in the project folder.
4. Run the following command:
   python calculator.py
   On Windows, if python is not recognized, try:
   py calculator.py
A calculator window should open.
How to Use
1. Click number buttons to enter digits.
2. Click an arithmetic operator (+, -, *, or /).
3. Continue entering numbers and operators to form an expression.
4. Click = to calculate and display the result.
5. Click C to clear the display.
Testing Checklist
Try these examples after launching the application:
Expression / Action	Expected result
7+3, then =	10
9-4, then =	5
6*5, then =	30
8/2, then =	4.0
5/0, then =	Error
Click C	Display is cleared


Implementation Notes
- tk.Tk() creates the main application window.
- tk.Entry() creates the display field.
- tk.StringVar() connects a variable to the display.
- tk.Button() creates the clickable controls.
- grid() arranges the display and buttons in rows and columns.
- press() appends a number or operator to the display.
- clear() clears the display.
- calculate() validates and evaluates the expression, then displays the result.
- mainloop() starts Tkinter's event loop so the application can respond to user actions.
The current implementation uses Python's eval() to evaluate arithmetic expressions after restricting the allowed characters and disabling built-ins. This is a simple learning-project approach; a dedicated arithmetic parser is preferable for production applications.
Learning Outcomes
This project provides practice with:
- Core Python syntax and functions
- Tkinter widgets and GUI layout
- Event-driven programming and button callbacks
- Conditional statements, loops and lambda functions
- Exception handling
- Running Python programs in Visual Studio Code
- Preparing code for GitHub

Author
Paridhi Jain
