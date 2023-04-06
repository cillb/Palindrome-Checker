"""
This program prompts a user to input a string, and will check if it is a palindrome.
The string can be a single word, or multiple words. The program will also check if a
multiple word string contains a palindrome, if it is not entirely a palindrome. It will
first check if it has been given a single word, and if so, check if it is a palindrome.
If it detects multiple words, it will check if the full text is a palindrome, and if it
is not, it will search for a palindrome inside of it.
"""
def checksingleword(arg: str):
    return arg == arg[::-1]

def checkphrase(arg: str):
    arg = arg.replace(" ", "")
    return checksingleword(arg)
# initialise a string called palindrome, used by the findpalindrome function to hold any palindrome found
palindrome = ""
def findpalindrome(arg: str):
    global palindrome
    words = arg.split(" ")
    for i in range(len(words)):
        if checksingleword(words[i]):
            palindrome = words[i]
            return True
        else:
            for j in range(1, len(words)-i):
                if words[i][0] == words[i+j][-1]:
                    phrase = " ".join(words[i:i+j+1])
                    if checkphrase(phrase):
                        palindrome = phrase
                        return True
# this function removes any characters that have no effect on whether a word is a palindrome, 
# but would otherwise fail the function
def cleanupstring(arg: str):
    chars = ",.'-!?"
    for c in chars:
        if c in arg:
            arg = arg.replace(c, "")
    return arg
# the program is ran here, the text to be searched must be typed into the prompt
if __name__ == "__main__":
    string = cleanupstring(input("Please enter the word(s) that you would like to check for a palindrome:\n\t\t").lower())
    if " " in string:
        if checkphrase(string):
            print("These words make a palindrome.")
        elif findpalindrome(string):
            print("These words do not make a palindrome, however they do contain a palindrome instead.\nThe palindrome is: %s" % palindrome)
        else: print("That is not a palindrome.")
    else:
        if checksingleword(string):
            print("That word is a palindrome.")
        else: print("That word is not a palindrome.")