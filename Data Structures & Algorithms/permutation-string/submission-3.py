class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1 = sorted(list(s1))
        len_s1 = len(s1)
        for i in range(len(s2)+1-len_s1):
            if s1 == sorted(list(s2[i:i+len_s1])):
                return True
        return False