class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}
        total = 0 
        
        for x in range(len(nums)):
            
            total = target - nums[x]

            if total in hashmap: 

                    
                return [x, hashmap[total]]
                
            hashmap[nums[x]] = x
            
            