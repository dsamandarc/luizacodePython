#1)The following values receive the types:
#a. 1 - int
# b. 12.6 - float
# c. True - bool
# d. False - bool
# e. -543 - int
# f. -5.78 - float 
# g. "copo" - str
# h. 'Belo dia' - str
#2)Type each line below into the Python shell and tell which ones are correct and which are an error:

# 1 ok
# 1a (error - invalid syntax)
# a1 (error - NameError)
# 1.ok
# .2 ok 
# -.03 ok
# 'agua"limpa' ok
# "agua"" (error - SyntaxError)
# """teste 123""" ok

#3)determine what is the result of the following calculations in Python:
#ai. 10+3 return: 13
#aii. 10-3 return: 7
#aiii. 10*3 return: 30
#aiv. 10/3 return: 3.3333333333333335
#av. 10/3.0 return: 3.3333333333333335
#avi. 13/3 return: 4.333333333333333
#avii. 13/3.0 return: 14.333333333333333
#aviii. 13//3.0 return: 4.0
#bi. 5+30*20 return: 605
#bii. (5+30)*20 return: 700
#biii. ((5+30)*20)/10 return: 70.0
#biv. 5+30*20/10 return: 65.0
#ci. 2<3 return: True
#cii. 9>8 return: True
#ciii. 1 == 1 return: True
#civ. 1 != 2 return: True
#cv. 1 != 1 return: False
#cvi. 4<=4 return: True
#cvii. 5>= 6 return: False
#cviii. 1<2<3 return: True
#cix. 1<2<2 return: False
#cx. 1+2<25/5 return: True
#di. 2**4 return:16
#dii. 26%5 return: 1
#ei. not True return: False
#eii. not False return: True
#eiii. True and True return: True
#eiv. True and False return: False
#ev. False and True return: False
#evi. False and False return: False
#evii. True or True return: True
#eviii. True or False return: True
#eix. False or True return: True
#ex. False or False return: False
#exi. True or True and False return: True
#exii. (True or True) and False return: False
#exiii. not True or False return: False
#exiv. not(True and False) return: True
#exv. not(True and False) and (True or False) return: True
#exvi. 1>2 and 3>4 return: False
#exvii. 1 > 2 and 3 < 4 return: False
#exviii. 1 < 2 and 3 < 4 return: True
#exix. 1 + 2 and 3 + 4 return: 7
#exx. 1+2 or 3+4 return: 3
#exxi. True and 3>5 return: False
#exxii. False and 3>5 return: False

#4)What will be the final value of x?
x = 10
x = x+10
x = 100-x
print(x) #return: 80

# 5) Solve these problems in Python, storing the values and their results in different variables.
# a. Find the area of a square whose side is 2 cm.
square_side = 2
square = square_side**square_side 
print(f'The area of a {square_side}cm square is {square}cm^2') #return: The area of a 2cm square is 4cm^2

# b. A suitcase costs R$120.00. This one received a 5% discount. How much will you pay for her.
suitcase = 120.00
discount = 5
discount_formula = 5/100
discount_value = suitcase*discount_formula 
final_price = suitcase - discount_value
print(f'The final price of a suitcase that costs {suitcase} with a {discount}% is {final_price}') 
#return: The final price of a suitcase that costs 120.0 with a 5% is 114.0

# c. A car is traveling at an average speed of 100 km/h, the journey will be 200 km. 
# How many hours will the trip take?
average_speed_in_km_h = 100
route_in_km = 200
hours_of_trip = int(route_in_km/average_speed_in_km_h)
print(f'The trip will take {hours_of_trip} hours in a average speed of {average_speed_in_km_h}km/h')
#return: The trip will take 2 hours in a average speed of 100km/h

# d. John has 2 lollipops, Mary 3 lollipops and Sofia 1 lollipop. 
# Calculate the total number of lollipops and your average.
john_lollipops = 2
mary_lollipops = 3
sofia_lollipops = 1
total_number_people = 3
total_number_lollipops = john_lollipops + mary_lollipops + sofia_lollipops
average_lollipops_per_people = int(total_number_lollipops/total_number_people)
print(f'The total number of lollipops is {total_number_lollipops} and each person acquire an a average of {average_lollipops_per_people} lollipops.') 
#return: The total number of lollipops is 6 and each person acquire an a average of 2 lollipops.

