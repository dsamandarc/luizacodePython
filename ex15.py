# 15)For the Python program in the ex15.py file.
# In a house, a family decided to share the value of the energy bill among the residents of the house. 
# In the program they inform the value of the energy bill and how many will divide the bill in the month.
# The program will calculate how much each should contribute to the energy bill.
energy_bill_value = float(input("Enter the value of your energy bill:"))
number_of_residents = int(input("Enter the number of residents of the house:"))
energy_by_residents = energy_bill_value/number_of_residents
print("Each resident of the house will pay:", energy_by_residents, 'reais')
#return:
# Enter the value of your energy bill:856
# Enter the number of residents of the house:5
# Each resident of the house will pay: 171.2 reais