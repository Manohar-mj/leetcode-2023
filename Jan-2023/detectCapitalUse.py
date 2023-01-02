https://leetcode.com/problems/detect-capital/solutions/2986755/python-2-lines-code/


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.islower() or word.istitle(): return True
        else: return False
