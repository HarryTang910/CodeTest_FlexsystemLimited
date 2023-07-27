def number_to_words(number):
    # Dictionary to store the word representations of numbers
    words_dict = {
        0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five",
        6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven",
        12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen",
        17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
        40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty",
        90: "ninety", 100: "one hundred"
    }

    if number in words_dict:
        return words_dict[number]
    elif number > 20 and number < 100:
        # For numbers between 21 and 99, decompose into tens and ones places
        tens = number // 10 * 10
        ones = number % 10
        return words_dict[tens] + ("-" + words_dict[ones] if ones > 0 else "")
    elif number == 100:
        return words_dict[100]
    else:
        return "Number out of range (0-100)"

"""
# Test cases
print("Output: " + number_to_words(13) + " (13)")   # Output: "thirteen"
print("Output: " + number_to_words(45) + " (45)")   # Output: "forty-five"
print("Output: " + number_to_words(50) + " (50)")   # Output: "fifty"
print("Output: " + number_to_words(100) + " (100)")  # Output: "one hundred"
print("Output: " + number_to_words(101) + " (101)")  # Output: "Number out of range (0-100)"
"""

def main():
    while True:
        try:
            # Get user input
            user_input = input("Enter a number between 0 and 100 (or 'n' to exit): ")

            # Check if the user wants to exit
            if user_input.lower() == 'n':
                print("Exiting the program.")
                break  # Exit the loop if the user enters 'n' or 'N'

            # Convert user input to an integer
            user_number = int(user_input)

            if 0 <= user_number <= 100:
                # Call the function and print the result
                result = number_to_words(user_number)
                print(f"The word representation of {user_number} is: {result}")
            else:
                print("Please enter a number between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    main()

