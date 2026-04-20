class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        total=0
        for i in range(n):
            current=set()
            for j in range(i,n):
                if s[j] in current:
                    break
                current.add(s[j])
            

                    
                
                
            
            total=max(len(current),total)
        return total
            

