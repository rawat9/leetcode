class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_string = ""

        for i in s.lower():
            if i.isalnum():
                new_string += i

        return new_string == new_string[::-1]

# Time Complexity = O(n)
