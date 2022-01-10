class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
        di = x = y = 0
        for instruction in instructions:
            if instruction == 'L': 
                di = (di + 1) % 4
            elif instruction == 'R': 
                di = (di - 1) % 4
            else: x, y = x + dirs[di][0], y + dirs[di][1]
        
        if x == 0 and y == 0 or di > 0: 
            return True
        return False
