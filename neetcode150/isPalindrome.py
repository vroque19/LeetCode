class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""
    
        # Iterate over the characters in the input string
        for c in s:
            if c.isalnum():
                new_string += c
        print(new_string)
        # Convert the new_string to lowercase
        new_string = new_string.lower()

        # Compare the new_string with its reverse
        return new_string == new_string[::-1]