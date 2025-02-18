import random
#rock
rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

# Paper
paper="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

# Scissors
scissor ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

random_int=random.randint(1,4)
print(random_int)

if random_int == 0:
    print(rock)
elif random_int ==1:
    print(paper)
else:
    print(scissor)

#type 0 rock ,1 paper ,sciessor 2
user_choice = int(input("ANYTHING YOU CAN CHOICE. enter your choice...."))
computer_user = random.randint(1,3)
print(computer_user)
if user_choice == 0 and computer_user == 2:
    print("you are win")
elif computer_user == 0 and user_choice == 2:
    print("you lose")
elif computer_user ==1 and user_choice == 2:
    print("you win")
elif computer_user == user_choice:
    print("draw")
else:
    print("invalid")



import random
list = ["Apple","Cherry" ," Pear" ,"Strawberry"]
list1 = ["Bithee","jannat","moni"]
list3 = [list,list1]
print(list3[1][1])
print("\n")
print(random.choice(list))

random_index = random.randint(1,4)
print(list[random_index])
list[1] = "Jack fruit"
list.extend(["cherry" ,"mango"])
print(list)
print(list[-3])


import random
import my_module
rand_int = random.randint(0,1)
#rand_int = random.random()
#rand_int = random.uniform(1,10)
if rand_int==0:
    print("head")
else:
    print("tail")
#print(rand_int)
#print(my_module.my_number)



#day 3
print("Welcome to Treasure island")
print("Your mission is to find the trasure")
dec = input("Take your 1st decision -----")
if dec == "left":
    dec1 = input("Take your 2nd decision----- ")
    if dec1 == "swim":
        print("Game Over")
    elif dec1 == "wait":
        dec3 = input("Take your 2nd decision. choose ur door----- ")
        if dec3 == "red":
            print("Game Over")
        elif dec3 == "blue":
            print("Game over")
        elif dec3 == "yellow":
            print("You win")
    else:
        print("Game over")

elif dec == "right":
    print("Game over")





a = 3
b =5
if not a>=b and a!=b:
    print(a)

print("Welcome to python Pizza Deliverise!")
small_pizza = 15
medium_pizza = 20
large_pizza = 25

add_chesse = 1
size = input("What size pizza do you want? S ,M or L")
extra_cheese = input("Do you want extra cheese? Y or No")
pepperoni = input("Do you want pepperoni on your pizza?")
if extra_cheese == "Y":
    small_pizza = small_pizza +1

    medium_pizza = medium_pizza +1
    large_pizza = large_pizza+1
elif pepperoni == "Y":
    small_pizza =  small_pizza +2
    medium_pizza = medium_pizza + 3
    large_pizza = large_pizza + 3

print(small_pizza)
print(large_pizza)
print(medium_pizza)









height = int(input("Enter ur height"))
if height > 120:
    print("you can ride")
    age = int(input("Enter your age"))
    if age<12:
        print("ticket price is +$5")
        ticket_price=5
    elif age>=12 or age<=18:
        print("ticket price is +$7")
        ticket_price=7
    elif age>18:
        print("ticket price is +$12")
        ticket_price = 12
    photo = input("Wants Photos")
    if photo == "yes":
        print("pay extra $3")
        total_price = ticket_price + 3
        print("the total bill is ",total_price)
    else:
        print("No")

else:
    print("you cant ride")


height = int(input("enter the hieght"))
if height >120:
    print("you can ride")
    age = int(input("enter your age"))
    if age>=18:
        print("Ticket price is $12")
    elif age<18:
        print("ticket price is $7")

else:
    print("you cant ride")

number= int(input("What number do u want to check "))
if number % 2 ==0:
    print("the given number is even")
else:
    print("the given number is odd")

print("welcome to the rollercoster6")
height = input("what is your height")
if height> 120:
    print("you are the rise the rollercoster ")
else:
    print("sorry you have to grow taller before you can ride")

