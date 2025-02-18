from caesarcipher import CaesarCipher
from art import *
cipher_logo = text2art("Caesor Cipher", font="black")  # You can choose other fonts too
print(cipher_logo)
# encrypt cipher text

def caesor(original_text , shift_amount , encode_or_decode):
    output_text = ""
    if encode_or_decode == "decode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in alphabet:
            output_text += letter
        else:
            shifted_position = alphabet.index(letter) + shift_amount
            shifted_position %= len(alphabet)
            output_text += alphabet[shifted_position]  # j
            print(f"Here is the {encode_or_decode} result : {output_text}")

should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt , type 'decode' to decrypt : \n").lower()
    text = input("Type your massage : \n").lower()
    shift = int(input("type the shift number: \n"))
    caesor(text,shift,direction)
    restart =input("Type 'yes' if you want to go again .Otherwise type 'No' \n").lower()
    if restart == 'no':
        should_continue = False
        print("Goodbye")

#love calculator
def calculate_love_score(name1, name2):
    name1 = name1.lower()
    name2 = name2.lower()
    combine_name = name1 + name2

    l_count = combine_name.count("l")
    o_count = combine_name.count("o")
    v_count = combine_name.count("v")
    e_count = combine_name.count("e")

    love_count = l_count + o_count + v_count + e_count

    t_count = combine_name.count("t")
    r_count = combine_name.count("r")
    u_count = combine_name.count("u")
    e_count_true = combine_name.count("e")

    true_count = t_count + r_count + u_count + e_count_true

    total = int(f"{true_count}{love_count}")
    print(f"Love score = {total}")
calculate_love_score("bithe", "lutfa")

def greet_with(name , location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
greet_with("Bithee","Dhaka")
greet_with("Laboni","savar")

def life_in_weeks(age):
    left_age = 90 - age
    print(left_age)
    weeks = (left_age*52)
    print(f"You have {weeks} weeks left.")
life_in_weeks(56)

def greet():
    print("hello angela")
    print("how do u do")
    print("isnt the weather nice?")

greet()
def greet_with_name(name,age):
    print(f"My name is {name}")
    print(f"my age is {age}")
greet_with_name("Bithee",24)

#class 7

import random

HANGMAN_PICS = ['''
 3.   +---+
 4.       |
 5.       |
 6.       |
 7.      ===''', '''
 8.   +---+
 9.   O   |
10.       |
11.       |
12.      ===''', '''
13.   +---+
14.   O   |
15.   |   |
16.       |
17.      ===''', '''
18.   +---+
19.   O   |
20.  /|   |
21.       |
22.      ===''', '''
23.   +---+
24.   O   |
25.  /|\  |
26.       |
27.      ===''', '''
28.   +---+
29.   O   |
30.  /|\  |
31.  /    |
32.      ===''', '''
33.   +---+
34.   O   |
35.  /|\  |
36.  / \  |
37.      ===''']
word_list = ["apple","banana","black" ,"berry"]
lives = 6
choice_word = random.choice(word_list)
print(choice_word)
placeholder = ""
word_length = len(choice_word)
for position in range(1,6):
    placeholder+= "_"
print(placeholder)

game_over = False
correct_letters = []
while not game_over:
    guess = input("Guess a letter ").lower()
    display = ""
    for letter in choice_word:
        if letter == guess:
            display +=letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter

        else:
            display += "_"
    print(display)
    if guess not in choice_word:
        lives-=1
        if lives ==0:
            game_over =True
    if "_" not in display:
        game_over = True
        print("You win.")
    print(HANGMAN_PICS[lives])
#class 5
def my_function():
    print("hello world")
my_function()

sky = input()
def my_function():
    if sky == "clear":
        print("Blue")
    elif sky == "cloudy":
        print("gray")
    print("hello")
print("world")


#class-05

import random

fruits = ["Bithee","Moni","Jannt","Mehjabin"]
for fruit in fruits:
    print(fruit)
    print(fruit +" kamal")
    print(fruits)

marks = [45,567,343,56,564,34,2,76,89]
total_mark = sum(marks)
print(total_mark)
sum = 0
for mark in marks:
    sum+=mark
print(sum)

marks = [45,567,343,56,564,34,2,76,89]

max_mark = max(marks)
print(max_mark)
max_mark = 0
for mark in marks:
    if mark> max_mark:
        max_mark = mark
print(max_mark)

sum = 0
for i in range(1,101):
    sum = sum+ i
    #print(i)
print(sum)

for i in range(1,10):
    if i%2==0:
        print("even")
    else:
        print(i)


for i in range(1,100):
    if i%3==0 and i%5==0:
        print("FizzBuzz")
    elif i%3==0:
        print('Fizz')
    elif i%5==0:
        print("Buzz")
    else:
        print(i)
import random
letters = ["a","b","c","d","e","f","j","h","i","j","k"]
symbol = ["@","!","#","%","$"]
number = ['1','2','3','4','5','6','7','8','9']

nr_letters = int(input("how many letters do u like un ur pass"))
nr_symbol = int(input("How many symbol do u like "))
nr_number = int(input("How many number do want to add ur password"))
password = ""
for char in range(0,nr_number):
    password+=random.choice(number)
for char in range(0,nr_symbol):
    password+=random.choice(symbol)
for char in range(0,nr_letters):
    password+=random.choice(letters)
print(password)



