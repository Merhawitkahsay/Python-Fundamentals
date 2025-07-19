

'''Chained Conditional

A chained conditional involves multiple conditions that are evaluated in sequence. It typically uses a series of if, else if, and else statements to check different conditions sequentially. If one of the conditions is true, the corresponding block of code is executed, and the rest of the conditions are skipped.

if #condition1:
    # Execute this block if condition1 is true
elif #condition2:
    # Execute this block if condition2 is true
elif #condition3:
    # Execute this block if condition3 is true
    
else:
    # Execute this block if none of the above conditions are true
'''

#Example:

def grade_chained(score):

    if score >= 90:

        return "A"

    elif score >= 80:

        return "B"

    elif score >= 70:

        return "C"

    elif score >= 60:

        return "D"

    else:

        return "F"

 
   
'''Nested Conditional

A nested conditional occurs when one conditional statement is placed inside another conditional statement. This allows for more complex decision-making, as the inner conditional is only evaluated if the outer conditional is true.


if #condition1:
    # Execute this block if condition1 is true
    if #condition2:
        # Execute this block if condition2 is true (and condition1 is also true)
    else:
        # Execute this block if condition1 is true but condition2 is false
else:
    # Execute this block if condition1 is false

'''


#Example:
def grade_nested(score):

    if score >= 60:

        if score >= 70:

            if score >= 80:

                if score >= 90:

                    return "A"

                else:

                    return "B"

            else:

                return "C"

        else:

            return "D"

    else:

        return "F"



'''Key Differences

1.Structure:· 
    Chained conditionals are linear and evaluate conditions in a sequence.     
    Nested conditionals are hierarchical, with one conditional statement contained within another.
2.Use Cases:
    Chained conditionals are useful when you have multiple distinct conditions to evaluate.
    Nested conditionals are useful when you need to evaluate additional conditions that depend on the truth of a previous condition.
3. Readability:     
    Chained conditionals can be easier to read when dealing with multiple independent conditions.
    Nested conditionals can become complex and harder to read if there are many levels of nesting.
    
    In summary, both chained and nested conditionals are valuable tools in programming for controlling the flow of execution based on conditions, but they serve different purposes and are structured differently. 



Reference

Downey, A. (2015). Think Python: How to Think Like a Computer Scientist (2nd ed.). Green Tree Press. Retrieved from https://greenteapress.com/thinkpython2/thinkpython2.pdf
'''