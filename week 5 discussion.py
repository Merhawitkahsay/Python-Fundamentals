
def any_lowercase1(s):
    for c in s:
        if c.islower():
            return True
        else:
            return False

print(any_lowercase1('Hello'))  #output  = False
print(any_lowercase1('hELLO'))  #output  = True


#Explanation:
#This function checks only the first character of the string. Due to the placement of the return statements inside the loop, the function exits after examining just one character. If the first character is lowercase, it returns True; otherwise, it returns False, regardless of the rest of the string.
#The output incorrect because "Hello" / "hELLO" does contain lowercase letters, but the function stops after checking 'h / H'.


# 2

def any_lowercase2(s):
    for c in s:
        if 'c'.islower():
            return 'True'
        else:
            return 'False'

print(any_lowercase2('WORLD'))   #output = True

#Explanation:
#This function checks whether the literal character 'c' is lowercase, which is always true. The expression 'c'.islower() does not evaluate the variable c, but the string 'c'.
#This is incorrect because the function will always return 'True' regardless of the string input.


# 3

def any_lowercase3(s):
    for c in s:
        flag = c.islower()
    return flag

any_lowercase3("ETHIOPIa")  # Returns True
any_lowercase3("ethiopiA")  # Returns False


#Explanation:
#This function checks whether the literal character 'c' is lowercase, which is always true. The expression 'c'.islower() does not evaluate the variable c, but the string 'c'.
#This is incorrect because the function will always return 'True' regardless of the string input.


# 4


def any_lowercase4(s):
    flag = False
    for c in s:
        flag = flag or c.islower()
    return flag

print(any_lowercase4("HELLo"))  # Returns True
print(any_lowercase4("HI"))   # Returns False


#Explanation:
#This is the correct implementation. The or operator ensures that once a lowercase letter is found, the flag remains True for the rest of the loop. The function evaluates all characters and accumulates the result correctly.

# 5


def any_lowercase5(s):
    for c in s:
        if not c.islower():
            return False
    return True
print(any_lowercase5("abcD"))  # Returns False
print(any_lowercase5("abcd"))  # Returns True

#Explanation:
#This function checks if all characters are lowercase, not whether any are. It returns False at the first non-lowercase character and only returns True if the entire string is lowercase.
#Incorrect Example:
#This is technically correct based on its logic, but it contradicts the goal of checking for any lowercase character.


