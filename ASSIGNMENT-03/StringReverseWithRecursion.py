def reverse_string_recursion(s):
    if len(s) == 0:
        return s
    else:
        return s[-1] + reverse_string_recursion(s[:-1])

# Get input from the user
user_input = input("Enter a string to reverse: ")

# Reverse the input string using the function
reversed_string = reverse_string_recursion(user_input)

# Print the reversed string
print(f"Reversed string: {reversed_string}")
