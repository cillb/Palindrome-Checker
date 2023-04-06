# Palindrome Checker

This program takes a string input, and returns whether or not a palindrome is found in the string. There is a priority in how it checks for a palindrome:

1. If the string is a single word, it checks if it is a palindrome.
2. If the string is multiple words;

    1. The whole string is checked is it is a palindrome.

    2. Starting with the first word, it checks for a palindrome with that word, then if that and the second word form a palindrome and so on.

    3. If there are no palindromes starting with the first word, the process is applied again starting with the second word and so on, until just the last word is checked if it is a palindrome.

The string that is inputted can be written in any way, with capital letters and special characters included. The string is cleaned up in the program so that the checks can be made.