

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

print(grade_nested(85))  # Example usage, should return "B"
print(grade_nested(95))  # Example usage, should return "A"

