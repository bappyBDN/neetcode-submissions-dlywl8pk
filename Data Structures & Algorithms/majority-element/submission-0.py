class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic={}
        maxcount=0
        ans=0
        for i in nums:
            dic[i]=dic.get(i,0)+1

            if dic[i] > maxcount:
                maxcount=dic[i]
                ans=i
        return ans



       

        