# e. Davi is 13 years old and her sister is 7 years old. Store in the variable is_older the
# check if David's age is greater than his sister's age.
davi_age = 13
sister_age = 7
is_older = davi_age > sister_age
print(is_older) #return: True

#6) What will be the value of z? What would be another way to write these codes?
#a. z = 3 
z = 3
print (z)
print(type(z)) #return: 3 <class 'int'>

#b. z += 2 
#another way to write this code is: z = z+2
z=0
z += 2
print (z)
print(type(z)) #return: 2 <class 'int'>

#c. z *= 6 -> z is an int and value 2
#another way to write this code is: z = z*2
z=1
z *= 2
print (z)
print(type(z)) #return: 2 <class 'int'>

#d. z /= 5 -> z is a float and value 0.5 
# #another way to write this code is: z = z/2
z=1
z /= 2
print (z)
print(type(z)) #return: 0.5 <class 'float'>

# 7) Consider the following variables:
# egg = 3.4
# cashew = 12.4
# What will be the response value on each line:
# answer1 = egg if 1 > 2 else cashew
# answer2 = egg if egg > cashew else cashew
# answer3 = egg if egg < cashew else cashew
# answer4 = 100 if egg + cashew > 15 else 200
# answer5 = 100 if egg == 3 else 0
egg = 3.4
cashew = 12.4
answer1 = egg if 1 > 2 else cashew
answer2 = egg if egg > cashew else cashew
answer3 = egg if egg < cashew else cashew
answer4 = 100 if egg + cashew > 15 else 200
answer5 = 100 if egg == 3 else 0
print(f' answer1 is {answer1}, answer2 is {answer2}, answer3 is {answer3}, answer4 is {answer4}, answer4 is {answer5}')
#return: answer1 is 12.4, answer2 is 12.4, answer3 is 3.4, answer4 is 100, answer4 is 0

# 8) What is the result of this problem? What is the final value of the variable end?
# ab = 10  Ab = 20  aB = 30  AB = ab + ab - aB  end = AB + 1 
ab = 10
Ab = 20
aB = 30
AB = ab + ab - aB
end = AB + 1
print(AB) #return: -10
print(f'The end value is:{end}') #return: The end value is:-9

#9) Qual é o resultado de cada linha de comando do Python? Siga a ordem dos comandos.
value = input("Enter a value: ")
print("Enter a value: ", value)

tipo = type(value)
x_str = "123"
x = int(x_str)
xf = float(x)
are_equals = x == xf
print("Is a float equal to an int?", are_equals)
#return: Enter a value: 20
#        Enter a value:  20
#        Is a float equal to an int? True

# 18) Make a program that reads a student's grade. Make sure the note is a integer value between zero and 100. 
# If the value is not in this range, inform that the note is invalid. 
# If the grade is greater than 60, it informs that the student was approved; case otherwise, it reports that he was disapproved.
grade = input("Enter our grade: ")

student_grade = int(grade)
if student_grade <=100 and student_grade >0:
    if student_grade>60: print('Your grade is: ', student_grade, 'and you are Approved') 
    else: print('Your grade is: ', student_grade, 'and you are Disapproved')
else: print('Note not valid')
grade = input("Enter our grade: ")

#return: Enter our grade: 50
#        Your grade is:  50 and you are Disapproved

# 19) A salesperson earns a commission from a sale as follows: If the
# sale is…
# ● less than R$1000.00, the seller does not earn any commission;
# ● between R$1,000.00 and R$5,000.00, the seller earns a 10% commission from the
# sale;
# ● between R$5,000.00 and R$10,000.00, the commission will be 20% of the sale;
# ● between R$10,000.00 and R$50,000.00 the commission will be 25% of the sale;
# ● above R$50,000.00 the commission will be 30% of the sale.
# Make a program that reports the amount of the salesperson's commission for a sale.
sale_value2 = input('Enter the sale value:')
sale_value = float(sale_value2)
commission10 = sale_value*0.10
commission20 = sale_value*0.20
commission25 = sale_value*0.25
commission30 = sale_value*0.30
if sale_value < 1000.00: print(f'The sale value was R$', {sale_value}, 'and you did not earn any commission')
elif 1000.00 >= sale_value < 5000.00: 
    print(f'The sale value was R$', {sale_value}, 'and you earned a commission of 10% of this amount, which results in R$', {commission10})
