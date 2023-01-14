class Solution:
    def get_next(self,n: int) -> int:
        total_sum = 0
        while n > 0:
            d = n % 10
            n = n // 10
            total_sum += d * d
            return total_sum

    def isHappy(self, n: int) -> bool:
        slow = n
        fast = self.get_next(n)

        while fast != 1 and slow != fast:
            slow = self.get_next(slow)
            fast = self.get_next(self.get_next(fast))

        return fast == 1

s = Solution()
t = s.isHappy(29)
print(t)
