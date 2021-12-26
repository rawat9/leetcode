class Solution:
    def countMatches(self, items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
        matchCount = 0
        
        for item in items:
            if ruleKey == 'type':
                if item[0] == ruleValue:
                    matchCount += 1
            if ruleKey == 'color':
                if item[1] == ruleValue:
                    matchCount += 1
            if ruleKey == 'name':
                if item[2] == ruleValue:
                    matchCount += 1
                    
        return matchCount