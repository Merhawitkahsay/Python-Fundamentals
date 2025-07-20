
#Write program to display your name and perform following operations on it:
#1. Display n characters from left. (Accept n as input from the user)
#2. Count the number of vowels.
#3. Reverse it.


#Input name prompt

name = str(input("What is your name? \n"))



#Display n characters from left. (Accept n as input from the user)

def display_name(name):
    display_character = int(input("Enter the number of characters you want to display?: "))
    print("\nHere are the characters you wanted to display: ")
    for x in range(display_character):
        print (name[0:display_character])
        display_character -= 1




#count number of vowels

def count_vowels(name):
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    count = 0
    for letter in vowels:
        if letter in name:
            count += 1
    print("\nNumber of vowels in your name: ", count)



#Reverse

def reverse(name):
        reverse = name[::-1]
        print("\nyour name in reverse: : ", reverse)



display_name(name)
count_vowels(name)
reverse(name)






