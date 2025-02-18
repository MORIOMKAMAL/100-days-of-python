#class-11
import random
def deal_card():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    card = random.choice(cards)
    return card

user_cards = []
computer_cards = []

for _ in range(2):
    new_card = [deal_card()]
    user_cards.append(new_card)



#class_10
def add(n1 , n2):
    return  n1 + n2
def sub(n1 , n2):
    return  n1 - n2
def mul(n1 , n2):
    return  n1 * n2
def div(n1 , n2):
    return  n1 / n2

operation = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}
#print(operation["*"](4,8))
def calculator():
    should_accumulate = True
    num1 = float(input("What is the first number? : "))
    while should_accumulate:

        for symbol in operation:
            print(symbol)
        operation_symbol = input("Pick an operation")
        num2 = float(input("What is the next number? "))
        answer = operation[operation_symbol](num1,num2)
        print(f"{num1}{operation_symbol}{num2} = {answer}")
        choice = input(f"Type 'y' to continue calculating with {answer} ,or type 'n' to start a new calculator")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()
def my_function(a):
    if a < 40:
        return
        print("Terrible")
    if a < 80:
        return "Pass"
    else:
        return "Great"


print(my_function(25))
def outer_function(a, b):


    def inner_function(c, d):
        return c + d


    return inner_function(a, b)

result = outer_function(5, 10)
print(result)

def is_leap_year(year):
    if (year %4==0) and (year%400==0 or year %100!=0):
        return True
    else:
        return False
print(is_leap_year(2024))

def function_1(f_name , l_name):
    if f_name == "" or l_name == "":
        return "you did not provide valid inputs"
    format_fname = f_name.title()
    format_lname = l_name.title()
    return f"result: {format_fname}{format_lname}"
output = function_1(input("Give me ur first name :" ), input("Give  me your last name :"))
print(output)

def function_1(text):
    return text + text
def function_2(text):
    return text.title()

output = function_2(function_1("hello"))
print(output)


def format_name(f_name , l_name):
    formated_fname = f_name.title()
    formated_lname = l_name.title()
    return f"{formated_fname} {formated_lname}"
print(format_name("Bihee","kamal"))

starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}
starting_dictionary["c"] =7
final_dictionary = starting_dictionary
print(final_dictionary)



travel_blog ={
    "France" :{
        "cities_visited" : ["paris","little","dijon"],
        "total_visit" : 12
    },
    "germany" : {
        "cities_visited" : ["berlin","stuttgart","hamburg"],
        "total_visit" : 12
    }
}
print(travel_blog["germany"]["cities_visited"][1])



student_scores = {
    "Harry": 85,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 65,
    "Neville": 62,
}

student_grades = {}

for student, score in student_scores.items():
    if score >= 91:
        student_grades[student] = "Outstanding"
    elif score >= 81:
        student_grades[student] = "Exceeds Expectations"
    elif score >= 71:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"

print(student_grades)





colours = {
    "apple" : "red",
    "pear" : "green",
    "banana" : "yellow"
}
print(colours["pear"])
colours["strawberry"] ="baby pink"
print(colours)
for key in colours:
    print(key)
    print(colours[key])