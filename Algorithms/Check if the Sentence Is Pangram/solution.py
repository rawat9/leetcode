from string import ascii_lowercase as alphabet

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        for char in alphabet:
            if char not in sentence:
                return False
            
        return True