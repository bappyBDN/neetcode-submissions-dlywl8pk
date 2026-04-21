class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=0
        MAXstring=""
        for i in range(len(s)):
            for j in range(i,len(s)):
                string=s[i:j+1]
                if string == string[::-1]:
                    if len(string) > length:
                        length=len(string)
                        MAXstring=string
        return MAXstring