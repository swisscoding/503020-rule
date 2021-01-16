#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | 50-30-20 strategy | ----\n", fg("red")))

# user interaction
after_tax_income = float(input("Your after tax income: "))

# function
def calculate(income):
    print(stylize("\nApportionment through 50-30-20 strategy:", fg("green")))
    apportionment = {
        "Needs": round(income / 100 * 50, 2),
        "Wants": round(income / 100 * 30, 2),
        "Savings": round(income / 100 * 20, 2)
    }

    for key in apportionment:
        value = stylize(apportionment[key], fg("red"))
        print(f"{key} -> {value}")

    print()

calculate(after_tax_income)
