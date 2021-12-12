class Solution:
    def interpret(self, command: str) -> str:
        result = ""
        
        for i in range(len(command)):
            if command[i] == 'G':
                result += command[i]
                
            elif command[i] == '(':
                if command[i+1] == ')':
                    result += 'o'
                else:
                    result += 'al'
                
        return result