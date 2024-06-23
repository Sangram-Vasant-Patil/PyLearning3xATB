def reverse_string_stack(s):
    stack = list(s)
    reversed_str = ''
    while stack:
        reversed_str += stack.pop()
    return reversed_str

# Get input from the user
user_input = input("Enter a string to reverse: ")

# Reverse the input string using the function
reversed_string = reverse_string_stack(user_input)

# Print the reversed string
print(f"Reversed string: {reversed_string}")
