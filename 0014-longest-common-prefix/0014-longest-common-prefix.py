class Solution(object):
    def longestCommonPrefix(self, strs):
        first = min(strs)
        last = max(strs)

        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return first[:i]

        return first[:min(len(first), len(last))]
        