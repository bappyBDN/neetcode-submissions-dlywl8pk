class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n=len(nums)
        l=1
        for i in range(1,n):
            if nums[i]!=nums[i-1]:
                nums[l]=nums[i]
                l+=1
        return l
            


        

        