# 16)Program ex16.py: I'm trying to understand my bank's fees. 
# For this, he reported this formula:
# final_value = loan_value + (loan_value * rate * time)
# where:
# ● loan_value: It is the amount that I will borrow.
# ● rate: It is the amount of the fee per month. For example: if it is 4% per month, the value will be 0.04.
# ● time: Number of months that I will repay the loan.
# Create a program that collects each of these values to calculate the final value that will be paying the bank.
loan_value = input("Enter the amount that you will borrow:")
fee = input("Enter the fee per month [in percentage]:")
months = input("Enter the number of months that you will repay the loan:")
loan_value = float(loan_value)
fee2 = float(fee)/100
months = float(months)
final_value = loan_value + (loan_value*fee2*months)
print("The final value that you will be paying the bank is:", final_value, 'reais')