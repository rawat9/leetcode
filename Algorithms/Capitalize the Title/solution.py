class Solution:
    def capitalizeTitle(self, title: str) -> str:
        title = title.lower().split()
        return " ".join(list(map(lambda x: x.title() if len(x) > 2 else x, title)))
