# 14) Create the following Python program in the ex14.py file.
# Collect the age of two people.
# And inform if the first age is bigger than the first one. 
# In this one, just answer True to inform that the first age is greater than the first.
age_1 = int(input("Enter your age:"))
age_2 = int(input("Enter your age:"))
comparison = age_1 > age_2
if comparison == True:
    print(f'{comparison}:The first age is bigger than the second')
    
    