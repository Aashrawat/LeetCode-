class Solution(object):
    def mySqrt(self, x):
        i = 0

        while (i + 1) * (i + 1) <= x:
            i += 1

        return i