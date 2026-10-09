class Solution:
    def checkRecord(self, s: str) -> bool:
        return not (s.count("A") >= 2 or s.count("LLL") > 0)