elif 5000.00 >= sale_value < 10000.00: 
    print(f'The sale value was R$', {sale_value}, 'and you earned a commission of 20% of this amount, which results in R$', {commission20})
elif 10000.00 >= sale_value < 50000.00: 
    print(f'The sale value was R$', {sale_value}, 'and you earned a commission of 25% of this amount, which results in R$', {commission25})
else:
    print(f'The sale value was R$', {sale_value}, 'and you earned a commission of 30% of this amount, which results in R$', {commission30})
#return: Enter the sale value:65240.0
#        The sale value was R$ {65240.0} and you earned a commission of 30% of this amount, which results in R$ {19572.0}

# 20) Create a program to calculate the amount to be paid for a given product for the
# company "I don't want a lot of your money". The personnel of this company requested the following:
# ● Let's collect three values:
# ○ The initial parcel amount.
# ○ The percentage value of each parcel.
# ○ The number of parcel.
# ● For each parcel to be paid, the calculation is as follows:
# parcel_value = previous_value + (previous_value * percentage)
# ● In the case of the first parcel, the previous amount is the initial amount.
# Create a program that will show each parcel and its value. For example: if the initial value
# is $100.00, the percentage value is 0.10, and the amount of parcels is 2; the program will show:
# Parcel 1: $110.0
# Parcel 2: $121.0
initial_parcel = input("Enter the initial parcel: ")
percentage = input("Enter the percentage value of each parcel:")
number = input("Enter the number of parcels:")
initial_parcel = float(initial_parcel)
percentage = float(percentage)
initial_number = int(1)
number = int(number)

while number:
    parcel_value = initial_parcel + (initial_parcel*percentage)
    print(f'Parcel', initial_number,':', parcel_value)
    initial_parcel = parcel_value
    if initial_number == number: break
    else: initial_number = initial_number + 1
    
   #return: Enter the initial parcel: 100.0
#           Enter the percentage value of each parcel:0.10
#           Enter the number of parcels:2
#           Parcel 1 : 110.0
#           Parcel 2 : 121.0

#21) The staff of the company Caça-Clientes works with calls to random numbers.
# They are given a list of various ranges of numbers for them to call. 
# On the list received, you have the phone prefix, first suffix and last suffix. 
# Create a script that lists all the telephone numbers, when informed, the prefix and the suffixes. 
# For example, suppose the prefix is “3232” and the first prefix is “0001” and the last suffix is “0005”; 
# then the program will print:
# Your phone numbers are:
# ● 3232-0001
# ● 3232-0002
# ● 3232-0003
# ● 3232-0004
# ● 3232-0005
phone_prefix = input("Enter phone prefix:")
if len(phone_prefix) !=4:
    print("You must enter 4 digits!")
    quit()
phone_first_sufix = input("Enter phone first sufix:")
if len(phone_first_sufix) !=4:
    print("You must enter 4 digits!")
    quit()
phone_last_sufix = input("Enter phone last sufix:")
if len(phone_last_sufix) !=4:
    print("You must enter 4 digits!")
    quit()

phone_prefix = int(phone_prefix)
phone_first_sufix = int(phone_first_sufix)
phone_last_sufix = int(phone_last_sufix)
print(f'Your phone numbers are:')
while phone_first_sufix <= phone_last_sufix:
    print(f'{phone_prefix}-{(str(phone_first_sufix).zfill(4))}')
    phone_first_sufix = phone_first_sufix + 1
    
#return:Your phone numbers are:
#3232-0001
#3232-0002
#3232-0003
#3232-0004
#3232-0005
    
