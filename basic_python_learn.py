

import random
import my_module
#random_integers = random.randint(1,10)
#random_integers = random.random() * 10
random_integers = random.uniform(1,10)
print(random_integers)
print(my_module.my_number)

#class 2
#project
total_bill = 124.56
print("what was the total bill? $",total_bill)
tips = [10,12,15]
tip =tips[1]
print("how much tip would you like to give ? 10,12, or 15?",tip)
split_bill = int(input("How many people to split the bill ?"))
print(split_bill)
total_bill_with_tips = total_bill + tip
pay = total_bill_with_tips/split_bill
print("Each person should pay: ",pay)


10
name = input("what is ur name?")
print(f"hello , {name}")
height = 1.65
weight = 84
height_sqrt = height * height
bmi =(weight)/(height_sqrt)

print(bmi)
print(round(bmi,2))

print(round(2.6))


print(3*5)
result = ((5**3 - 12) * (7 + 4/2) // 3) % 7 + (15 * (3**2 - 9/3) / (4 + 8%3))
print(result)
print(type(3*3+3/3-3))
print(5//3)
print("Bithee"[3])
print("Bithee"[-2])
print("Number of letters in your name " + str(len(input("Enter your name"))))
print("123" + "456")
print(123_4556_567)


mystery = 734_529.678
print(type(mystery))

print(type("hello"))
print(type(45.67))
print(type(345))
print(type(True))
#class 1

print("Welcome to the Band Name Genarator.")
city_name = input("What's the name of city you grew up in?")
print(city_name)
pet_name = input("Whats your pet's name?")
print(pet_name)
print("your band name could be", city_name , pet_name )

glass1 = "milk"
glass2 = "juice"
temp = glass1
glass1 = glass2
glass2 = temp
print(glass1)
print(glass2)


name = input("Enter your name ?")
print("User Name = " ,name)
print("Length" ,len(name))

print("Hello "+ input("Enter your name ?") + "!")

print("1. Mix 500g of Flour, 10g Yeast and 300ml Water in a bowl.")
print("2. Knead the dough for 10 minutes.")
print("3. Add 3g of Salt.")
print("4. Leave to rise for 2 hours.")
print("5. Bake at 200 degrees C for 30 minutes.")