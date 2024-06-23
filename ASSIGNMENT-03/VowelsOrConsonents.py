def count_vowels_and_consonants(s):
    vowels = "aeiouAEIOU"
    Vowels_count = 0
    Consonants_count = 0

    for char in s:
        if char.isalpha():  # Check if the character is an alphabet letter
            if char in vowels:
                Vowels_count += 1
            else:
                Consonants_count += 1

    return Vowels_count, Consonants_count


# Get input from the user
user_input = input("Enter a string: ")

# Initialize counts
vowels, consonants = count_vowels_and_consonants(user_input)

# Print the counts
print(f"Number of vowels: {vowels}")
print(f"Number of consonants: {consonants}")
