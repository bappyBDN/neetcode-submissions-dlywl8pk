class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[0]*n
        maxi=-1
        
        for i in range(n-1,-1,-1):
            res[i]=maxi
            maxi=max(arr[i],maxi)
        return res





        