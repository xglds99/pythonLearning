class Solution:
    def reorderSpaces(self, text: str) -> str:
        words = text.split()
        print(len(words))
        space = text.count(' ')
        print(space)
        if len(words) == 1:
            return words[0] + ' ' * space
        per_space, rest_space = divmod(space, len(words) - 1)
        return (' ' * per_space).join(words) + ' ' * rest_space

domo = Solution()
ans = domo.reorderSpaces("  this  is  a  demo   ")
print(ans)
