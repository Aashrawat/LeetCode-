class Solution(object):
    def lengthOfLastWord(self, s):
        i = len(s) - 1

        # Skip trailing spaces
        while i >= 0 and s[i] == " ":
            i -= 1

        end = i

        # Find the start of the last word
        while i >= 0 and s[i] != " ":
            i -= 1

        return end - i