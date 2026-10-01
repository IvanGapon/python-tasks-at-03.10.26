class Solution:
    def checkRecord(self, s: str) -> bool:
        if (s.count("A") >= 2 or s.count("LLL") > 0):
            return False
        return True
