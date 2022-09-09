# 10)Collect the name of person, her city of birth, and the year she was born. 
# Then you will show the data collected on different lines. 
# Also, you must inform how many years the person will have in the year 2030.
name = input("Enter your name:")
city_of_birth = input("Enter your city of birth:")
year_of_birth = input("Enter you year of birth:")
age_at_2030 = 2030 - int(year_of_birth)
print("Your name is:", name)
print("You were born in the city of", city_of_birth)
print("You were born in", year_of_birth)
print("In 2030, you will have", age_at_2030, "years old")
# return: Enter your name:Amanda
# Enter your city of birth:São Carlos
# Enter you year of birth:1991
# Your name is: Amanda
# You were born in the city of São Carlos
# You were born in 1991
# In 2030, you will have 39 years old