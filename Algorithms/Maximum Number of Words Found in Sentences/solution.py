class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        ht = {}
        for sentence in sentences:
            ht[sentence] = len(sentence.split())

        return max(ht.values())
