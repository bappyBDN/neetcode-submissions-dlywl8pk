class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1,num+1):
            ans=i*i
            if ans > num:
                return False
            if ans == num:
                return True


        