class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n=len(s2)
        for i in range(n):
            ans=s2[i: i+len(s1)]
            if sorted(s1) == sorted(ans):
                return True
            
        return False
            

        