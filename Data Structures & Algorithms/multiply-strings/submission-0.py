class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        maping={'0':0, '1':1, '2':2, '3':3, '4':4, 
               '5':5, '6':6, '7':7, '8':8, '9':9}
        res1=0
        res2=0
        for i in num1:
            res1=10*res1+maping[i]
        for i in num2:

            res2=10*res2+maping[i]
        ans=res1*res2
        final=str(ans)
        return final

        
        