class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        n=len(nums)
        nums.sort() 
        if not nums:
            return 0
        
        left=nums[0]
        
        cnt=0
        i=0
        res=0
        while i < n :
            if left != nums[i]:
                left=nums[i]
                cnt=0
            while i<n and nums[i]==left:
                i +=1
            cnt+=1
            left += 1
            res = max(res,cnt)
        return res
        
            



        