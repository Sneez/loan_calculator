import json

print("Loan Payment Calculator")

# accept input from user and validate the type, whether it be int or float
def acceptInput(prompt, inputType):
    while True:
        num = input(prompt)
        # catch inputs that are too big
        if len(str(num)) > 15:
            print("Please input a value with less than 15 digits")
        else:
            # type cast input depending on input type to confirm correct type
            try:
                if inputType == 'int':
                    val = int(num)
                elif inputType == 'float':
                    val = float(num)
                # check for negative numbers
                if val < 0:
                    print("Please enter a positive number")
                else:
                    return val
                    break
            # show error message if input was bad, let user try again
            except ValueError:
                if inputType == 'int':
                    print("This is not an integer. Please enter a valid integer (ex. 1000)")
                elif inputType == 'float':
                    print("This is not a floating point number. Please enter a valid floating point number (ex. 5.5)")

def main():
    # get the inputs from the user
    amount = acceptInput("Enter loan amount (ex. 100000): ", 'int')
    interest = acceptInput("Enter interest percentage (ex. 5.5): ", 'float')
    downPayment = acceptInput("Enter down payment (ex. 20000): ", 'int')
    term = acceptInput("Enter term in years (ex. 30): ", 'int')

    #calculate outputs

    A = amount - downPayment
    n = 12 * term
    r = (interest * 0.01) / 12
    D = ((1 + r)**n - 1) / (r * (1 + r)**n)

    monthlyPay = A / D
    totalPay = downPayment + (monthlyPay * term * 12)
    totalInterest = totalPay - amount

    # organize output without changing actual values
    # round to two decimals and then output string to ensure 2 decimals are used
    outputDict = {
        "monthly payment": f'{round(monthlyPay, 2):.2f}',
        "total interest": f'{round(totalInterest, 2):.2f}',
        "total payment": f'{round(totalPay, 2):.2f}'
    }

    print(json.dumps(outputDict, indent = 0))

if __name__=="__main__":
    main()

