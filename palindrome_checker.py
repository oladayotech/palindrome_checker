import time

def type_text(text, delay=0.04):
    for char in text:
        print(char, end="", flush= True)
        time.sleep(delay)
    print()

type_text("Palindrome Checker Project \n")

type_text("""A simple yet efficient program designed to check if a given input string is a palindrome. 
A palindrome is a word, phrase, number, or other sequences of characters that reads the same forward and backward (ignoring spaces, punctuation, and capitalization).\n""")
    
def input_validation():
    # Validates user input and returns the input string.
    while True:
        try:
            user_input = input("Enter a word to check if it is a palindrome: ")
            if not user_input.strip().lower():
                print("User's input can't be empty")
                input_validation()
            else:
                return user_input
        except Exception as e:
            print(e)

inputs = input_validation()

def isPalindrome(input_to_check):
    # Checks if the input string is a palindrome and returns a boolean value.
  startIndex = 0
  endIndex = len(input_to_check) -1

  for x in input_to_check:
    if input_to_check[startIndex] != input_to_check[endIndex]:
      return type_text(f"{False}! This is not a palindrome \n")
    startIndex += 1
    endIndex -= 1
  return type_text(f"{True}! This is a palindrome \n")

isPalindrome(inputs)

def main():
    type_text("Do yo want to play again (yes/no):")
    user_input = input()
    if user_input.lower() == "yes":
        inputs = input_validation()
        isPalindrome(inputs)
        main()
    else:
        type_text("Thank you for playing")

if __name__ == "__main__":
    main()
