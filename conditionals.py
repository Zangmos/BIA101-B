

# get input from the user
# do calculation based on user input
# give output to the user
# check what string did user input
# if user input input give output to the user

print('* for multipliocation')
print('+ for addition')
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))

if whatUserTyped=="+":
    print("doing addition")
    
print("doing more addition")

if whatUserTyped=="-":
    print("doing subtraction")
    print("doing more subtraction")
print('-------------------')
if whatUserTyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
        if 'b' == 'b':
            print('bisb')


# Objective: a calculator application made using 
# variables and if statements

# STEPS
# 1. get input from user --> DONE

# 2. do calculation based on user input
# 2.1 check what string did user typed
# 2.2 if usser string == * then do multiplicatio and so on

# 3. give output to the user

print('* for multipliocation')
print('+ for addition')
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))

print('-------------------')
if whatUserTyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')

print('doing more addition')

if whatUserTyped == "-":
    print('Doing Subtraction')
    print('doing moresubtraction')
