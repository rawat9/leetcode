class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        if colors.count('A') < 3:
            return False
        
        alice = 0
        bob = 0
        for i in range(1, len(colors)-1):
            print(alice, bob)
            if colors[i-1] == colors[i] == colors[i+1] == 'A':
                alice += 1

            if colors[i-1] == colors[i] == colors[i+1] == 'B':
                bob += 1

        return alice > bob
