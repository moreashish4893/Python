#  Q. Write a program using functions to Compute the monthly payment, given the loan amount, number of years and
# the annual interest rate.



def compute_monthly_payment(loan_amount, annual_interest_rate, years):
    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = annual_interest_rate / 12 / 100
    
    # Convert years to total number of monthly payments
    num_payments = years * 12
    
    # Calculate monthly payment using the formula
    if monthly_interest_rate > 0:
        monthly_payment = loan_amount * (monthly_interest_rate * (1 + monthly_interest_rate)**num_payments) / ((1 + monthly_interest_rate)**num_payments - 1)
    else:
        # If interest rate is 0, simplify the formula
        monthly_payment = loan_amount / num_payments
    
    return monthly_payment



