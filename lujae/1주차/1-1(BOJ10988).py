def isPalindrome(word):
    return word == word[::-1];

word = input()

determine = isPalindrome(word);

print(1 if determine == True else 0);
