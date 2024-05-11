# this is an implementation of 'checking a word if its palindrome or not'
# main2.py contains a more efficient solution

def checkPalindrome(word):

    isPalindrome = 0
    # if condition will check if the string actually has some letters. it shouldn't be empty ofcourse
    if len(word) > 0:
        length = len(word)
        for i in range(length // 2):
            if word[i] != word[-i-1]: # this will pick one character from the left side of the word and one from the right side of the word
                return False

        return True
    else:
        print("Provided string is empty")

# this will take input from human and pass directly to the function 'checkPalindrome'
palindrome = checkPalindrome(input("Human, enter a word please: "))
if palindrome:
    print(f"\nHuman your word is palindrome: {palindrome}")
else:
    print(f"\nHuman your word is not a palindrome: {palindrome}")