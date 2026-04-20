class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        res=[0]*n
        
        for i in range(0,n):
            maxi=-1
            for j in range(i+1,n):
                maxi=max(maxi,arr[j])
            res[i]=maxi
        return res


        