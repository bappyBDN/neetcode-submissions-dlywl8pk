class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res=[]
        n=len(nums)
        nums.sort()
        l=0
        r=0
        
        while r< n:
            nums[l]=nums[r]
            while r < n and nums[r]==nums[l]:
                r+=1
            l+=1
        return l
            


        

        