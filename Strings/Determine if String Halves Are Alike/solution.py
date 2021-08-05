class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        mid = len(s)//2        # mid of string
        left = s[:mid]
        right = s[mid:]
        vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
        left_count = 0
        right_count = 0
        for vowel in vowels:
            if vowel in left and vowel not in right:
                left_count += left.count(vowel)
            elif vowel in right and vowel not in left:
                right_count += right.count(vowel)
            elif vowel in left and right:
                left_count += left.count(vowel)
                right_count += right.count(vowel)

        return left_count == right_count


# Time Complexity = O(N)