class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashset = set()

        for n in nums:
            if n in hashset:
                return True
            hashset.add(n)
        return False
        

        # for n in range(len(nums)):
        #     for j in range(n+1,len(nums)):
        #         if nums[n] == nums[j]:
        #             return True 
            
        # return False