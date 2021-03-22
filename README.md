# Python Payment Calculator

This is a simple calculator that will calculate loan monthly payments, total interest, and total payment based on the loan parameters inputted.

## Setup

- Make sure you have Python 3 installed on your local machine. If you are unsure of how to install it or check that its installed, the [Visual Studio Python Tutorial](https://code.visualstudio.com/docs/python/python-tutorial#_prerequisites) is a great resource.
- If you are using VS Code, you can simply choose your interpreter and run this code through the IDE as described in the link above.
- If you would rather run via command line, simply run:
  - `python3 /path/to/calculate.py`

## Using the program

- Simply enter your loan amount, interest percentage, down payment, and term as they are prompted by typing in a number and then hitting ENTER.
    - Note that the only input that allows decimals is the interest percentage.
- Once you are finished inputting the loan details, you should see the output like so:
  - Loan Payment Calculator  
    Enter amount (ex. 100000): 10000  
    Enter interest percentage (ex. 5.5): 5.5  
    Enter down payment (ex. 20000): 3535  
    Enter term in years (ex. 30): 7  
    {  
    "monthly payment": "92.90",  
    "total interest": "1338.80",  
    "total payment": "11338.80"  
    }

## Testing

Running tests with VS Code is incredibly easy. Since I have included the .vscode folder with settings for the test, the configuration is already in place. If you don't already have unittest installed, VS Code will prompt you to install it. Then just run 'Python: Discover Tests' and 'Python: Run All Tests' in the Command Palette. These commands can also be found on the blue bar on the bottom of VS Code.