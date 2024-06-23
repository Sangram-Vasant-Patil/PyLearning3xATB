def reverse_string_loop(s):
    reversed_str = ''
    for char in s:
        reversed_str = char + reversed_str
    return reversed_str

# Get input from the user
user_input = input("Enter a string to reverse: ")

# Reverse the input string using the function
reversed_string = reverse_string_loop(user_input)

# Print the reversed string
print(f"Reversed string: {reversed_string}")