#22)Create a script that reads 10 positive integers and that will display:
# ● The list of read values in order.
# ● The count of each item. For example, if the user entered [1,1,1,1,2, 3], here we present:
# ○ 1: 4x.
# ○ 2: 1x.
# ○ 3: 1x.
# ● An output identifying the number, whether the number is even, and whether it is prime. 
# This will be done separated by commas: 
# For example, [1,2,3,6] was entered. We will present it here:
# ○ 1, odd, not prime
# ○ 2, even, is prime
# ○ 3, odd, is prime
# ○ 6, even, not prime
integers = input("Enter 10 positive integers:")
list1 = []
for i in integers:
    int(i)
    list1.append(i)
print(f'Lista =', list1)

list1.sort()
print(f'Ordered list:', list1)
for i in set(list1):
    count = list1.count(i)
    print(f'{i}: {count},x')
    
list2 = map(int, list1)
for i in list2:
    def is_prime(i):
        for i in range(2, n):
            if (n%i) ==0:
                print(f'not')
        print(f'prime')


for i in set(list1):
    count = list1.count(i)
    print(f'{i}: {count},x')
    
f = False
list2 = map(int, list1)
for e in list2:
    if e > 1:
        for i in range(2, i):
            if (e%i) == 0:
                f=True
                break
    if f:
        print(f'NOT PRIME')
    else:
        print(f"PRIME")
            
        

i = 1
j = 0
list2 = map(int, list1)
for e in list2:
    x = (e/2)
    while i <= e:
        if (e%i) == 0:
            i = i + 1
            j = j + 1
        elif i>=x:
            i = e
            i = i+1
            j= j+1
        else:
            i = i+1
            if(j==2):
                print('Is prime')
            else: ("Is not a prime")
        
                
    if i == 0
        print(f'{i}, even, is not a prime number')
    elif i == 1
        print(f'{i}, odd, is not a prime number')
    elif i==2:
        print(f'{i}, even, is a prime number')
    elif i%2 == 0:
        print(f'{i}, even, is not a prime number')
    else: 
        
    
    if i > 1:
        if (i%2) == 0 and i!=2: 
            print(f'{i}, even, is not a prime number')
        elif i==2:
            print(f'{i}, even, is a prime number') 
        elif i == 0:
            print(f'{i}, even, is not a prime number')
        else: 
               
       x = primo if x%x ==0 and x%1 == 0                   
    #     elif (i%i) != 0 and (i%2) != 0:
    #         if i == 3 or 1 == 5:
    #             print(f'{i}, odd, is a prime number')
    #         elif [(i%3) == 0 or (i%5) == 0 or (i%7) == 0 or (i%9) == 0]
    #             print(f'{i}, odd, is not a prime number')
    #     else:
    #         print(f'{i}, odd, is a prime number')
    # if i == 0:
    #     print(f'{i}, even, is not a prime number')
        

    # elif int(i) % 2 == 0 and int(i) % int(i) != 1 and int(i) % 1 !=0:
    #     print(f'{i}, even, not a prime number')
    # elif int(i) % 2 != 0 and int(i) % int(i) != 1 and int(i) % 1 !=0:
    #     print(f'{i}, odd, not a prime number')
    # elif int(i) % 2 != 0 and int(i) % int(i) == 1 and int(i) % 1 == 0:
    #     print(f'{i}, odd, is a prime number') 
   
# while i != i in list1:
#     count = list1.count(i)
    
# else:
#     list1[(list1.index(i))+1]    
# x = [(i, list1.count(i)) for i in list1]
# print(x)
# for i in list1:
#     count = list1.count(i)
#     # if not i in x:
#     #     x.append(count)
#     # if not i in x:
#     #     list1.append(i)
#     # else:
#     #     list1.index()
#     print(count)
    # print(f'{i}, {x}x')
        
    # else:
    #     list1.remove(i)
    #     x = list1.count(i)
    #     print(f'{i}, {x}x')
       
            

        
        
        

# for element in list1:
#     a = list1.count(element)
#     while any(element != element for element in list1):
#         print({element},{a})
    
    
print(list)
