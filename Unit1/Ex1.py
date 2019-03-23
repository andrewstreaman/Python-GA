"""
	1. The purpose of this program is to calculate the total amount of principal and interest expected to be paid by the borrower.
	2. The user (borrower) is required to submit distinct inputs
		a. Principal = this is the total amount the borrower is asking the lender to lend
		b. Rate = interest rate applied to the loan
		c. Compound = "payment_frequency_per_year" =frequency of payments
		d. Time = "total_years" = Total amount of time the loan will be outstanding prior to maturity
There is a calculation [A = P(1 + r/n)^n] that is applied to the user inputs. The output will be the total amount of principal and interest due from the borrower.
"""

"""
principal = float(input("Please enter the loan amount"))
rate = float(input("Please enter the interest rate"))
compound = float(input("Please enter the frequency of payments"))
time = float(input("Please enter the time until maturity of the loan"))

"""
principal = 10000.0
rate = 4.875
payment_frequency_per_year = 12.0
total_years = 7.5

percentage_points = 100  # this is not a user input

total_balance = principal * ((1 + ((rate / percentage_points) / payment_frequency_per_year))) ** (
            payment_frequency_per_year * total_years)

answer = 14403.47392844136
print(round(answer, 4))

print("You owe a total balance of", round(total_balance, 4))

""""
For future considerations:
    Include a start and end date
Have the total_years calculate from that
define payment_frequency by "monthly", "semi-annual", or "annual"
"""

















